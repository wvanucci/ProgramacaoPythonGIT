#Nomeando parâmetros: Código ficar mais claro

def nome_completo(nome, sobrenome): #é bom colocar parametros claros ex: nome e sobrenome
    return f'Seu nome é {nome} {sobrenome}'

print(nome_completo('Angeline', 'Julie'))

#Parâmetros são variáveis declaradas na definição de uma função;
#Argumentos são dados passados durante a execução de uma função;

#A ordem dos parâmetros importa

#Argumentos nomeados (keyword arguments)
#se utilizamos nomes dos parâmetros nos argumentos para informá-los, podemos utilizar qualquer ordem

print(nome_completo(nome='Angeline',sobrenome='Jolie'))
print(nome_completo(sobrenome='Machado',nome='Ana')) #assim nao importa a ordem. Mas tem q conhecer a função

# Erro comum

def soma_impares(num):
    total=0
    for n in num:
        if n %2 !=0:
            total = total +n                    #somar os impares da lista
    return total                                #o return sai da função, por isso nao pode estar no bloco do if

lista=[1,2,3,4,5,6]
print(soma_impares(lista))