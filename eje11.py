año1 = int (input ("Ingrese el año de inicio: "))
año2 = int (input ("Ingrese el año de final: "))
r = "Los años bisiestos entre "+str(año1)+" y "+str(año2)+" son: " 

for i in range(año1,año2):
    if(i%4==0 and i%100!=0) or (i%400==0):
       r = r + str(i)+","
print(r)        