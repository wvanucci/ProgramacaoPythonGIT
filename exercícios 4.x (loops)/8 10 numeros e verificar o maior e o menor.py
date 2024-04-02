#fazendo com lista
lista = []
contador = 1

while contador < 11:
    valor = float(input(f'Digite seu {contador}º valor: '))
    lista.append(valor)
    lista.sort()
    contador += 1
#verificar a lista:
#print(lista)
#verificar contador:
#print(contador)
# verificar tamanho da lista (lembrando que vai de 1 até len(lista))
print(len(lista))
print(f'o menor valor digitado é {lista[0]} e o maior é {lista[len(lista)-1]}')

# ou (funções min e max)
print(f'o menor valor digita é {min(lista)} e o maior é {max(lista)}')