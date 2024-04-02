"""
maior numero palíndromo feio a partir do produto de 2 números com 3 digitos
"""

l=[]
l1=[]
maior = 0
for i in range(100,1000):
    for j in range(100,1000):
        a = i*j
        str_a = str(a)
        l.append(str_a)          #só para ver
        if str_a == str_a[::-1]:   #invertir a str e conferir se a str é igual invertido (palindromo)
            int_a = int(str_a)
            l1.append(int(str_a))    #todos os numeros palíndromos
            if max(l1) == i*j:     #max da lista é igual i j guarde i e j
                n1 = i
                n2 = j


print(f'maior número palíndromo feito a partir do produto de 2 números com 3 digito é {n1}*{n2} = {max(l1)}')