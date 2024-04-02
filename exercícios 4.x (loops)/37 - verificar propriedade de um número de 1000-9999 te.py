""" teste para verificar transformação str para int de primeiro termos de um núemro
n = '3032'
print(type(n))
print(n[0:2])
int(n[0:2])
print(int(n[0:2]))
print(type(int(n[0:2])))
"""
# verificar propriedade de um número de 1000-9999:  se a soma do nº de maior baixa ordem mais o de menor baixa ao
# quadrado é igual o próprio numero confirmar (Ex: 3025, 30+25=55 -> 55² =3025)

for i in range(1000,10000):
    str_i = str(i)           # str_i está em str
    i1 = int(str_i[0:2])
    i2 = int(str_i[2:4])
    a = i1 + i2
    if int(str_i) == (a**2):    # devo mudar para int para verificar igualdade
        print(f'{str_i}, {i1}+{i2} = {a} -> {a}² = {str_i}')





