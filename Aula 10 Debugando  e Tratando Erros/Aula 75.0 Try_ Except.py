"""
o bloco try/except

utilizamos para tratar erros que podem ocorrer no nosso código. Previnindo assim que o programa pare de funcionar e o
usuário receba mensagens de erro inesperadas.

A forma geral mais simples é:

try:
    //execução problemática
except:
    //o que deve ser feito em caso de problema

"""

# Exemplo 1 - tratando erro genério

try:                # pode ter erro
    geek()
except:             # se tiver faça o seguinte
    print('Deu algum erro')

# colocar 