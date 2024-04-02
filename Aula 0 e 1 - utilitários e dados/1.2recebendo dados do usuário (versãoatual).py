""""
input() -> todo dado recebido via input é do tipo str

Em pythron,string, é tudo que estiver entre:
 - Aspas simples:
  - Aspas duplas:
  - aspas simples triplas;
  - aspas duplas triplas.

  Exemplo:
- As pas simples -> 'Angeline Jolie'
- Aspas duplas - > "Angeline Jolie"
-Aspas siples triplas- > ''' Angeline Jolie'''
 - Aspas duplas triplas -> (não vou usar aqui pq ja tem um comentario com aspas triplas)
"""

# entrada
    #exemplo do print mais atual 3.7 (eu acho)

print('Qual seu nome? ')
nome = input()

print(f'seja bem-vindo {nome}')

print('Qual sua idade? ')
idade = input()
#processamento


#saída
print(f'O(a) {nome} tem {idade} anos')

"""
Cast é a 'conversão' deu um tipo de dado para outro """
print(f'O(a) {nome} nasceu em {2020-int(idade)}')  # int(idade) =>cast

