"""
Faça um programa que calcule o menor número divisível por cada um dos números de 1 a 20.

Ex: 2520 é o menor número que pode ser dividido por cada um dos números de 1 a 10, sem sobrar resto.
"""

i = 1
j = 1
while j <= 10:      # teste para 1 até 10
    if i % j == 0:  # se a variavel i for divisivel  somente soma j (conta o j)
        j = j + 1
    else:
        i = i + 1   # se para alguma i, nesse intervalo j, não for divisivel o programa volta do 'inicio' ou seja>
        j = 1       # j retorna para o valor inicial
print(i)
