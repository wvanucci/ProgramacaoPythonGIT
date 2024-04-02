qtd = int(input('Quantas vezes esse loop deve rodar: '))
soma = 0
for n in range(1,qtd+1):
    num = int(input(f'informe o {n}º valor: '))
    soma +=num
print(f'A soma é {soma}')

print()

"""lista de códigos de emotion
https://unicode.org/emoji/charts/full-emoji-list.html"""

# código original  U+1F600
# modificar U0001F600  (substituir + por 000)
for x in range(3):
    for num in range(1,11):
        print('\U0001F4A9'*num)

