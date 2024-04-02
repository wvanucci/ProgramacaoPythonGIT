"""
Imagina que tu quer colocar dois parametros fixos e os outros o usuario pode colocar quandos quiser
"""

def soma(n1,n2, *args):
    return n1+n2+sum(args)

#print(soma())  #note que vai rodar somente se indicar os dois primeiro argumentos obrigatoriamente

print(soma(1,1,3,4,5))  #note que a funçaol soma os args, posso mudar n1+n2+sum(args) na funçao

#bom dependendo do problema, o parâmetro *args é ilimitado  e não obrigatório colocar no processo,
# porém, outros parâmetros são obrigatório

#outro exemplo

def verifica_info(*args):
    if 'Geek' in args and 'university' in args:
        return 'Bem-vindo'
    return 'Eu nao tneho crtz quem vc é...'
    #como args retorna tupla a função vai verificar geek e universityu nessa tupla:

print(verifica_info())
print(verifica_info(1,True,'university','Geek'))
print(verifica_info(1,True,'university',3.145512))

#exemplo 2

def soma_todos_numeros(*args):
    #print(args)
    return sum(args)

print(soma_todos_numeros())
print(soma_todos_numeros(3,2,3))

num= [1,2,3,4,5]
num1= (1,2,3,4,5)

"""
# Desempacotador
n1,n2,n3,n4,n5,n6,n7 = num #cada elemento da lista sera atribuido a uma variavel (mas tem q saber o tamanho da lista)
print(soma_todos_numeros(num)) #TypeError pq nao se soma lista com numero
"""

#agora vamos utilizar o modo *
print(soma_todos_numeros(*num))   #indico que num é uma lista (coleção) então a função realiza um desempacotamento (o * é para isso)
print(soma_todos_numeros(*num1))