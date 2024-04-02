"""
Entendo *args
- O *args é um parametro, como outro qualquer. Isso significa que você poderá chamar de qualquer coisa, desde que comece
com asterisco

Exemplo:
*xis

Mas por convenção, utilizamos *args para definí-lo

Mas o que é *args?
    O parãmetro *args utilizado em uma função, coloca os valores extras informados como entrada em uma tupla. Lemre
    que dupla são imutáveis
#exemplo

def soma_todos_numeros(n1,n2,n3):
    return n1+n2+n3

print(soma_todos_numeros(1,2,3))

#print(soma_todos_numeros(1,4)) #TypeError/ como solucionar? colocar valor padrão nos parâmetros( aulas passadas)

print(soma_todos_numeros(1,3,5,6)) #TypeError
"""


# Entendendo o args exemplo 1

def soma_todos_numeros(*args):  # para declarrar usar *
    print(args)  # para utilizar apenas args


soma_todos_numeros()
soma_todos_numeros(1, 2, 3, 4)
soma_todos_numeros(2, 3, 5, 1)
soma_todos_numeros(1, 3, 45, 6, 6)  # vai gerar tuplas dos valores de entrada

print()


# Exemplo 2. Pensando como utilizar args para não precisar escrever muito parâmetro na função

def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total


print(soma())
print(soma(1, 2, 4, 5))
print(soma(1, 2, 40, 5))
print(soma(1, 2, 40, 50, 5))
""" Parace mais interessante para reduzir a função
- Para cálculo acredito que tem que dominar while e for (loopings)
"""

# Exemplo 3

print('\n exemplo 3\n')


def min_max_sum(
        *args):  # como args estão em tupla eu posso usar funções built-in (ou outras criadas) para fazer o que preciso
    x = input('Quer lista do args (L) ou min, max e soma dos valores da tupla de args(MMS)? ').upper().strip()
    if x == 'L':
        return list(args)  # pegar os dados de args e transformar em lista
    elif x == 'MMS':
        return [min(args), max(args), sum(args)]  # retornando em uma lista (posso retornar em tupla tbm)
    else:
        return 'entrada inválida'


print(min_max_sum(1, 2, 3))

#importante args é tupla, são imuteveis; seria interessante colocar para lista; lembrando que os metodos de sum é para int e flaot né