# interar com reversedd
for letra in reversed('Geek University'):
    print(letra, end='') #  end='' para noa pular linha

# sem o for
print()
print(''.join(list(reversed('Teste Testando')))) # join manipula string -> pega a lista  reversed e junta os elementos em
#forma de string

print()

# Podemos tamb´[em utilizar o reversed() para fazer um loop for reverso
for n in reversed(range(0,10)):
    print(n, end=' ')

print()

#modo usual
for n in range(9,-1,-1):
    print(n, end=' ')