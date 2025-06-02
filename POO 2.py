import tkinter as tk

# Variable global para contar los clics
contador = 0

def contar_clics():
    global contador
    contador += 1
    print(f"Has hecho clic {contador} veces")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Contar Clics")

# Crear el botón
boton = tk.Button(ventana, text="Contar Clics", command=contar_clics)
boton.pack(pady=20)

# Ejecutar la aplicación
ventana.mainloop()
