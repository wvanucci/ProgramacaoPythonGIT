"""
Faça uma função que receba como parâmetro o valor de um ângulo em graus e calcule o valor do seno
desse ângulo usando sua respectiva série de Taylor:
[ \sin x = \sum_{n=0}^{\infty} (-1)^n \frac{x^{2n+1}}{(2n+1)!} =
x - \frac{x^3}{3!} + \frac{x^5}{5!} - … \text{ para todo } x. ]

Se você tiver mais alguma dúvida ou precisar de ajuda adicional, é só perguntar!

"""
import math
pi=math.pi

def seno(angulo):
    global pi
    rad = angulo * pi / 180
    soma = 0
    for i in range(100):
        prod = 1
        for p in range(1, (2 * i + 1)+1):
            prod *= p
        #print(prod)
        x = ((-1) ** i / prod) * (rad ** (2 * i + 1))
        soma += x
        #print(soma)
    return f'{soma}'

print(seno(60))

