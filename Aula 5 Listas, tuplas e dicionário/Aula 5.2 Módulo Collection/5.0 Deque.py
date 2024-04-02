"""
Deque ->Lista de alta performance
ALGUNS MÉTODOS:
"""
from collections import deque

#criando deques

deq = deque('curso')
print(deq)

deq.append('y') #adiciona no final
print(deq)

    #potencilidade
deq.appendleft('k') #adiciona no começo
print(deq)

#removendo
print()
print(deq.pop())
print(deq)

    #potencialidade
print()
print(deq.popleft())
print(deq)