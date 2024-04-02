# 0 1 1 2 3 5 8 13 ... até o primeiro número superior do qual foi digitado
t1=0
t2 = 1
cont = 1
n = int(input('Até qual nº: '))
print(f'{t1} {t2}', end= ' ')
while cont <= n:
    cont+=1
    t3 = t1 +t2
    print(t3, end= ' ')
    t1=t2
    t2=t3
    if t3 > n:
        break
