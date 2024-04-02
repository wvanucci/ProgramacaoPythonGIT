# somar os valores pares da sequencia do fibonacci

t1, soma=0,0
t2 = 1
cont = 1

# n = int(input('Até qual nº: '))
# print(f'{t1} {t2}', end= ' ')
while True:
    t3 = t1 + t2
    if t3 > 4_000_000:
        break
    t1=t2
    t2=t3
    if t3%2 ==0:
        soma += t3

print(soma)