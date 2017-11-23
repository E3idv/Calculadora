#esta Funcion nos dice si un numero es primo o no, 
#si no lo es simplemente nos indica porque 
#escribiendo los numeros por los que es divisuble l numero introducido

def Determinar_si_un_numero_es_primo():
  numero= int(input("¿Qué numero quieres que analize? "))
  valor= range(2,numero)
  contador = 0
  for n in valor:
      if (numero %n==0):
         contador +=1
         print("divisor:", n) 
         #aqui es donde imprimen los valores con los que es divisible el numero que no es primo


  if(contador > 0 ):
     print("El numero numero no es primo")
  else:
      print("El numero numero es primo")
      
#esta funcion calcula el indice de masa corporal pidiendo al usuario
#su peso, y estatura para despues calcularlo, y tambien te muestra 
#una tabla sobre los indices normalees, bajos y altos, para que compares 
def IMC():
  #aqui se imprime la tabla
  print("-"*85)
  print("Menor a 18"+(" -"*10)+ " Peso bajo. Necesario valorar signos de desnutrición")
  print("-"*85)
  print("18 a 24.9"+(" -"*10)+ " Normal")
  print("-"*85)
  print("25 a 26.9"+(" -"*10)+ " Sobrepeso")
  print("-"*85)
  print("Mayor a 27"+(" -"*10)+ " Obesidad")
  print("-"*85)
  print("27 a 29.9"+(" -"*10)+ " Obesidad grado I. Riesgo relativo alto para desarrollar enfermedades cardiovasculares")
  print("-"*85)
  print("30 a 39.9"+(" -"*10)+ " Obesidad grado II. Riesgo relativo muy alto para el desarrollo de enfermedades cardiovasculares")
  print("-"*85)
  print("Mayor a 40"+(" -"*10)+ " Obesidad grado III Extrema o Mórbida. Riesgo relativo extremadamente alto para el desarrollo de enfermedades cardiovasculares")
  print("-"*85)
  #aqui te pide los valores
  x=float(input("¿Cuanto pesas(Kg)?"))
  y=float(input("¿Cuanto mides(metros)?"))
  #aqui se efectua el calculo y te arroja el resultado
  z=x/(y*y)
  print("Tu indice de masa corporal es "+str(z))
      
def Multiplicacion():
    total=1.0
    print("Ponga 1 para cuando quiera terminar")
    while True:
        numero=float(input("Numero:"))
        total*=numero
        if numero== 1:
          break
    print("El total es:",total)
    
def Modulo():
    x = float (input("Escribe el numero que quieres dividir: "))
    y = float (input("Escribe el numero por el que quieres dividir "))
    
    if (y==0):
      print("No se puede dividir entre 0")
    else:
      print ("El resultado es: ")
      print (x/y)
      print ("Su modulo es:")
      print(x%y)

    
def Potencia():
    print("Numero a elevar:")
    a=float(input())
    print("Potencia:")
    b=float(input())
    resultado=a**b
    print(resultado)
    
def Numeros_primos_en_un_rango_definido():
    x=int(input("Introduzca hasta que numero quiere saber si los numeros son primos: "))
    while (x.isdigit() ==False):
        print ("Rango invalido, por favor introdusca un numero valido")
        x=input("Introduzca hasta que numero quiere saber si los numeros son primos: ")
    x=int(x)
    contador2=1
    print ("Los numeros primos hatsa ese rango son:")
    while(contador2<x+1):
      esprimo=True
      contador=2
      while (contador<contador2):
          if (contador2%contador==0):
              esprimo=False
          contador=contador+1
      if(esprimo):
          print (str(contador2))
      contador2=contador2 + 1
    
def Division ():
    x = float (input("Escribe el numero que quieres dividir: "))
    y = float (input("Escribe el numero por el que quieres dividir "))
    
    if (y==0):
      print("No se puede dividir entre 0")
    else:
      print ("El resultado es: ")
      print (x/y)
    
def Suma():
    total=0.0
    print("Ponga 0 para cuando quiera terminar")
    while True:
        numero=float(input("Numero:"))
        total+=numero
        if numero==0:
            break
    print("El total es:",total)
    

def Raiz():
    print("Numero a sacar raiz")
    a=float(input())
    print("Raiz")
    b=float(input())
    if (b==0):
      print("No existe la raiz 0")
    else:
      resultado=a**(1/b)
      print(resultado)
  
def Binario_Decimal():
    binario=input('Ingrese el numero binario: ')
    numero=[]
    contador=0
    decimal=0
    decimalizador=0
    while (contador < len(binario)):
        numero.append(int(binario[contador]))
        contador=contador+1
    while (decimalizador<len(binario)):
        decimal=decimal*2
        if (numero[decimalizador]==1):
            decimal=decimal+1
        decimalizador=decimalizador+1

    print ("Su decimal es:", decimal)
    
def Decimal_Binario():
  decimal=int(input("Ingreese el numero decimal:"))
  resultado=""
  while ((decimal // 2) != 0):
    resultado=str(decimal%2)+resultado
    decimal=decimal//2
  print ("El numero en binario equivalente es: ")+(str(decimal)+resultado)

def Hexadecimal_Decimal():
    while True:
        print("introdzca 'x'.")
        hexdec = input("introduzca numero en hexadecimal")
        if hexdec =='x':
            break
        else:
            dec = int(hexdec,16)
            print(hexdec,"en decimal = ",str(dec),"\n")        
  
def Binario_Hexadecimal():
  print('ingrese su valor binario para que sea convertido a hexadecimal')
  binario=input(str)
  hexadecimal=hex(int(binario,2))
  print(hexadecimal)

def Menu():
    ans = True
    while ans:
        print("""
        1.-Suma
        2.-Multiplicaccion
        3.-Division
        4.-Modulo
        5.-Potencia
        6.-Raiz
        7.-Binario-Hexadecimal
        8.-Hexadecimal-Binario
        9.-Decimal-Hexadecimal
        10.-Hexadecimal-Decimal
        11.-Decimal-Binario
        12.-Binario-Decimal
        13.-Numeros primos en un rango definido
        14.-Determinar si un numero es primo
        15.-IMC
        16.-Salir y acabar de sufrir
        """)

        ans=int(input("Que te gustaria hacer:"))
       
        if ans==1:
           Suma()
        elif ans==2:
            Multiplicacion()
        elif ans==3:
           Division()
        elif ans==4:
            Modulo()
        elif ans==5:
            Potencia()
        elif ans==6:
            Raiz()
        elif ans==7:
            Binario_Hexadecimal()
        elif ans==8:
            Hexadecimal_Binario()
        elif ans==9:
            Decimal_Hexadecimal()
        elif ans==10:
            Hexadecimal_Decimal()
        elif ans==11:
            Decimal_Binario()
        elif ans==12:
            Binario_Decimal()
        elif ans==13:
            Numeros_primos_en_un_rango_definido()
        elif ans==14:
            Determinar_si_un_numero_es_primo()
        elif ans==15:
            IMC()
        elif ans==16:
            print("salir gracias men")


         
            


Menu()





