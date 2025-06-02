#crear ventana que diga "saludar", cuando se hace click en el botón, se debe imprimir "¡Hola desde el botón!"
import tkinter as tk

def saludo():
    etiqueta.config (text="¡Hola desde el botón!")

ventana=tk.Tk()
ventana.title="Saludar"
ventana.geometry("300x200")

etiqueta=tk.Label(ventana, text=" ")
etiqueta.pack()

boton=tk.Button(ventana,text="saludar",command=saludo)
boton.pack(pady=20)


ventana.mainloop()