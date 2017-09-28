def potencia():
    print("Numero a elevar:")
    a=float(input())
    print("Potencia:")
    b=float(input())
    resultado=a**b
    print(resultado)

def raiz():
    print("Numero a sacar raiz")
    a=float(input())
    print("Raiz")
    b=float(input())
    resultado=a**(1/b)
    print(resultado)
    
def Menu():
    ans = True
    while ans:
        print("""
        1.-Suma
        2.-Multiplicaccion
        3.-Division
        4.-Modullo
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

        ans=int(input("Que te gustaria hacer"))
       
        if ans==1:
           suma()
        elif ans==2:
            multiplicacion()
        elif ans==3:
           division()
        elif ans==4:
            Modullo()
        elif ans==5:
            Potencia()
        elif ans==6:
            Raiz()
        elif ans==7:
            Binario-Hexadecimal()
        elif ans==8:
            Hexadecimal-Binario()
        elif ans==9:
            Decimal-Hexadecimal()
        elif ans==10:
            Hexadecimal-Decimal()
        elif ans==11:
            Deciaml-Binario()
        elif ans==12:
            Binario-Decimal()
        elif ans==13:
            Numeros primos en un rango definido()
        elif ans==14:
            Determinar si un numero es primo()
        elif ans==15:
            IMC()
        elif ans==16:
            print("salir gracias men")


         
            


Menu()




