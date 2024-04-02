"""
Set Comprehension
set = {1,2,3,4,5} nao aceita valores repetidos e ordeção, fatiamente. Mas oepra matematicamente sepa


"""

num = {n for n in range(1,7)}
print(num)

print()

n = {x**2 for x in range(10)}
print(n)

print({letra for letra in 'Geek University'})  #sem repetir e sem ordenação

