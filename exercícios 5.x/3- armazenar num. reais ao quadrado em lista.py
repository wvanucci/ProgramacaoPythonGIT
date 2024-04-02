import math
l =[]
lf=[]
cont = 0
l.append(int(input('Qual o primeiro valor: ')))
for n in l:
    l.append(float(input('Qual valor: ')))
    cont += 1
    if cont > 8:
        break
print(l)
for i in l:
    a= pow(i,2)
    lf.append(a)

print(l, lf)


