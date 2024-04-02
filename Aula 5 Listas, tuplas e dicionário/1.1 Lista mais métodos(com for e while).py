lista1 = [1,99,4,28,123,12,13123,55,464,1231]
lista2 = ['v','a','n','u','c','c','i']
lista3 = []
lista4 = list(range(11)) #list  transforma argumento em uma lista; rangecria elemento de 0 10
lista5 = list('Wilson Vanucci') #tem a msma funçao da lista 2 (mas nesse metodo ele adiciona o sstring ' ')

# Copiar lista
lista7 = lista2.copy()

# podemos contar quantos elementos existe na lista (tamanho da lsita):
print('\33[31mtamanho da lista(len):\33[m ',len(lista7))

#remover ultimo elemento da lista
lista1.pop()  #removeu 1231
print(lista1)
print(lista1.pop())  # removeu 464 da lista 1 e printa o que foi removido
print(lista1)
        #pop remove e retorna

# podemos remover um elemento pelo indice usando pop
print('\n\33[31mRemovendo elemento(pop):\33[m')
print(lista5)
print('\33[31mremovendo um elmento da lista:\33[m ',lista5.pop(2))
print(lista5)
#OBS: Os elemntos á direita desse índice serão deslocados  para esquerda
#OBS; se não houver elemento no indice informado vai dar erro

#limpar um lista:
print('\n\33[31mLimpando lista(clear):\33[m')
print(lista4)
lista4.clear()
print(lista4)

#repetir elementos em uma lista:
print('\n\33[31mRepetir elemento:\33[m')
nova = [1,2,3]
print(nova)
nova = nova*3
print(nova)

#Converter um string para um lista:
print('\n\33[31mConverter str em lista(split).\33[m \n   \33[31mExemplo 1:\33[m ')
curso = 'Curso de Programação '
print(curso)
curso = curso.split()
print(curso)
#OBS: Por padrão, o split separa os elementos da lista pelo espaço entre elas
#podemos identificar o separador:
print('  \33[31mExemplo 2:\33[m')
curso1='Curso-de-Programação'
print(curso1)
curso1=curso1.split('-')
print(curso1)

#convertendo lista em str:
print('\n\33[31mConvertendo lista em str:\33[m')
lista6 = ['curso','de','programação']
print(lista6)
curso2 = ' '.join(lista6) # pega lista6 e coloca espaço(' ') em cada elemento e transforma em str
print(curso2)

# soma de elemento str:
print('\n\33[31mSomando os interaveis da lista:\33[m')
print(lista2)
soma=''
for elemento in lista2:
    print(elemento)
    soma +=elemento

print(soma)
# OBS: str só pode ser somado com str e int com int (por isso soma inicial é uma str ('')

# somando usando While:
print('\n\33[31mUsando While:\33[m\n')
carrinho = []
produto = ''
while produto != 'sair':
    produto = input(' Adicione o produto na lista ou digite "sair" para sair: ').lower()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

