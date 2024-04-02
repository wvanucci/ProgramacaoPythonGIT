"""
Erros mais comuns em Python
IPC: Aprender a Ler saídas de erro
-SyntaxeError - Ocorre qunado o Python encotnra um erro de sintaxe. Ou seja, escreveu que o Python nao reconhece
como parte da linguagem
    #exemplos
    a)
    def funcao:                    #falta parentese
        print('asda')

    b) None = 1
    c) return fora da função

-NameError -  Ocorre quando uma variável ou funçao nao foi definida
    a)
    print(geek)

    b)
    geek()

    c)
    a = 18
    if a<10:
        msg = 'é maior que '
    print(msg)  # nao entra no bloco if e  msg nunca foi definido

- TypeError - > Ocorre quando uma função/operação é aplicada errado de type
Exemplos

    a) print(len(5))  # len nao opera em inteiro (somente em iterável)
    b)print('Geek' + []) # tentando concatenar tipos diferentes ( str não opera com adição com o tipo lista)

- IndexError -> Ocorre quando tentamos acessar um elemento em uma lsita ou outro tipo de dado indexado utilizando
um índice inválido
Exemplos
    a)
    lista = ['2323']
    print(lista[2])

- ValueError - Ocorre quando uam função/operação built-in (integrada) recebe um argumento com tipo correto, mas valor
inapropriado
exemplo:
    a) print(int('Geek'))
    b)

- KeyError - > Ocorre quando tentamos acessar um dicionário com uma chave que não existem
exemplos:
    dic{}
    print(dic['Geek'])

- AttributeError - Ocorre quando uma variável não em atributo/função

exemplos

    a)
    trupla = 11,23,123,2
    print(tupla.sort()) # sort() é aplicada só em lista

-IdentationError -> Ocorre quando não respeitamos a identação do Python (4espaços)
exemplos
    a)
    def novaf():
    print()

OBS: Exceptions e Erros são sinônimos na programação

masi erros: https://docs.python.org/3.10/library/exceptions.html
"""