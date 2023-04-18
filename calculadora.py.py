numero1=int(input("ingrese un numero: "))
numero2=int(input("ingrese el siguiente numero: "))
eleccion= 0
while eleccion :=6: 
    print("""
    Indique la operacion a realizar:
    1) Suma
    2) Resta
    3) Multiplicacion
    4) Division
    5) hacer otra operacion
    6) Salir
     """)
    eleccion=int(input( ))
    
    if eleccion== 1:
        print("resultado: ",numero1,"+",numero2,"=",numero1 + numero2 )
        
    if eleccion== 2:
        print("resultado: ",numero1,"-",numero2,"=",numero1 - numero2 )

    if eleccion== 3:
        print("resultado: ",numero1,"*",numero2,"=",numero1 * numero2 )

    if eleccion== 4:
        print("resultado: ",numero1,"/",numero2,"=",numero1 / numero2 )
        
    if eleccion== 5:
        numero1=int(input("ingrese un numero: "))
        numero2=int(input("ingrese el siguiente numero: "))
        
    if eleccion== 6:
        print("gracias por usar la calculadora creada por ")
