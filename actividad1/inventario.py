
def verificar_codigo(codigo):
    codigo = codigo.upper()  
    if codigo.startswith("PRO"):
        return "Código válido"
    else:
        return "Código inválido"


codigo_producto = input("Ingrese el código de producto: ")

resultado = verificar_codigo(codigo_producto)
print(resultado)