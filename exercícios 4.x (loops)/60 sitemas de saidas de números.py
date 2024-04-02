
l=[]
paresL = []
while True:
    num = float(input('Digite um número (pressione 0 para sair): '))
    if num == 0:
        break
    l.append(num)

for i in l:
    if i%2 == 0:
        paresL.append(i)

print(l)
print('soma dos nº ',sum(l))
print(f'qunatidade de nºs digitados é {len(l)}')
print(f'média dos números digitados é {sum(l)/len(l)}')
print(f'o maior nº é {max(l)}')
print(f'O menor nº é {min(l)}')
print(paresL,len(paresL))
print(f'A média dos pares é {sum(paresL)/len(paresL)}')





