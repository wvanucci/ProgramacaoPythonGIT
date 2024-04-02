# combinando filter() e map()

nomes = [ 'Vanessa', 'Ana', 'Maria']

# criar uam lsita contendo 'Sua instrutura é '+ nome, desde que cada nome tenha menos de 5 carateres

lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) <5, nomes)))
# os dados para o map são os dados filtrados (filter)
# print(list(filter(lambda nome: len(nome) <5, nomes)) teste do filter
print(lista)