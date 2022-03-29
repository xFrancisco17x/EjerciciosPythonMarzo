from random import randint, randrange, uniform
#randit(x,y)--->numero leatorio entre "x" y "y"
#random()--->numero aleatorio entre 0 y 1
#randrange(x,y,p)--->numero leatorio entre "x" y "y" con un paso de "p"
#uniform(x,y)--->numero aleatorio de tipo float entre "x" y "y"

zonaUsuario = int(input("¿En que zona deseas disparar?"))
zonaPortero = randint(1,6)

print("El portero ha cubierto la zona: ",zonaPortero)

if zonaUsuario == zonaPortero:
    print("No ha sido gol")
else:
    print("GOOOOOOL :D")
