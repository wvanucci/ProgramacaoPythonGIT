"""
Len, Abs, Sum, Round
# Len
len() - > Retorna o tamanho (ou seja, o número de itens) de um iterável

"""

# utilizamos a função len(), o python faz o seguinte:
# Dunder len são funções especiais (usado bastante em orientação objeto)
print('Geek University'.__len__())
"""
print(len('ggergre')) utilizado __len__()
"""

"""
# Abs

abs() -> retorna o vlaor absoluto de número inteiro ou real. De forma basíca, seria o seu valor real sem sinal

print(abs(-5), abs(-3.5432), abs(12312312.2))
"""

"""
# sum
sum() - > recebe como parâmetro um iterável, podendo receber um valor  inicial, e retorna a soma total dos elementos, incluindo o valor inicial
sintaxe -> sum(dadso de soma, elemento inicial)
#OBS: O valor inicial default =0

"""
print()
print(sum([1,2,3,4,5])) # default é 0 no final soma zero
print(sum([1,2,3,4,5], 5)) #agora peço para fazer a soma com o 5 no final
#funciona para qualquer coleção:  set, tupla, lista dict

print(sum({'a':1,'b':2,'c':3}.values())) # somar os valores (valoues()) sum não soma string
