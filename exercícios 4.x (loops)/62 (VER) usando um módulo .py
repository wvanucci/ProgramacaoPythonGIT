"""Se os números de 1 a 5 são escritos em palavras: um, dois, três, quatro, cinco, então há 2 + 4 + 4 + 6 + 5 = 22 letras
usadas no total. Faça um programa que conte quantas letras seriam utilizadas se todos os números de 1 a 1000 (mil)
fossem escritos em palavras. OBS: Não conte espaços ou hifens.

tentar entender: """

#
quantos = [4, 2, 4, 4, 6, 5, 4, 4, 4, 4]
nomes = {0: 'zero', 1: 'um', 2: 'dois', 3: 'tres', 4: 'quatro', 5: 'cinco', 6: 'seis', 7: 'sete', 8: 'oito', 9: 'nove'}
n1 = 0  # variavel para somar
for i in range(1, 1001):
    l = str(i)  # transforma em string o valor i
    l1 = []  # variavel lista
    for k in range(0, len(l)):  # desmontando a string l
        l1.append(int(l[k]))
    for k in l1:
        n1 = n1 + int(quantos[k])  # somando o valor

print(f' a somas das letras dos algarismos entre 1 e 1000 é {n1}')

# o de cima não conta todos (mas vale a pena entender a lógica e arrmar)
# usei biblioteca indicada
from num2words import num2words

total = ""

for n in range(1, 1001):
    num = num2words(n, lang='pt-BR')  #transforma cada número em escrita exemplo: 23 em vinte e três (lang escolhe a língua
    total += num.replace(' ', '')          # para cada substituir espaçao em brnaco para sem espaço

#mostrar o total (teste):
    #print(total)

print(f'Entre 1 e 1000 temos {len(total)} letras.')

