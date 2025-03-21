def edad():
   edad = int(input ("que edad tiene: "))
   if edad <0:
      print("edad no valida,ingrese nuevamente su edad...")
   breakpoint
   if edad <12:
     print ("usted es un niño.Sigue explorando y aprendiendo")
   elif edad >=13 and edad <=17:
      print ("usted es un adolescente.Estas en la mejor etapa de tu vida,se tu mismo")
   elif edad >=18 and edad <=64:
      print("usted es un adulto.Disfruta cada momento de la vida")
   elif edad >=65:
      print ("usted es un adulto mayor.Comparte tu sabiduría con los jovenes")
edad()