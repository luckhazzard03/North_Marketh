from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from time import sleep
from openpyxl import load_workbook
import pandas as pd
import re

datos_totales = []


# Configuración del navegador
def configurar_driver():
    options = Options()
    options.add_argument("--start-maximized")
    return webdriver.Chrome(options=options)


# Iniciar sesión manualmente
def iniciar_sesion(driver):
    driver.get("https://www.instagram.com/")
    print("Por favor, inicie sesión manualmente en Instagram.")
    input("Cuando termine de logear, presiona ENTER aquí...")


# Scroll en el modal de seguidores
def scroll_modal(modal, veces=5):
    for _ in range(veces):
        driver.execute_script(
            "arguments[0].scrollTop = arguments[0].scrollHeight", modal
        )
        sleep(2)


# Extraer información del perfil del seguidor
def extraer_info_seguidor(perfil_url):
    driver.get(perfil_url)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "header"))
    )
    sleep(2)

    nombre = "No disponible"
    email = "No disponible (cuenta privada)"
    telefono = "No disponible (cuenta privada)"
    fecha_post = "No disponible (cuenta privada)"
    fecha_union = "No disponible (cuenta privada)"

    try:
        nombre = driver.find_element(By.TAG_NAME, "h2").text
    except:
        pass

    try:
        bio_element = driver.find_element(By.XPATH, "//div[contains(text(), '@')]")
        bio = bio_element.text
        correos = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", bio)
        telefonos = re.findall(r"\+?\d[\d\s().-]{7,}", bio)
        email = correos[0] if correos else email
        telefono = telefonos[0] if telefonos else telefono
    except:
        pass

    try:
        # Scroll para cargar las publicaciones en el perfil
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(2)
        publicaciones = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//article//a[contains(@href, '/p/')]")
            )
        )
        if publicaciones:
            publicaciones[0].click()  # Primera publicación visible
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//time[@datetime]"))
            )
            time_tag = driver.find_element(By.XPATH, "//time[@datetime]")
            if time_tag:
                fecha_post = time_tag.get_attribute("datetime").split("T")[0]
            driver.back()
        else:
            print("[!] No hay publicaciones visibles.")
    except (TimeoutException, NoSuchElementException) as e:
        print(f"[!] No se pudo extraer la fecha de publicación: {e}")

    try:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(2)
        spans = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, '//span[@data-blocks-name="bk.components.Text"]')
            )
        )
        for span in spans:
            texto = span.text.strip()
            if re.match(r"^[A-Za-zÁÉÍÓÚáéíóúñÑ]+ de \d{4}$", texto):
                fecha_union = texto
                break
    except:
        pass

    return {
        "Nombre": nombre,
        "Email": email,
        "Teléfono": telefono,
        "Fecha publicación": fecha_post,
        "Fecha de unión": fecha_union,
    }


# Procesar una cuenta de Instagram y sus seguidores
def procesar_perfil(perfil):
    print(f"\n Abriendo perfil de @{perfil}")
    driver.get(f"https://www.instagram.com/{perfil}/")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "header"))
    )
    sleep(2)

    try:
        followers_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//ul/li[2]//a"))
        )
        driver.execute_script("arguments[0].click();", followers_button)
        sleep(3)

        modal = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, '//div[@role="dialog"]//div[contains(@class, "x1dm5mii")]')
            )
        )
        scroll_modal(modal, veces=3)

        seguidores = driver.find_elements(
            By.XPATH,
            '//div[@role="dialog"]//a[contains(@href, "/") and not(contains(@href, "/stories/"))]',
        )

        urls = set()
        for s in seguidores:
            href = s.get_attribute("href")
            if href and re.match(r"https://www.instagram.com/[^/]+/$", href):
                urls.add(href)

        urls = list(urls)
        print(f"Se encontraron {len(urls)} seguidores únicos.")

        for url in urls[:5]:  # Limitar por seguridad
            info = extraer_info_seguidor(url)
            info["Cuenta origen"] = perfil
            print("\n Info de seguidor:")
            for clave, valor in info.items():
                print(f"• {clave}: {valor}")
            datos_totales.append(info)

    except Exception as e:
        print(f"Error al procesar seguidores: {e}")


# MAIN: ejecución principal del script
if __name__ == "__main__":
    perfiles = ["elcorteingles", "mercadona", "carrefoures"]
    driver = configurar_driver()
    iniciar_sesion(driver)

    for perfil in perfiles:
        procesar_perfil(perfil)

    print("\n Proceso completado.")
    driver.quit()

    if datos_totales:
        df = pd.DataFrame(datos_totales)
        df = df.drop_duplicates(subset=["Nombre", "Cuenta origen"])  # Evitar duplicados
        nombre_archivo = "seguidores_instagram.xlsx"
        df.to_excel(nombre_archivo, index=False)

        # Ajustar ancho de columnas
        wb = load_workbook(nombre_archivo)
        ws = wb.active
        for column_cells in ws.columns:
            length = max(
                len(str(cell.value)) if cell.value else 0 for cell in column_cells
            )
            col_letter = column_cells[0].column_letter
            ws.column_dimensions[col_letter].width = length + 2
        wb.save(nombre_archivo)

        print(f"Archivo Excel guardado como '{nombre_archivo}'")
    else:
        print(
            "No se extrajeron datos. Verifica si Instagram cargó los seguidores correctamente."
        )
