""" min() max() mínimo e máximo valor funao built-in"""

nomes = ['Arya', ' kalsdka', 'asdasd', 'jkhgjhj']
print(max(nomes, key = lambda nome: len(nome)))
print(min(nomes, key = lambda nome: len(nome)))

# em dicionario
print()

musicas = [
    {'título': 'THunder', 'tocou': 3},
    {'título': 'Psiu', 'tocou': 13},
    {'título': 'Get wawya', 'tocou': 33},
    {'título': 'Physical', 'tocou': 1231}

]

print(max(musicas, key=lambda x: x['tocou'])) # a fu nção lambda:valor x da chave tocou
print(min(musicas, key=lambda x: x['tocou'])) #valor x da chave tocou

#Desafio!
maior = max(musicas, key=lambda x: x['tocou'])
print(maior['título'])