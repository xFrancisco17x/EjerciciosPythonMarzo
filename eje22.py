from random import randint
def llenarSec(n):
    lista=[]
    for i in range(1,n+1):
        lista+=[i]
    return lista

def llenarAle(n):
    lista=[]
    num=randint(1,n)
    lista+=[num]
    for i in range(n-1):
        while num in lista:
            num=randint(1,n)
        lista+=[num]
    return lista



A=llenarSec(10)
B=llenarAle(10)
print(A)
print(B) 

for i in range(len(A)):
    print("La persona:", A[i]," es pareja con",B[i])
    