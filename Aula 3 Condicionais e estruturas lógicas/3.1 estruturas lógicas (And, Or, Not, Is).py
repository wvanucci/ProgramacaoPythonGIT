"""Estruturas lógicas and(e), or(ou), not(não), is(é)

operadores unários (dependem apenas de um valor):
    - not,
oepradores binários (depende de dois valores):
    - and, or, is

Regras de funcionamento:

Para o 'and', ambos os valores precisam ser True
Para o 'or' um ou outro precisa ser True
Para o 'is', o valor é comparado com um segundo
"""

"""
ativo = False
logado = True

if ativo and logado:
    print('Bem-Vindo')
else:
    print('Você precisa ativar sua conta. Verifique seu email')

"""

"""
# checando is

ativo = False
logado = False

if ativo is False:
    print('checar email')
else:
    print('Bem Vindo \'~nome do usuario~\'')

# not False -> True
# not True -> False
"""

"""
#checando not
ativo = True
logado = False

if ativo not True:
    print('checar email')
else:
    print('Bem Vindo \'~nome do usuario~\'')
"""

# OBS: essa foi a aula mais confunsa e largada do curso, foi tipo um se vira
# se usar dir(váriavel ou dado) é possivel notar podemos obter alguns métodos is para essa váriavel. Exemplo:

nome = 'você'
print(dir(nome))  #conferindo os is
print(nome.istitle())  #retorna bool
print(nome.title().istitle())  #retorna bool
print(nome.islower())  #retorna bool

# Dica: Se usar o terminal (no pycharm, prompt comando termina linux) não é necessario o print para retornar

