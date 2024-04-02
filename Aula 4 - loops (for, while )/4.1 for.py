""" Loop for
LOOP é uma estrututra de repetição
e for é uma desssas estruturas

C ou Java
    for(in i = 0; i<10; i++){
        //execução do loop
}

Python

    for intem in intereável:
        //execução do loop

Utilizamos loops para iterar sobre sequencias ou sobre valores iteráveis

INTERADOR: um iterador se refere tanto ao objeto que permite ao programador percorrer um container(uma coleção de elementos)
particularmente listas, quanto ao padrão de projetos Iterator, no qual um iterador é usado para percorrer
um container e acessar seus elementos
Exemplo de interáveis:
- str
    nome = 'João'
- lista
    lista = [1,2,3]
- range
    numeros = range(1,16)
"""

nome = "João"
lista = [1,3,5,7,9]
numeros = range(1,10) # temos que transformar em uma lista/ range vai de 1-9

# exemplo de for 1 (interando sobre str)
for letra in nome:
    print(letra)
print()

# exemplo 2 (interando sobre lista)
for i in lista:
    print(i)
print()

# exemplo 3 (interando sobre range)
for i in numeros:
    print(i)
"""
Enumerate:
usar help(enumerate)
retorna um objeto de interavel. 

Para o exemplo nome:
((0,'J'),(1,'o'),(2,'ã'),(3,'o'))
print()

for numero,letra in enumerate(nome):
    print(letra)   #imprimindo nome[0], nome [1]...
    
OBS: quando não precisamos de um valor pode descartá - lo utilizando _ . Por exemplo:

for _,letra in enumerate(nome):
    print(letra)   #imprimindo nome[0], nome [1]..
"""
print()
print('exemplo enumerate')
for valor in enumerate(nome):    # vai retornar a tupla inteira
    print(valor)

print()

# imprimindo só em uma linha no for
for letra in nome:
    print(letra, end='')


