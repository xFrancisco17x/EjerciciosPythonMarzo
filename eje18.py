from random import randint

aciertos=0
v=True

while v:
    op=randint(1,2)
    num1=randint(1,10)
    num2=randint(1,10)
    if op==1:
        res=num1*num2
        print(num1," * ",num2, "=")
        resUsario=int(input("Ingrese su respuesta"))
        if resUsario==res:
            print ("Correcto")
            aciertos+=1
        else:
            print("Incorrecto")
            v=False
    elif op==2:
        res=num1//num2
        print(num1," / ",num2, "=")
        resUsario=int(input("Ingrese su respuesta"))
        if resUsario==res:
            print ("Correcto")
            aciertos+=1
        else:
            print("Incorrecto")
            v=False
print("Su total de aciertos es: ",aciertos) 