meu_dicionario = {
  "marca": "Ford",  # <- Tipo string
  "eletrico": False, # <- Tipo booleano
  "ano": 1964, # <- Tipo inteiro
  "cors": ["red", "white", "blue"] # <- Tipo lista
}

print(meu_dicionario)

print('\n Método keys()')
print(meu_dicionario.keys()) #key() vai retornar lista com as chaves

print('\n Método values()')
print(meu_dicionario.values()) # values() vai retornar umalista com os valores

print('\n Método items()')
print(meu_dicionario.items()) #retorna uma lista de tuplas contendo os pares de chave:valor do dicionário.

# método deep copye shallow copy funcionam para dict:
print('\n Método deep copy para dict:')
novo = meu_dicionario.copy()
novo['d']=4
print(meu_dicionario)
print(novo)

print('\n Método shallow copy')
outro = meu_dicionario
outro['outro']=4
print(meu_dicionario)
print(outro)

# método clear

print('\n Método clear (para o dict novo):')
novo.clear()
print(novo)

# método fromkeys
print('\n Método fromkeys para criar dict')
outro1 = {}.fromkeys('a','b')

print('\n  Método fromkeys para criar dict')
usuario = {}.fromkeys(['nome','apelido','sobrenome'],'desconhecido')
print(usuario)

    # o método fromkeys recebe dois valores: um interável e um valor
    # Ele vai gerar para cada valor do inte´ravel uma chave e irá atribuir a esta chave o valor informado

print('\n  Método fromkeys para criar dict')
veja = {}.fromkeys('teste','valor')
print(veja)
veja1 = {}.fromkeys(range(1,5),'valor')
print(veja1)