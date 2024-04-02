#List Comprehension vs Loop

#Loop

num = [1,2,3,4,5]
num_dobrados=[]

for n in num:
    n1=n*2
    num_dobrados.append(n1)

print(num_dobrados)

#List Comprehensions
print()

print([n*2 for n in num])  #poderoso

print('\n Exemplo 2\n')

nome = "lalala"

print([letra.upper() for letra in nome ])

print('\n Exemplo 3\n')

amigos = ['maria', 'julia', 'pedro', 'guilherme','vanessa']
print([amigo.title() for amigo in amigos]) #primeiro caract em maiusculo

x = [str(n) for n in [1,2,3,4,5]]
print(x)

