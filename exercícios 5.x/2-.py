a = []

cont = 0

a.append(input('Qual valor '))

for n in a:
    a.append(input('Qual valor: '))
    cont += 1
    if cont > 4:
        break
for i in range(0,len(a)):
    print(a[i])

print(a)


