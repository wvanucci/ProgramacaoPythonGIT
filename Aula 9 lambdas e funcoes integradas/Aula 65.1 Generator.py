#comparação de memória
from sys import getsizeof

# Gerando uma lista de números com List comprehension

lit_comp = getsizeof([x*10 for x in range(1000)])

# Gerando lista com set comprehension

setcomp = getsizeof({x*10 for x in range(1000)})

# Gerando uma lista de numeros com dict tionary

dic_comp = getsizeof({x: x*10 for x in range(1000)})

# Gerando uma lista de num com Generator
gen = getsizeof(x*10 for x in range(1000))

print('Memória')
print(f' List comp {lit_comp}bytes/ set {setcomp}bytes/ dictcomp {dic_comp}bytes/ gen {gen}bytes')
#note trabalhar com generator objeto gasta bem menos memória/list compehrension é interessante tbm
# pq dict e set ocupa mais memória - pq tem q ter recurso computacional para ver se tem key repetidas (dict) e valores e
#reptidos em set

print()

# Eu posso iterar no Generator Expression? Sim!

gen = (x*10 for x in range(1000))
print(gen) # gen não é um objeto explicito; mas posso operar cada elemento

for num in gen:
    print(num)