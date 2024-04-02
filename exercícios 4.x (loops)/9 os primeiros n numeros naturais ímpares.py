# natural = inteiro nãi negativo
valor = int(input('Quantos numeros ímpares inteiros quer conferir? '))
contador, numero = 1 ,1
while contador <= valor:
    if numero%2 != 0: # somente se o numero for ímpar...
        print(numero)
        contador += 1  # ...será printado e vai aumentar o contador
    numero += 1  # isso faz um papel do range do for

