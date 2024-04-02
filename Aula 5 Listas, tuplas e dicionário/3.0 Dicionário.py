"""
Dicionários

OBS: Em algumas linguagens de programação, os dicionários Python são conhecidos por mapas

Dicionário são coleções de tipe chave/valor.
Dicionários são representadas por {}

print(type{}) -> retorna tipo dict

OBS: SObre  dicionários
    Chave e valor são separados por dois pontos 'chave:valor';
    Tanto chave quanto valor podem ser de qualquer tipo de dado;
    Podemos misturar tipos de dados;

paises ={'br':'Brasil','eua':'Estados Unidos'}

print(paises)
print(type(paises))

#outra forma

paises2 = dict(br='brasil',eua='Estados unidos')
print(paises2)
print(type(paises2))
"""

# Acessando elementos
paises ={'br':'Brasil','eua':'Estados Unidos'}


    # forma 1. Acessando via chave:
print(' Forma 1')
print(paises['br']) # é acessado o valor via chave por []

    #forma2. Acessando via get (recomendado):
print('\n Forma 2:')
print(paises.get('br'))
print(paises.get('ru'))  #não tem ru no dict portanto vai retornar none (somente se usando gue o tipo None é False)

    # verficiando objetos:

print('\n  Verificando se chave se enconta no dict:')
print('br' in paises)
print('ru' in paises)
print('Brasil' in paises)

    #Exemplo de utiliade:
print('\n Exemplo de utilidade if/else:')
if 'ru' in paises:
    russia = paises['ru']
else:
    print('Não tem essa chave no dict')

