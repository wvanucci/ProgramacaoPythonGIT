"""
List Comprehension

POdemos add estruturas condicionais lógicas
"""

# Exemplos

nl=[1,2,3,4,5,6]
pares = [num for num in nl if num %2 ==0]
impares = [num for num in nl if num %2 !=0]
print(pares)
print(impares)

#refatorar

pares = [num for num in nl if not num%2] # Qualquer numero par módulo de 2 é 0 e 0 no Python False. not False = True
impares = [num for num in nl if num%2] #ímpar módulo de 2 é 1, e 1 em Python é True

print(pares)
print(impares)

print()

#exemplo 2

res = [n*2 if n%2==0 else n/2 for n in nl]
print(res)