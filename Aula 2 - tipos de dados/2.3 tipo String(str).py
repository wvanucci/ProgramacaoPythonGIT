""""
Tipo String
Em Python, um dado é considerado do tipo string sempre que:
 Estiver entre aspas simples ou aspas duplas ou aspas simples triplas ou aspas triplas

 Exemplos:
 '123', 'a', "3", "False",'True', '2.3', '''4.2'''

 """

# como pular linhas
print('Wilson \nVanucci')
nome = 'Wilson \nVanucci'
nome2 = """Wilson 
Vanucci"""
print()
print(nome,type(nome))
print()
print(nome2,type(nome2))

# Alguns métodos de str são aplicaveis como .upper() entre outros(cursoEmVideo  tem alguns desses métodos)

print()
print('Exemplo de alguns métodos')

umaListaDeStr = nome.split() #transformar a lista
print(umaListaDeStr)
print(umaListaDeStr[1],umaListaDeStr[0]) #acessar termos da lista

# manipular str. Slice de String:
print(nome[0:3]) # retorna as três primeiras str ( 0 - 1 - 2)

#inverter str:
print()
print('Exemplo para inverter string')

print(len(nome)) # verificar o tamanho da string
print(nome[::-1]) #comece do primeiro elemento, vá até o último elemento e inverte
print(nome.replace('V', 'W'))  #trocar letras

"""Como estou comentado está errado. Comentários de uma linha deve ser colocados em uma linha isolado"""
