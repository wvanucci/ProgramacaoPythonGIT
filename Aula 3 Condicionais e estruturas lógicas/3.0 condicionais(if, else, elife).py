"""" Estruturas COndicioionais: if(se), else(senao), elif( senao se)

"""
# exemplo if, else, elif no python:

idade = int(input('Qual sua idade? '))
if idade == 1: #os dois pontos indicam novo bloco (próximo bloco identado 4 espaçoes)
    print('Recem nascido') #deve finalizar um com uma linha e branco (sem identação)
elif idade == 18:
    print('Tem 18 anos')
elif idade <14:
    print('É uma criança')
elif 14 < idade < 18:
    print('É adolescente')
else:
    print('Maior de idade')
                         #finalizando com nova linhha (Lembrando que esse comentários são errados fazer em um programa)


