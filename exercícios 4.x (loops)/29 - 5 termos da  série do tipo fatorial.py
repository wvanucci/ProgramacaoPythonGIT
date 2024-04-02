# 5 temos do tipo S(n) = 0 +1/2! + 2/4! +3/6! .... + n/(2n)! (sum(n=0 to 5 ) n/((2n)!))

from math import factorial
print('Série do tipo S(n) = 0 +1/2! + 2/4! +3/6! .... + n/(2n)!')
n = int(input('Digite n: '))
s_n = 0

for i in range (0,n+1):
    fat = 2*i
    s_n+=i/(factorial(fat))

print(f'A série S(n) até n = {n} é {s_n}')