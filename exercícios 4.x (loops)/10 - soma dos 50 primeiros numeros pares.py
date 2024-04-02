#lembrando que zero é par
contador, numero, soma = 1 , 0, 0
while contador <= 51:
    if numero%2 == 0: # somente se o numero for par...
        print(numero)
        soma += numero
    contador += 1  # ...será printado e vai aumentar o contador
    numero += 1  # isso faz um papel do range do for
print(f'A soma dos nº pares entre 0 - 50 é {soma}')