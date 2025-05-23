valor = 0
class Banco:
    def __init__(self,titular,saldo):
        self.titular = titular
        self.__saldo = saldo
        
    def depositar(self):
        self.__saldo += valor
        return self.saldo
    
    def retirar(self):
        self.__saldo -= valor
        return self.saldo
    
    def get_saldo(self):
        return self.__saldo
    
    def set_saldo(self,nuevo_saldo):
        if nuevo_saldo > 0:
            self.__saldo = nuevo_saldo
    
    def __str__(self):
        return f"el usuario es el siguiente {self.titular} y su saldo  en su cuenta bancaria es el siguiente {self.__saldo}"