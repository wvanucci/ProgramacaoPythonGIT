"""
Docstrings
 Documentando funções com Docstrings: Importante para especificar/função a função para o futuro

Exemplos
print(help(print)) #imprime o help do print essas informações é o Docstring no print()

"""

#como criar docstrings

def diz_oi():
    """Uma função simples que retorna a string 'Oi'"""
    return 'oi!'

#print(diz_oi())


#print(diz_oi.__doc__)   #como ver a documentação de uma função em Python utilizando a propriedade __doc__

#help(diz_oi)  #Acessando com help

#método de fazer documentação

def exp(n1,pot=2): #dar aspas triplas e dar enter ele faz uma resumo para vc registar
    """
Função quadrado de um 'n1' ou o 'n1' da potência desejada
    :param n1: base
    :param pot: expoente; padrão 2
    :return: retornar a potencia de n1 no expoente pot
    """
help(exp)