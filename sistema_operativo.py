def verificar_codigo(codigo):
    codigo = codigo.strip().upper()
    if codigo.startswith("PRO"):
        return "El código ingresado es válido."
    else:
        return "El código ingresado no es válido. Por favor, intente de nuevo."

def solicitar_codigo():
    while True:
        cod = input("Digite el código del producto que desea verificar: ")
        if cod.strip():
            mensaje = verificar_codigo(cod)
            print(mensaje)
            break
        else:
            print("No se permite dejar el campo vacío. Por favor, ingrese un código.")

solicitar_codigo()