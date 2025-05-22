import sqlite3
import bcrypt
from database import DB_NAME, crear_tabla

crear_tabla()# Llamamos a la función para asegurarnos que la tabla 'usuarios' exista antes de insertar datos

def crear_usuario(username, password):
    # Hasheamos la contraseña recibida usando bcrypt y generamos una sal automáticamente
    # Luego decodificamos para almacenar el hash como texto
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO usuarios (username, password) VALUES (?, ?)", (username, hashed))
        conn.commit()
        print("Usuario creado exitosamente.")
    except sqlite3.IntegrityError:
        print("El usuario ya existe.")
    conn.close()


usuario = input("Usuario: ")# Pedimos al usuario que ingrese su nombre
clave = input("Contraseña: ")# Pedimos que ingrese la contraseña (no está oculta aquí)
crear_usuario(usuario, clave)# Llamamos a la función para crear usuario con esos datos
