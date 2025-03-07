def validar_codigo_producto():
    # Ingresar código de producto
    codigo_producto = input("Ingrese el código de producto: ")

    # Verificar si el código comienza con "PRO" (en mayúsculas)
    if codigo_producto.upper().startswith("PRO"):
        print("Código válido")
    else:
        print("Código inválido")

validar_codigo_producto()