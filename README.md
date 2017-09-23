# Calculadora
  #Numeros primos
  x=int(raw_input("Introdusca hasta que numero quiere saber si los numeros son primos: "))
  contador2=2
  while(contador2<x+1):
      esprimo=True
      contador=2
      while (contador<contador2):
          if (contador2%contador==0):
              esprimo=False
          contador=contador+1
      if(esprimo):
          print str(contador2)+" es primo"
      else:
          print str(contador2)+ " no es primo"
      contador2=contador2 + 1 
