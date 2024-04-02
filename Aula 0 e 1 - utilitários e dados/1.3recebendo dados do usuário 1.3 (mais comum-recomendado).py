nome = input('Qual o seu nome? ')

print(f'Seja bem-vindo {nome.lower().title()}') # saida do nome com o padrão de letra maisculono começo

idade = int(input('qual sua idade? '))  # já fiz o cast( transformar tipode dados) entre str e para int

print(f'O(a) {nome} tem {idade} anos e nasceu em {2020 - idade}.')
