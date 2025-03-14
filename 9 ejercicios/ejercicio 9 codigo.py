def verificar_codigo():
    codigo = input("Ingresa el código del producto: ").strip()

    if codigo.startswith("PRO"):  
        print("El código es válido")
    else:
        print("El Código es inválido")

verificar_codigo()
