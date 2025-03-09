

NUMERO6
#SE PIDE EL NOMBRE  DE EL USUARIO PARA PODER SER REGISTRADO 
nombredelusuario = input("ingrese su nombre")
if len(nombre) < 3 o len(nombre) > 8 :
    print (" su nombre no esta bien, revise las condiciones impuestas para ser valido ")
    
 else 
 print (f"bienvenido , {nombredelusuario.upper()}.")    


NUMERO7

comentario = input("Ingrese el comentario: ").lower()
repeticiones = comentario.count("excelente")
print(f"comentario modificado\n-{comentario.strip()}\n Veces que se repitioa \"Excelente\": {repeticiones}.")


NUMERO8

articulo = input("Ingrese el articulo: ").strip()
articulo = articulo.lower().replace("tegnologia antigua", "tegnologia de punta")
print(articulo.split("."))

#SE HIZO USO DE MODIFICADORES DE CADENA DE TEXTO PARA PODER "EDITAR LAS PALABRAS"

NUMERO9

while True: #BOOLEAN
    codigo = input("Ingrese su codigo: ").strip().upper()
    if codigo.startswith("PRO"):
        print("Código válido")
    else:
        print("Código inválido")
