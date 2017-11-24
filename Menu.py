# esta Funcion nos dice si un numero es primo o no,
# si no lo es simplemente nos indica porque
# escribiendo los numeros por los que es divisuble l numero introducido

def Determinar_si_un_numero_es_primo():
    
    numero = (input("¿Qué numero quieres que analize? "))
    lista_permitida=["1","2","3","4","5","6","7","8","9","0"]
    comprobar=0
    while(comprobar<len(numero)):
        if(numero[comprobar] in lista_permitida):
            comprobar+=1
        else:
            comprobar=0
            print("")
            print("Valor invalido")
            numero = (input("¿Qué numero quieres que analize? "))
    numero=int(numero)
    valor = range(2, numero)
    contador = 0
    for n in valor:
        if (numero % n == 0):
            contador += 1
            print("Valor divisible entre:", n)
            # aqui es donde imprimen los valores con los que es divisible el numero que no es primo

    if (contador > 0):
        print("El numero numero no es primo")
    else:
        print("El numero numero es primo")


# esta funcion calcula el indice de masa corporal pidiendo al usuario
# su peso, y estatura para despues calcularlo, y tambien te muestra
# una tabla sobre los indices normalees, bajos y altos, para que compares
def IMC():
    # aqui se imprime la tabla
    print("-" * 150)
    print("Menor a 18" + (" -" * 10) + " Peso bajo. Necesario valorar signos de desnutrición")
    print("-" * 150)
    print("18 a 24.9" + (" -" * 10) + " Normal")
    print("-" * 150)
    print("25 a 26.9" + (" -" * 10) + " Sobrepeso")
    print("-" * 150)
    print("Mayor a 27" + (" -" * 10) + " Obesidad")
    print("-" * 150)
    print("27 a 29.9" + (
    " -" * 10) + " Obesidad grado I. Riesgo relativo alto para desarrollar enfermedades cardiovasculares")
    print("-" * 150)
    print("30 a 39.9" + (
    " -" * 10) + " Obesidad grado II. Riesgo relativo muy alto para el desarrollo de enfermedades cardiovasculares")
    print("-" * 150)
    print("Mayor a 40" + (
    " -" * 10) + " Obesidad grado III Extrema o Mórbida. Riesgo relativo extremadamente alto para el desarrollo de enfermedades cardiovasculares")
    print("-" * 150)
    # aqui te pide los valores
    x = (input("¿Cuanto pesas(Kg)?"))
    lista_permitidax=["1","2","3","4","5","6","7","8","9","0","."]
    comprobar=0
    while(comprobar<len(x)):
        if(x[comprobar] in lista_permitidax):
            comprobar+=1
        else:
            comprobar=0
            print("")
            print("Valor invalido")
            x = (input("¿Qué numero quieres que analize? "))
    x=float(x)

    y = (input("¿Cuanto mides(metros)?"))
    lista_permitiday=["1","2","3","4","5","6","7","8","9","0","."]
    comprobar=0
    while(comprobar<len(y)):
        if(y[comprobar] in lista_permitiday):
            comprobar+=1
        else:
            comprobar=0
            print("")
            print("Valor invalido")
            y = (input("¿Qué numero quieres que analize? "))
    y=float(y)
    # aqui se efectua el calculo y te arroja el resultado
    z = x / (y * y)
    print("Tu indice de masa corporal es " + str(z))


def Multiplicacion():
    total = 1
    print("Ponga 1 para cuando quiera terminar")
    while True:
        numero = (input("Numero:"))
        lista_permitiday=["1","2","3","4","5","6","7","8","9","0","."]
        comprobar=0
        while(comprobar<len(numero)):
            if(numero[comprobar] in lista_permitiday):
                comprobar+=1
            else:
                comprobar=0
                print("")
                print("Valor invalido")
                numero = (input("¿Qué numero quieres que analize? "))
        numero=float(numero)
        total *= numero

        if numero == 1:
            break
    print("El total es:", total)


def Modulo():
    x = (input("Escribe el numero que quieres dividir: "))
    lista_permitiday=["1","2","3","4","5","6","7","8","9","0","."]
    comprobar=0
    while(comprobar<len(x)):
        if(x[comprobar] in lista_permitiday):
            comprobar+=1
        else:
            comprobar=0
            print("")
            print("Valor invalido")
            x = (input("¿Escribe el numero que quiere dividir: "))
    x=float(x)

    y = (input("Escribe el numero por el que lo quieres dividir: "))
    lista_permitiday=["1","2","3","4","5","6","7","8","9","0","."]
    comprobar=0
    while(comprobar<len(y)):
        if(y[comprobar] in lista_permitiday):
            comprobar+=1
        else:
            comprobar=0
            print("")
            print("Valor invalido")
            y = (input("Escribi el numero por el que lo quieres dividir: "))
    y=float(y)

    if (y == 0):
        print("No se puede dividir entre 0")
    else:
        print("El resultado es: ")
        print(x / y)
        print("Su modulo es:")
        print(x % y)


def Potencia():
    print("Numero a elevar: ")
    a = (input())
    lista_permitiday=["1","2","3","4","5","6","7","8","9","0","."]
    comprobar=0
    while(comprobar<len(a)):
        if(a[comprobar] in lista_permitiday):
            comprobar+=1
        else:
            comprobar=0
            print("")
            print("Valor invalido")
            a = (input("Numero a elevar: "))
    a=float(a)

    print("Potencia:")
    b = (input())
    lista_permitiday=["1","2","3","4","5","6","7","8","9","0","."]
    comprobar=0
    while(comprobar<len(b)):
        if(b[comprobar] in lista_permitiday):
            comprobar+=1
        else:
            comprobar=0
            print("")
            print("Valor invalido")
            b = (input("potencia: "))
    b=float(b)

    resultado = a ** b
    print("El resultado es "+ resultado)


def Numeros_primos_en_un_rango_definido():
    x = (input("Introduzca hasta que numero quiere saber si los numeros son primos: "))
    while (x.isdigit() == False):
        print("Rango invalido, por favor introdusca un numero valido")
        x = input("Introduzca hasta que numero quiere saber si los numeros son primos: ")
    x = int(x)
    contador2 = 1
    print("Los numeros primos hatsa ese rango son:")
    while (contador2 < x + 1):
        esprimo = True
        contador = 2
        while (contador < contador2):
            if (contador2 % contador == 0):
                esprimo = False
            contador = contador + 1
        if (esprimo):
            print(str(contador2))
        contador2 = contador2 + 1


def Division():
    x = (input("Escribe el numero que quieres dividir: "))
    lista_permitiday=["1","2","3","4","5","6","7","8","9","0","."]
    comprobar=0
    while(comprobar<len(x)):
        if(x[comprobar] in lista_permitiday):
            comprobar+=1
        else:
            comprobar=0
            print("")
            print("Valor invalido")
            x = (input("Escribi el numero que quieres dividir: "))
    x=float(x)
    
    y = (input("Escribe el numero por el que lo quieres dividir "))
    lista_permitiday=["1","2","3","4","5","6","7","8","9","0","."]
    comprobar=0
    while(comprobar<len(y)):
        if(y[comprobar] in lista_permitiday):
            comprobar+=1
        else:
            comprobar=0
            print("")
            print("Valor invalido")
            y = (input("Escribe el numero por el que lo quieres dividir "))
    y=float(y)
    if (y == 0):
        print("No se puede dividir entre 0")
    else:
        print("El resultado es: ")
        print(x / y)


def Suma():
    total = 0.0
    print("Ponga 0 para cuando quiera terminar")
    while True:
        numero = (input("Numero:"))
        lista_permitiday=["1","2","3","4","5","6","7","8","9","0","."]
        comprobar=0
        while(comprobar<len(numero) or numero[comprobar]=="" ):
            if(numero[comprobar] in lista_permitiday):
                comprobar+=1
            elif(numero[comprobar]==""):
                comprobar=0
                print("")
                print("Valor invalido")
                numero = (input("¿Qué numero quieres que analize? "))
            else:
                comprobar=0
                print("")
                print("Valor invalido")
                numero = (input("¿Qué numero quieres que analize? "))
        numero=float(numero)
        total += numero
        if numero == 0:
            break
    print("El total es:", total)


def Raiz():
    print("Numero a sacar raiz: ")
    a = (input())
    lista_permitiday=["1","2","3","4","5","6","7","8","9","0","."]
    comprobar=0
    while(comprobar<len(a)):
        if(a[comprobar] in lista_permitiday):
            comprobar+=1
        else:
            comprobar=0
            print("")
            print("Valor invalido")
            a = (input("Numero a sacar raiz: "))
    a=float(a)

    b = (input("Raiz: "))
    lista_permitiday=["1","2","3","4","5","6","7","8","9","0","."]
    comprobar=0
    while(comprobar<len(b)):
        if(b[comprobar] in lista_permitiday):
            comprobar+=1
        else:
            comprobar=0
            print("")
            print("Valor invalido")
            b = (input("Raiz: "))
    b=float(b)

    if (b == 0):
        print("No existe la raiz 0")
    else:
        resultado = a ** (1 / b)
        print(resultado)


def Binario_Decimal():
    binario = input('Ingrese el numero binario: ')
    numero = []
    comprobar = []
    aceptable = ["1", "0"]
    contador = 0
    contadoracep = 0
    decimal = 0
    decimalizador = 0
    listones = False
    contar = 0
    while (contadoracep < len(binario)):
        comprobar.append(binario[contadoracep])
        contadoracep = contadoracep + 1
    while (listones == False):
        while (contar < len(comprobar)):
            if (comprobar[contar] in aceptable):
                contar += 1
            else:
                contadoracep = 0
                contar = 0
                comprobar = []
                print("")
                print('Solo se admite "1" y "0"')
                binario = input('Ingrese el numero binario: ')
                while (contadoracep < len(binario)):
                    comprobar.append(binario[contadoracep])
                    contadoracep = contadoracep + 1
        listones = True

    print("")
    while (contador < len(binario)):
        numero.append(int(binario[contador]))
        contador = contador + 1
    while (decimalizador < len(binario)):
        decimal = decimal * 2
        if (numero[decimalizador] == 1):
            decimal = decimal + 1
        decimalizador = decimalizador + 1

    print("Su decimal es:", decimal)


def Decimal_Binario():
    lista_permitida=["1","2","3","4","5","6","7","8","9","0",]
    decimal=(input("Ingreese el numero decimal:"))
    resultado=""
    comprobar=0
    while(comprobar<len(decimal)):
        if(decimal[comprobar] in lista_permitida):
            comprobar+=1
        else:
            print("")
            print("Valor invalido")
            decimal=(input("Ingreese el numero decimal:"))
            comprobar=0 
    decimal=int(decimal)
    while ((decimal // 2) != 0):
      resultado=str(decimal%2)+resultado
      decimal=decimal//2
    binario=(str(decimal)+resultado)
    print("El numero en binario es: "+ binario)


def Hexadecimal_Decimal():

    A=10
    B=11
    C=12
    D=13
    E=14
    F=15
    lista_permitida=["1","2","3","4","5","6","7","8","9","0","A","B","C","E","F"]
    lista_letras=["A","B","C","D","E","F"]
    lista_hexa=[]
    completo=False
    suma=0
    hexadecimiliador=16
    sumador=0
    comprobar=0
    hexa=input("Ingrese el numero hexadecimal: ").upper()
    contador=int(len(hexa))-1
    while(contador>=0):
        lista_hexa.append(hexa[contador])
        contador-=1
    
    while(comprobar<len(lista_hexa)):
        if(lista_hexa[comprobar] in lista_permitida):
            comprobar+=1
        else:
            lista_hexa=[]
            contador=0
            comprobar=0
            print ("")
            print ("Ingrese in valor valido")
            hexa=input("Ingrese el numero hexadecimal: ").upper()
            contador=int(len(hexa))-1
            while(contador>=0):
                lista_hexa.append(hexa[contador])
                contador-=1
    
    
    while (sumador<len(lista_hexa)):
        if(lista_hexa[sumador] in lista_letras):
            if(lista_hexa[sumador] =="A"):
                suma+=(A*(hexadecimiliador**sumador))
            if(lista_hexa[sumador] =="B"):
                suma+=(B*(hexadecimiliador**sumador))
            if(lista_hexa[sumador] =="C"):
                suma+=(C*(hexadecimiliador**sumador))
            if(lista_hexa[sumador] =="D"):
                suma+=(D*(hexadecimiliador**sumador))
            if(lista_hexa[sumador] =="E"):
                suma+=(E*(hexadecimiliador**sumador))
            if(lista_hexa[sumador] =="F"):
                suma+=(F*(hexadecimiliador**sumador))
        else:
            suma+=(int(lista_hexa[sumador])*(hexadecimiliador**sumador))
        sumador+=1
    print("")
    print("")
    print ("El equivalente en decimal es: "+str(suma))


def Binario_Hexadecimal():
    binario = input('ingrese su valor binario para que sea convertido a hexadecimal: ' )
    lista_permitiday=["1","0"]
    comprobar=0
    while(comprobar<len(binario)):
        if(binario[comprobar] in lista_permitiday):
            comprobar+=1
        else:
            comprobar=0
            print("")
            print("Valor invalido")
            binario = input('ingrese su valor binario para que sea convertido a hexadecimal: ')
    
    hexadecimal = hex(int(binario, 2))
    print(hexadecimal)

def Decimal_Hexadecimal():
    lista_permitida=["1","2","3","4","5","6","7","8","9","0",]
    decimal=(input("Ingreese el numero decimal:"))
    resultado=""
    comprobar=0
    while(comprobar<len(decimal)):
        if(decimal[comprobar] in lista_permitida):
            comprobar+=1
        else:
            print("")
            print("Valor invalido")
            decimal=(input("Ingreese el numero decimal:"))
            comprobar=0 
    decimal=int(decimal)
    while ((decimal // 2) != 0):
      resultado=str(decimal%2)+resultado
      decimal=decimal//2
    binario=(str(decimal)+resultado)
    hexadecimal=hex(int(binario,2))
    print(hexadecimal)

def Hexadecimal_Binario():
    A=10
    B=11
    C=12
    D=13
    E=14
    F=15
    lista_permitida=["1","2","3","4","5","6","7","8","9","0","A","B","C","E","F"]
    lista_letras=["A","B","C","D","E","F"]
    lista_hexa=[]
    completo=False
    suma=0
    hexadecimiliador=16
    sumador=0
    comprobar=0
    hexa=input("Ingrese el numero hexadecimal: ").upper()
    contador=int(len(hexa))-1
    while(contador>=0):
        lista_hexa.append(hexa[contador])
        contador-=1
    
    while(comprobar<len(lista_hexa)):
        if(lista_hexa[comprobar] in lista_permitida):
            comprobar+=1
        else:
            lista_hexa=[]
            contador=0
            comprobar=0
            hexa=input("Ingrese el numero hexadecimal: ").upper()
            contador=int(len(hexa))-1
            while(contador>=0):
                lista_hexa.append(hexa[contador])
                contador-=1
    
    
    while (sumador<len(lista_hexa)):
        if(lista_hexa[sumador] in lista_letras):
            if(lista_hexa[sumador] =="A"):
                suma+=(A*(hexadecimiliador**sumador))
            if(lista_hexa[sumador] =="B"):
                suma+=(B*(hexadecimiliador**sumador))
            if(lista_hexa[sumador] =="C"):
                suma+=(C*(hexadecimiliador**sumador))
            if(lista_hexa[sumador] =="D"):
                suma+=(D*(hexadecimiliador**sumador))
            if(lista_hexa[sumador] =="E"):
                suma+=(E*(hexadecimiliador**sumador))
            if(lista_hexa[sumador] =="F"):
                suma+=(F*(hexadecimiliador**sumador))
        else:
            suma+=(int(lista_hexa[sumador])*(hexadecimiliador**sumador))
        sumador+=1
        
    decimal=suma
    resultado=""
    while ((decimal // 2) != 0):
      resultado=str(decimal%2)+resultado
      decimal=decimal//2
    print("")
    print("")
    print ("El numero en binario equivalente es: ")+(str(decimal)+resultado)


import time

def Menu():
    #son lo unicos valores permitido en esta funcion
    aceptable=["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"]
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
        ans = (input("Que te gustaria hacer:"))
       
        #revisa si el input es aceptable en la lista de los valores que se usan en la funcion
        if (ans in aceptable):
            ans=int(ans)
            if ans == 1:
                Suma()
            elif ans == 2:
                Multiplicacion()
            elif ans == 3:
                Division()
            elif ans == 4:
                Modulo()
            elif ans == 5:
                Potencia()
            elif ans == 6:
                Raiz()
            elif ans == 7:
                Binario_Hexadecimal()
            elif ans == 8:
                Hexadecimal_Binario()
            elif ans == 9:
                Decimal_Hexadecimal()
            elif ans == 10:
                Hexadecimal_Decimal()
            elif ans == 11:
                Decimal_Binario()
            elif ans == 12:
                Binario_Decimal()
            elif ans == 13:
                Numeros_primos_en_un_rango_definido()
            elif ans == 14:
                Determinar_si_un_numero_es_primo()
            elif ans == 15:
                IMC()
            elif ans == 16:
                print("salir gracias men")
                break
            time.sleep(3)
        elif(not ans in aceptable):
            print ("Ingreso un valor no valido")
            continue
        
            time.sleep(2)

                       
Menu()
