
l =[]
cont = 0
x= int(input('Qual a posição X: '))
y= int(input('Qual a posição Y: '))
l.append(float(input(f'{cont+1}º valor: ')))

for n in l:
    l.append(float(input(f'{cont+2}º valor: ')))
    cont+=+1
    if cont > 6:
        break

s= l[x]+l[y]
print(f' a lista é {l} e a soma de {l[x]}+{l[y]} = {s}')