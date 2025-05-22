import tkinter as tk # Importamos tkinter para la interfaz gráfica y messagebox para mostrar mensajes emergentes
from tkinter import messagebox
import requests # Importamos requests para consumir la API
from database import crear_tabla, verificar_usuario# Importamos nuestras funciones personalizadas para crear la tabla y verificar el usuario


# Al iniciar el programa, nos aseguramos de que la tabla de usuarios esté creada
crear_tabla()

# Función que se ejecuta al hacer clic en el botón de login
def login():
    usuario = entry_usuario.get()  # Obtiene el texto ingresado en el campo de usuario
    clave = entry_contraseña.get() # Obtiene la contraseña ingresada
    
    # Verificamos si el usuario existe y si la contraseña es correcta
    if verificar_usuario(usuario, clave):
        messagebox.showinfo("Éxito", "¡Login exitoso!")
        mostrar_datos_api()
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos.")

# Esta función se ejecuta después de un login exitoso
def mostrar_datos_api():
    ventana_api = tk.Toplevel(ventana)# Creamos una nueva ventana encima de la principal
    ventana_api.title("Personajes de Rick and Morty") # Le damos título a esa ventana
    
    # Realizamos una petición GET a la API de Rick and Morty
    response = requests.get("https://rickandmortyapi.com/api/character")
    # Si la respuesta es exitosa (código 200), mostramos los primeros 5 personajes
    if response.status_code == 200:
        personajes = response.json()["results"][:5]
        for i, p in enumerate(personajes, 1):
             # Mostramos el nombre y estado de cada personaje en la nueva ventana
            tk.Label(ventana_api, text=f"{i}. {p['name']} - {p['status']}").pack()
    else:
        # Si hubo un error al consultar la API, mostramos un mensaje
        tk.Label(ventana_api, text="Error al obtener los datos de la API").pack()

# A partir de aquí creamos la interfaz gráfica principal con campos de usuario y contraseña
ventana = tk.Tk()
ventana.title("Login API")# Título de la ventana principal

# Campo de entrada para el usuario
tk.Label(ventana, text="Usuario:").grid(row=0, column=0, padx=10, pady=10)
entry_usuario = tk.Entry(ventana)
entry_usuario.grid(row=0, column=1)

# Campo de entrada para la contraseña (oculta con asteriscos)
tk.Label(ventana, text="Contraseña:").grid(row=1, column=0, padx=10, pady=10)
entry_contraseña = tk.Entry(ventana, show="*")
entry_contraseña.grid(row=1, column=1)

# Botón para iniciar sesión que llama a la función login()
tk.Button(ventana, text="Iniciar sesión", command=login).grid(row=2, column=0, columnspan=2, pady=10)

# Bucle principal de tkinter para mostrar la ventana
ventana.mainloop()
