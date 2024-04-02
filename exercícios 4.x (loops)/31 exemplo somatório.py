# S= 1/1 + 3/2 + 5/3
n=int(input('Digite um valor n parao somatório: '))
s = 0
for i in range(1, n+1):
    s += (2*i -1)/i

print(s)

"""
pode ser da seguinte forma?
for i in range(0, n+1):  
    s += (2*i + 1)/i

não pq para i = 0 s=1/0 (nao existe)    
"""