#crear clase persona con atributos nombre y edad con metodo saludar
#que imprima "hola mi nombre es <nombre> y tengo <edad>


class persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"mi nombre es {self.nombre} y tengo {self.edad}")

nombre=str(input("Ingresa tu nombre: "))
edad=int(input("Ingresa tu edad: "))

persona1= persona(nombre, edad)
persona1.saludar()

#crear ventana que diga "saludar", cuando se hace click en el botón, se debe imprimir "¡Hola desde el botón!"
import tkinter as tk

ventana=tk.Tk()
ventana.title="Saludar"

def saludo():
    print("¡Hola desde el botón!")

boton=tk.Button(ventana,text="saludar",command=saludo)
boton.pack(pady=20)