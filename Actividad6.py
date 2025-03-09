nombre =(input("querido(a) usuario por favor ingrese su nombre: "))
if len(nombre) > 3 and len(nombre) < 8:
    print(f"Hola querido(a) {nombre.upper()},Bienvenido(a).")
else:
    input("querido(a) usuario su nombre debe tener de 3 a 8 caracteres")
    
