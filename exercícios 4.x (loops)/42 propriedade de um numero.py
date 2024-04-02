import random, math

qt= int(input('Quantos valores deve ter esse conjunto:'))
l = []
for i in range(0,qt):
    a = random.uniform(-1,5)
    print(a)
    if a <0:
        break
    l.append((a))
for i in l:
    if i >= 0:
        aoQ, aoC, raiz = i**2, i**3, math.sqrt(i)
        print(f'{i}² = {aoQ}; {i}³ = {aoC}; raiz de {i} = {raiz}')
    else:
        break

print()