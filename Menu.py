def Multiplicacion():
    total=1
    print("Ponga 0 para cuando quiera terminar")
    while True:
        numero=float(input("Numero:"))
        total*=numero
        if numero=="":
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
    contador2=1
    while(contador2<x+1):
      esprimo=True
      contador=2
      while (contador<contador2):
          if (contador2%contador==0):
              esprimo=False
          contador=contador+1
      if(esprimo):
          print (str(contador2)+" es primo")
      else:
          print( str(contador2)+ " no es primo")
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
    binario=input('ingrese el numero binario: ')
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
        11.-Deciaml-Binario
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




