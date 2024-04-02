"""
Exemplos 'complexos'
"""

usuarios = [
    {'usuario': 'samuel', 'tweets': ['Eu adoro bolos', 'Adoro pizza']},
    {'usuario': 'carla', 'tweets': ['Eu adoro gatos']},
    {'usuario': 'bob', 'tweets': [], 'cor': 'Amarelo'},
    {'usuario': 'sdogo', 'tweets': []},
    {'usuario': 'gal', 'tweets': ['Eu adoro bolos', 'Adoro cachorro']},
    {'usuario': 'lzinho', 'tweets': []}
]

print(usuarios)

print(sorted(usuarios, key=lambda usuario: usuario['usuario'])) # ordenar pelo valor da chave usuario (ordem alfabética)