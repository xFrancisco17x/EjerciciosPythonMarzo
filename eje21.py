A=["a","b","c","d","e","f"]
B=["c","e","g","h","i","j"]
ltodo=[]
lSolo1=[]
lSolo2=[]
lambas=[]


ltodo=A+B

for palabra in A:
    if palabra in B:
        lambas=lambas+[palabra]
    else:
        lSolo1=lSolo1+[palabra]
for palabra in B:
    if palabra not in A:
        lSolo2=lSolo2+[palabra]
print(A)
print(B)
print(ltodo)
print(lSolo1)
print(lSolo2)
print(lambas)
