# A diferença entre map() e filter() é:

#   map() recebe dois parâmetros, uma função e dois iteráveis, e retorna um objeto mapeando a função para cada elemento
# do iterável
#   filter() recebe dois parâmetros, uma função e um iterável, e retorna um objeto filtrando apenas os
# elementos de acordo com a função
#   GRANDE diferença: filter retorna valores bool e map retorna qualquer tipo de dados

# exemplo 'complexo'

usuarios = [
    {'usuarios': 'samuel', 'tweets': ['Eu adoro bolos', 'Adoro pizza']},
    {'usuarios': 'carla', 'tweets': ['Eu adoro gatos']},
    {'usuarios': 'bob', 'tweets': []},
    {'usuarios': 'sdogo', 'tweets': []},
    {'usuarios': 'gal', 'tweets': ['Eu adoro bolos', 'Adoro cachorro']},
    {'usuarios': 'lzinho', 'tweets': []}
]
print(usuarios)  # lista de chaves
# Tarefa: filtrar os usuários que estão inativos no Twitter

inativos = list(filter(lambda u: len(u['tweets']) == 0, usuarios))
# da lista do usuario vou acessar os valores da chave tweets verificando o tamanho da str; usei o filter para
# filtrar esses dados
print(inativos)
print(f'Usuarios inativos: {len(inativos)}')

# forma 2
print()
inativos = list(filter(lambda u: not u['tweets'], usuarios))  # verificar os valores do tweets. a lista vazia é false
# not False -> True. Logo vai retornar os True,k que são as listas vazias (sem tweets)
print(inativos)
