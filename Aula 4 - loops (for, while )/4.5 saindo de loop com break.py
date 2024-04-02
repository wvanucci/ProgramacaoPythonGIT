"""
Saindo de loops com break
Funciona da mesma forma que nas linguagens C e Jarvan

Utilizamos break para sair de loops de maneira forçada ou de maneira intencional
"""


# exemplo 1

for numero in range(1,11):
    if numero == 6:
        break
    else:
        print(numero)
print('Out')

# Exemplo 2

while True:
    comando = input('Digite "sair" para "sair": ').lower().strip() #strip() remove espaço se nao especificar nos parenteses
    if comando == 'sair':
        break

