"""
Utilizando Lambdas
Conhecidas por Expressões Lambdas, ou simplesmente Lambdas, são funções sem nome, ou seja, funções anônimas.

# Função em python
def soma(parâmetro):
    processo
-----------------------------

def funcao(x):
    return 3 * x + 1


print(funcao(4))

print()

# Expressão Lambda
lambda x: 3 * x + 1  # mesma funcao definida a cima (lembrando que lambda é reservada)

# Como utilizar? temos que atribuir uma variável para funcao lambada (forma rústica/feia)
cal = lambda x: 3 * x + 1

print(cal(4))

#sintaxe
lambda entrada: retorno/processo
"""

# Podemos ter expressões lambdas com múltiplas entradas

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()
# remove espaço inicio e fim (strip) e começa com letra maiuscula cada str

print(nome_completo('angelina', 'jOlIe'))
print(nome_completo('Felicity', ' Jones'))
