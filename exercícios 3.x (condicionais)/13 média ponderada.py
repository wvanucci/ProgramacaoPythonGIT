# média ponderada de 3 notas. nota 1 e 2 peso 1 e 3 peso 2

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
n3 = float(input('Terceira nota: '))

mP = (n1+n2+2*n3)/(1+1+2)
if mP >= 6:
    print(f'Média {mP}. Aprovado')
else:
    print(f'Média {mP}. Reprovado')