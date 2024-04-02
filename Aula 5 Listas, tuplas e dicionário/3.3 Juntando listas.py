"""
ADicionando produtos. Exemplo:
Carrinho de compras:
    produto 1:
        -nome
        -quantidade
        -preço
    produto2:
        nome
        quantidade
        preço
"""
# Forma 1: utilizando lista
    # uma lista de lista
print('\n Foma de Lista')
carrinho = []
produto1 = ['PS4', 1, 3000.00]
produto2 = ['GTA IV',1,150.00]

carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)

# Devemos saber qual é o indice de informação do produto

# Forma 2: Utilizando tupla
    #tupla de tupla
print('\n Forma de tupla')
produto = ('ps4',1,3000.00)
produto = ('GTA',1,150.00)

carrinho = (produto, produto)
print(carrinho)

#Forma 3 - dicionário:
    # Usando lista no dict (podemos fazer uma tupla de dict)
print('\n Forma de dict:')
carrinho = []
produto1={'nome':'PS4','quantidade':1,'preço':3000.00}
produto2={'nome':'GTA','quantidade':1,'preço':150.00}
carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)

    # Na forma de dict evita problemas. Podemos identificar a informação de cada elemento

