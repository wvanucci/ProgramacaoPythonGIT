# Refatorando
"""
def cantar_parabens(aniversariante):
    print('Parabéns para você')
    print('Nesta data querida')
    print('Muitos felicidades')
    print(f'Viva o(a) {aniversariante}!')

cantar_parabens('Lúcio')

"""

#Funções podem ter n parametros de entrada. ou sejam podemos receber como entrada em uma função quantos
#parametros forem necessarios. Eles são separados por vírgula

def soma(a, b):
    return a+b

def multiplica(num,num1):
    return num1*num

def outra(num,b, msg):
    return (num + b)*msg

print(soma(2,5))
print(multiplica(2,2))
print(outra(1,2,3))

#Obs: se informar um numero errado de argumento teremos TypeError

#print(soma(2,3,4,5))  #vai dar erro. OU SEJA, eu tenho que conhecer a função