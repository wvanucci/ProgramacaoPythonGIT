"""
Funções com Parâmetros (de entrada)
- Funções que recebem dados para serem processados dentro da mesma

Se a gente pensar em um programa qualquer, geralmente temos:

Entrada -> processamento - > saída

Se a gente pensar em uma função, já sabemos que temos funções que:

- Não possuem entrada;
- Não possuem saída;
- Possuem entrada mas não possuem saída;
- Não possuem entrada mas possuem saída;
- Possuem entrada e saída;

"""

# refatorando uma função com parametro de entrada

def quadrado_de_7(num):
    return num*num

print(quadrado_de_7(1))  # entrada do 1  vai dar 1*7

ret = quadrado_de_7(4)
print(ret)

# se print(quadrado_de_7()) sem entrada vai dar erro pq a função pede uma entrada TypeError

