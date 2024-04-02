#Exemplo complexo

p1 = [8,9.1,7.8]
p2 = [9.8, 8.9, 5.3]
alunos = ['maria', 'pedro', 'carla']

a = list(zip(alunos, p1, p2))
print(a)
print()
final = {dado[0]:max(dado[1],dado[2]) for dado in zip(alunos, p1, p2)}

#print(list(zip((alunos, p1, p2))))
print(final)

# utilizando map

final = zip(alunos, map(lambda nota: max(nota), zip(p1, p2)))
#verificando
#print(list(zip(p1, p2)))  #junção das dnotas
#print(list(map(lambda nota: max(nota), zip(p1, p2)))) #para cada elemento fazendo máximo das notas

print(dict(final))