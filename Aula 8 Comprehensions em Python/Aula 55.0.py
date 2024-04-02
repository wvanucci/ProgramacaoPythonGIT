"""
Lista aninhadas
-Algumas linguagens de programação (C/Javaa/PHP) possum um estrutura de dados chamadas de arrays:
    - Unidimensionais (Arrays/vetores);
    -Multidimensionais (Matrizes)
-No python não existe arrays, existem as listas

n = [1,2,3,4,5]  <---- LISTA em python ( é mais potencial em python pq podemos ter variaos tipos de dados e ilimitados)

"""

# exemplos

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # matriz 3x3
print(listas)
print(type(listas))

# Como fazemos para acessar os daods?

print(listas[0][2])  # linha 0 coluna 3 elemento 3
print(listas[2][1])  # 8

print()
# Interando com loops

for list in listas:
    for num in list:
        print(num)

print()

# com List comprehension
[[print(valor) for valor in list] for list in listas]

print()

# GErando um tabuleiro/matriz 3x3
    #NOTA: sintaxe [[Faça isso] para cada elemendo da lista( usa for)] esse ISSO é gerar outra lista
matriz = [[num for num in range(1, 4)] for valor in range(1, 4)]
print(matriz)

# gerando jogadas para jogo da velha
    #posso colocar condição
velha = [['X' if numero % 2 == 0 else '0' for numero in range(1, 4)] for valor in range(1,4)]
print(velha)

