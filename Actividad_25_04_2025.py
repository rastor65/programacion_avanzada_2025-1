class Calculadora:
    def __init__(self):
        print("Bienbenido a la calculadora creada por  ian ")
        
    def dividir(self):
        try:
            num1 = float(input("Ingresa el primer numero"))
            num2 = float(input("ingresa el segundo numero"))
            resultado = num1/num2
            
        except ValueError:
            print("Error debes ingresar  numeros que se puedan dividir")
        except ZeroDivisionError:
            print("Error No se pudo realizar la operacion porque colocaste un cero para dividir >:(")  
        
        finally: 
            print("Gracias por usar mi calculadora me debes 3k ")  
    dividir()
            
if __name__ == "__main__":

    # Llamar al método trabajar
    Calculadora.__init__()
    Calculadora.dividir()