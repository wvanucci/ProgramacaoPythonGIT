# soma dos n primeiros primos (lembrando q 1não é primo)

num = int(input("Digite um numero: \n"))

while num < 1:
    num = int(input("Digite um numero: \n"))

primo = []
lista = []
cont = 1

while len(primo) < num:
    for i in range(1, cont + 1):
        if cont % i == 0:
            lista.append(i)

    if len(lista) == 2:
        primo.append(cont)
        lista.clear()
    else:
        lista.clear()
    cont += 1
print(primo)
print(f"A soma dos {num} primeiros numeros primos é {' + '.join(map(str, primo))} = {sum(primo)}")



"""
.join adiciona str em interavel (lista, str, tupla, dic). Note .join (map(str,primo))
está adcionando '+' em cada termo do interavel primo (list).
Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
 ____________________________________________________________________________________________________
 sum() Parameters
iterable - iterable (list, tuple, dict, etc). The items of the iterable should be numbers.
start (optional) - this value is added to the sum of items of the iterable. The default value of start is 0 (if omitted)
umbers = [2.5, 3, 4, -5]

# start parameter is not provided
numbers_sum = sum(numbers)
print(numbers_sum)

# start = 10
numbers_sum = sum(numbers, 10)
print(numbers_sum)
Output

4.5
14.5
If you need to add floating-point numbers with exact precision, then you should use math.fsum(iterable) instead.

If you need to concatenate items of the given iterable (items must be strings), then you can use the join() method.

'string'.join(sequence)


"""

