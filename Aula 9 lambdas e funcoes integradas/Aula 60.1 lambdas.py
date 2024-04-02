# Em funções Python pódemos ter nenhuma ou várias entradas. Em lambdas também

a = lambda: 'Como não amar Python?'
uma = lambda x: 3 * x + 1
duas = lambda x, y: (x * y) ** 0.5
tres = lambda x, y, z: 3 / (1 / x + 1 / y + 1 / z)
# n= lambda x1, x2, x3, ...xn, : <expressão>

print(a())
print(uma(2))  # entrada obrigatória
print(duas(2, 3))  # entrada obrigatória
print(f'{tres(2, 3, 4):.4f}')  # entrada obrigatória

# outro exemplo

print()

autores = ['Isaac Asimov', 'Ray Bradbury', 'E. E. OK', 'Arthur C. Clarke', 'Frank Herbert', 'Euzinh Pata',
           'Elezingo', 'Faz o L', 'OK ok']
# ordernar pelo sobrenome: usar sort()
print(autores)
autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
# explicando: sort -> ordena; sort(key=) é por onde fazer a ordenação, a função lambada vai é processo da ordenação
# o split vai dividir string em uma lista o delimitador é o ' ' e vai pegar o último elemento da lista [-1]
# lower é deixar a str em minusculo
    # ordena pelo ordem ascedente
print(autores)
