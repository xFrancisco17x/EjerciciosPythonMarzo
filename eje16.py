from random import randint

def ppt(op):
    if op==1:
        r="piedra"
    elif op ==2:
        r="papel"
    elif op==3:
        r="tijera"
              
    return r  

ganadas = 0
while ganadas <3:
    opUusuario = int(input("Ingrese opcion:\n1.-Piedra\n2.-Papel\n3.-Tijera"))
    if opUusuario>3 or opUusuario<1:
        print("Ingrese una opcion valida")
        continue
    opMaquina = randint(1,3)
    print("La maquina eligio: ",ppt(opMaquina))
    print("El usuario eligio: ",ppt(opUusuario))
    if (opUusuario==1 and opMaquina==3) or (opUusuario==2 and opMaquina==1)or(opUusuario==3 and opMaquina==2):
        print("Gana el usuario")
        ganadas+=1
    elif opUusuario==opMaquina:
        print("Es un empate")
    else: 
        print("Gana la maquina")
    print ("Ganadas: ",ganadas)        
