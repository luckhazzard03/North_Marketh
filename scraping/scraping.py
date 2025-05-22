import requests
from bs4 import BeautifulSoup # Importamos BeautifulSoup para analizar el HTML

#Se define la función buscar_productos que toma una palabra clave como argumento
def buscar_productos(palabra_clave):
    url = f"https://listado.mercadolibre.com.co/{palabra_clave.replace(' ', '-')}"
     # Encabezado para simular que la petición viene de un navegador
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    # Realizamos la petición a la página
    respuesta = requests.get(url, headers=headers)
    if respuesta.status_code != 200:
        print("Error al acceder a MercadoLibre.")
        return

    # Parseamos el contenido HTML con BeautifulSoup
    soup = BeautifulSoup(respuesta.text, "html.parser")
    # Seleccionamos los primeros 5 productos del listado
    productos = soup.select("li.ui-search-layout__item")[:5]

    # Si no se encontraron productos, muestra mensaje y sale
    if not productos:
        print("No se encontraron productos.")
        return

    print(f"\nResultados para: '{palabra_clave}'\n")
    
    
    # Iteramos sobre los productos encontrados
    for i, producto in enumerate(productos, start=1):
        # Título
        titulo_tag = producto.select_one("h3.poly-component__title-wrapper") or \
                     producto.select_one("h2.ui-search-item__title")
        titulo = titulo_tag.text.strip() if titulo_tag else "Título no encontrado"

        # Precio
        precio_entero = producto.select_one("span.andes-money-amount__fraction")
        precio_decimal = producto.select_one("span.andes-money-amount__cents")
        if precio_entero:
            precio = precio_entero.text
            if precio_decimal:
                precio += f",{precio_decimal.text}"
        else:
            precio = "Precio no disponible"

                

        print(f"{i}.Título: {titulo}")
        print(f"   Precio: ${precio}")
        

# Pedimos al usuario una palabra clave para buscar productos
palabra = input("Ingrese palabra clave para buscar: ")
buscar_productos(palabra)
