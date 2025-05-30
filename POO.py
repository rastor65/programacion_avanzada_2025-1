valor = 0
class CuentaBancaria:

    def __init__(self, titular, saldo ):
        self.titular = titular
        self.__saldo = saldo

    def depositar(self):
        self.__saldo += valor
        print("deposito exitoso, nuevo saldo {self.__saldo}")
    
    def retirar(self):
        self.__saldo -= valor
        print("retiro exitoso, nuevo saldo {self.__saldo}")
    
    def get_saldo(self):
        return self.__saldo
    
    def set_saldo(self, nuevo_saldo):
        if nuevo_saldo > 0:
            self.__saldo = nuevo_saldo
            print("saldo actualizado: {self.__saldo}")
