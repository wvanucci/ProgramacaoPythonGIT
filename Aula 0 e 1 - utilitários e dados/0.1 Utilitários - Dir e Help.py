""""
Utilitários Python para auxiliarna programação

DIR
e
HELP"""
"""
Dir -> Apresente todos os atributos/proprieades e funções/métodos disponiveis para determinado tipo de dado ou variável

dir(tipo de dado/variável)
por exemplo
dir("Oi")
vai apresentar quais funções ou metodos disponiveis para o tipo de dado/variável

Help -> Apresenta a documentação/como utilizar os atributos/propriedades e funções/métodos disponiveis  para determinado
tipo de dado ou variável.

help(tipo de dado/variavel com o método ou função)
Por exemplo:
help("oi".upper)
nesse caso vai descrever o que o método .upper realiza

"""

"""Vamos usar o terminal do ambiente virtual gupp (usar: workon gupp (no prompt de comando)). Aqui já está no ambiente virtual criado"""

""" UM TRANSCRIÇÃO VIA O QUE FOI FEITO NO TERMINAL DO PYCHARM:

(gupp) C:\Users\Wilson\PycharmProjects\CursoUdemy>python
Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:30:23) [MSC v.1928 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> dir("Geek")
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__
', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul
__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index
', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip',
'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapca
se', 'title', 'translate', 'upper', 'zfill']
>>> help("Geek".lower)
Help on built-in function lower:

lower() method of builtins.str instance
    Return a copy of the string converted to lowercase.
>>> 'GEEK'.lower()
'geek'
>>> help('university'.title)
Help on built-in function title:

title() method of builtins.str instance
    Return a version of the string where each word is titlecased.

    More specifically, words start with uppercased characters and all remaining
    cased characters have lower case.

>>> 'wilson vanucci'.title()
'Wilson Vanucci'
>>> 'WILSON VANUCCI'.lower().title()  #vai converter todas em minusculas depois só as iniciais em maiusculas
'Wilson Vanucci'
"""
