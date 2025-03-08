def verificar_codigo():
    codigo = input("Ingresa el código del producto: ").upper()
    
    if codigo.startswith("PRO"):
        print("Código válido")
    else:
        print("Código inválido")

verificar_codigo()
