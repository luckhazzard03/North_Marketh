import sqlite3
import bcrypt

# Nombre del archivo de base de datos
DB_NAME = "usuarios.db"

# Función para crear la tabla 'usuarios' si no existe aún
def crear_tabla():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL
        )
    """)
    conn.commit()# Guardamos los cambios en la base de datos
    conn.close() # Cerramos la conexión

# Función para verificar si el usuario existe y si la contraseña es correcta
def verificar_usuario(username, password):
    conn = sqlite3.connect(DB_NAME)  # Abrimos conexión a la base de datos
    cursor = conn.cursor()           # Creamos un cursor
    cursor.execute("SELECT password FROM usuarios WHERE username=?", (username,))
    fila = cursor.fetchone()
    conn.close()

    if fila:
        hashed = fila[0]
         # Usamos bcrypt para comparar la contraseña ingresada (sin hashear) con la almacenada (hasheada)
        return bcrypt.checkpw(password.encode(), hashed.encode())
    return False
