"""" TIpo booleano
Algebra Booleana, criada por George Boole
2 constantes = verdadeiro ou falso
no python é True e False (sempre com a inicial maiuscula)
"""

ativo = True
naoAtivo = False

print(ativo)

""" OPERAÇÕES BÁSICAS:"""

# Neggação (not):
""" 
Fazendo a negação, se o valor for verdadeiro oresultado será falso
se for falso o resultado será verdadeiro. Ou seja, sempre o contrário
"""

print(not ativo)
print(not naoAtivo)

# Ou (or):
"""
É uma operação binária, ou seja, depende de dois valores. Ou um ou outro deve ser verdadeiro
True or True -> True
True or False - > True
False or True - > True
False or False -> False

um exemplo:
"""
print()
print('Exemplo de ''or''')
print(True or False)
print(ativo or naoAtivo)

# e  (and):

"""
Também é uma operação binária, ou seja, depende de dois valores. 
AMbos os valores devem ser verdadeiros

True and True - > True
True and False -> False
False and True -> False
False and False ->True 

"""
print()
print("testando 'and'")
print(ativo and naoAtivo)
print(5>5)
print(5<=5)
print(5<6 or 5<=4) # True or False - > True
print(5<6 and 5<=4) # True and False - > False

"""A ordem de precedência natural dos operadores
primeiro as operações aritméticas, depois as de comparação, por fim as
lógicas:

exponenciação **
multiplicação * / // %
adição + -
relação == != <= >= > <
not
and
or
"""
