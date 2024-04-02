l = []
cont = 0

while cont >= 0:
    valor = float(input('Digite um número: '))
    l.append(valor)
    l.sort()
    continuar = input('Deseja continuar [S/N]? ').upper().strip()
    if continuar == 'N':
        break
# verificar
# print(l)
# print(len(l))
# print(len(l)-1)
for i in l:
    if i == l[len(l) - 1]:
        cont += 1
print(f'O maior valor é {l[len(l)-1]} e foi lido {cont} vezes')


