# 1 + 2 + 3 + 4 + 5 + 6 +...+ n
n = int(input('Qual valor?' ))
soma = 0
for i in range(1, n + 1):
    soma += i
print(soma)

# 1 - 2 + 3 - 4 + 5 - 6 +...+ (2n - 1)
n = int(input('Até qual valor? '))
soma = 0
for i in range(1, (n * 2 - 1) + 1):
    if i % 2 == 0:
        i *= -1
    soma += i
print(soma)

# 1 + 3 + 5 + 7 +...+ (2n - 1)
n = int(input('Até qual valor? '))
soma = 0
for i in range(1, (n * 2 - 1) + 1, 2):
    soma += i
print(soma)