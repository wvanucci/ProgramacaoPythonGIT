#Exemplo Complexo

def mostrar_informacao(nome='Julio', instrutor=False):
    if nome == 'Julio' and instrutor:
        return 'Bem-Vindo intrutor Julio'
    elif nome == 'Julio':
        return 'Eu pensei que era o instrutor'
    return f'Olá {nome}'

print(mostrar_informacao()) #
print(mostrar_informacao(instrutor=True))
print(mostrar_informacao('Ozzy'))
print(mostrar_informacao(nome='Ozinho'))

# Por quê utilizar parâmetros com valor default?
    #Permite ser mais flexíveis nas funções;
    #Evita erros com parâmetros incorretos
    #permite trabalhar com exemplos mais legíveis de código

# Quais tipos de dados podemos utilizar ocmo valores default para paâmetros?
    #qualquer tipo
        #números, strings, float, bool, listas, tuplas, funções, etc...

#Exemplos
print('\n Exemplos\n')
def soma(n1,n2):
    return n1 +n2

def mat(n1,n2,fun=soma):
    return fun(n1,n2)

def subtracao(n1,n2):
    return n1 - n2

print(mat(2,3))
print(mat(2,2, subtracao)) # os dois primeiros argumentos serão utilizadas na função subtração tbm (na funcao mat
#será retornado a funcao do ultimo argumento (linha 30))