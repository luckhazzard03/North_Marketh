# Scraper de Seguidores de Instagram

Este proyecto permite extraer información pública de los seguidores de las cuentas de Instagram:

- `@elcorteingles`
- `@mercadona`
- `@carrefoures`

Para cada seguidor, se recopila lo siguiente (si está disponible públicamente):

- Nombre de usuario
- Correo electrónico
- Número de teléfono
- Fecha de su primera publicación
- Fecha de unión (si se puede inferir)
- Cuenta de origen (desde cuál fue extraído)

La información se guarda automáticamente en un archivo Excel (`seguidores_instagram.xlsx`).

---

## Requisitos

- Python 3.10+
- Google Chrome
- ChromeDriver compatible con tu versión de Chrome
- Entorno virtual (opcional pero recomendado)

---

## Instalación

1. Clona este repositorio:

```bash
git clone https://github.com/luckhazzard03/North_Marketh.git/Prueba2_instagram
cd Prueba2_instagram

2. Crea un entorno virtual (opcional pero recomendable):

python3 -m venv env
source env/bin/activate

3. Instala las dependencias:

pip install -r requirements.txt


# Politicas de la plataforma 
1. Políticas de la Plataforma de Instagram (Meta Platform Policies)
Fuente oficial: https://developers.facebook.com/policy

Sección 3.2:
“No puedes usar técnicas automatizadas para extraer datos de nuestros productos sin nuestro permiso.”

Sección 3.1.5:
“No recopiles contenido ni información de nuestros Productos usando técnicas de scraping sin nuestro consentimiento previo por escrito.”



2. Términos de uso de Instagram
Fuente: https://help.instagram.com/581066165581870

“No debes acceder ni recopilar datos de Instagram usando medios automatizados (sin nuestro permiso), como bots, spiders, scrapers o crawlers.”

"Instagram prohíbe el uso de técnicas automatizadas como el scraping para obtener datos de sus usuarios, incluyendo la fecha de publicación de los posts. Por esta razón, esa información no está disponible en nuestro análisis, respetando sus políticas oficiales de privacidad y uso de datos."