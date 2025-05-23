
##Primer punto del quiz
# class Persona:
#     def __init__(self, Nombre, Edad):
#         self.Nombre = Nombre
#         self.Edad = Edad
        
#     def Saludar(self):
#         print(f"Hola, mi nombre es {self.Nombre} y tengo {self.Edad} años")
        
# Yo = Persona (" Ian Lopez", 20)
# Yo.Saludar()
##Segundo punto
# def main():
#     try:
#         numero = int(input("Ingres un numero entero para poder darle una elevacion al cuadrado de ese numero"))
#         numDoble = numero * 2
#         print(f"El doble del {numero} es: {numDoble}")
#     except ValueError:
#         print("Debes ingresar un numero entero mamauevo")
# if __name__== "__main__":
#     main()
##tercer punto
# from tkinter import *
# def Saludar():
#     print("Hola desde el Boton")
# ventana = Tk()
# boton = Button(ventana, text ="SALUDAR", command=Saludar)
# def mostrar_mesaje
# boton.pack(expand=True)
# ventana.mainloop()
##punto cuatro
class Mascota:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo 
    def mostrar_info(self):
        print(f"NOMBRE = {self.nombre} - TIPO = {self.tipo}")


    Mascota1= Mascota("Mia" ,"Perro")
    Mascota2= Mascota("Alfredo", "gato")
    Mascota3= Mascota("Juan", "Pez")
    
list_Mascotas =[Mascota1, Mascota2,Mascota3]
for mascota in List_Mascotas:
    mascota.mostrar_info()
        

        