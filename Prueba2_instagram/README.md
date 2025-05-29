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
git clone https://github.com/tu_usuario/Prueba2_instagram.git
cd Prueba2_instagram

2. Crea un entorno virtual (opcional pero recomendable):

python3 -m venv env
source env/bin/activate

3. Instala las dependencias:

pip install -r requirements.txt
