#Exemplo da moeda
import random

def moeda():
    #gerar um numero pseudorandomico
    valor = random.randint(0, 1) #Podemos, uma uma função, retornar qualquer tipo de dados e até mesmo múltipls valores
    print(valor)
    if valor >0.5:
        return 'Cara'
    return 'Coroa'

print(moeda())

#erroes comuns na utilização do retorno