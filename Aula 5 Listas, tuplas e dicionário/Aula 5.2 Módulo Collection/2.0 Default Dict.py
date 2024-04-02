"""
Default Dict -> Ao criar utilizando-o, nós informamos um valor default
podendo utilizar um lambda para isso. Este valor será utilizado sempre que não houver um
valor definido. Caso entemos acessar uma chave que não existe, essa chave será criada e o
valor defaul será atribuída

OBS: Lambda são funções sem nome, que podem ou não receber parametros de entrada e retornar
valores
"""
from collections import defaultdict

dicionario = defaultdict(lambda:0)

print(dicionario)

dicionario['curso'] = 'Programação em Python'
print(dicionario)

print(dicionario['outro']) #como outro não existe no dict daria erro, porém com
# o default adicionamos um parâmetro valor  (no caso 0) para a chave não existente. Default evita  o  erro

print(dicionario)