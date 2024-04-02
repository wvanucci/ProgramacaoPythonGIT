"""
Tratar de forma especifica
# Exemplo - Erro específico

try:
    len(5)                               # type error
except NameError:  # só trata NameError
    print('Você está utilizando uma funçõa inexistente')
except TypeError as err:  # chama o TypeError de err
    print(f'Erro: {err}')
"""

try:
    #len(5)
   # geek()
    print('asda'[9])
except NameError as err:
    print(f'Erro: {err}')
except TypeError as errb:
    print(f'Erro: {errb}')
except:
    print('Deu outro erro')