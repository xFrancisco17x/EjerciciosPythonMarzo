a = 0
b = 5

print("La ecuacion es: "+str(a)+"x + "+str(b)+" = 0")

if a == 0 == b:
    r = "Todos los números son solución"
elif a == 0:
    r = "No existe solucion"    
else: 
    r = "La unica solución es: "+ str(-b/a)

print("La respuesta es: "+r)        