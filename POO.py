valor = 0
class CuentaBancaria:

    def __init__(self,titular,saldo):
        self.titular =titular
        self.__saldo =saldo
    
    def depositar(self):

        self.saldo +=valor
        print (f"su deposito ha sido exitoso, su nuevo saldo es de {self.__saldo}")
    
    def retirar(self):

        self.saldo-=valor
        print (f"su retiro ha sido exitoso, su nuevo saldo es de {self.__saldo}") 
    
    def getSaldo(self):

        return self.__saldo
    
    def setSaldo(self, nuevoSaldo):
        if nuevoSaldo >0:
            self.__saldo = nuevoSaldo 
            print(f"Saldo actualizado: {self.__saldo}")
    
    def __str__(self):
        print(f"su nombre es de: {self.titular}")

class vehiculo:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        print(f"su vehiculo es {nombre} del tipo {tipo}")

class persona:
    def __init__(self,edad,nombre):
        self.edad=edad
        self.nombre=nombre

class profesor:
    def __init__(self, pregrado, añosExp, clase):
        self.pregrado= pregrado
        self.añosExp= añosExp
        self.clase=clase

    def dictarClase (self):
        print ("el profe está dictando la clase")

class estudiante:
    def __init__(self, pregrado):
        self.pregrado= pregrado

    def estudiar(self):
        print ("estudiando")

class trabajador:
    def __init__(self, horario,rol):
        self.horario=horario
        self.rol=rol


    def trabajar(self):
        print("trabajando")

class asistente:
    def __init__(self):