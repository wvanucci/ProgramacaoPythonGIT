#definindo funçlão

def diz_oi():
    print('oi')

diz_oi()

"""
OBS:
1 - pode utilizar outra funções dentro de uma funtção
2- executa 1 tarefa
3 nao retorna nada
4 - nao recebe nem uma parametro
5 - para utilizar tem que realizra a chamda de execução (linha 6)
"""
# exemplo de utilizar função em loop utilizando outra função built -in (for e range)
for n in range(5):
    diz_oi()

#em python, podemos inclusive criar variaveis do0 tipo de uma função e executar esta função através da variável
print("exemplo 2")
canta = diz_oi()

canta