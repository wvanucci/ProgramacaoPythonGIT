""" 3 notas entre 0-10. Um trabalho lab de peso 2; avaliaçã semestrel peso 3; exame peso 5.
 0-2,9  reprovao; 3-4,9 recuperação ou aprovado (media 5)"""

tLab = float(input('Primeira nota: '))
aSemestral = float(input('Segunda nota: '))
exame = float(input('Terceira nota: '))

mP = (tLab*2+aSemestral*3+exame*5)/(2+3+5)

if mP >= 5:
    print(f'Média {mP}. Aprovado')
elif 3<=mP<5:
    print(f'Média {mP}. Recuperação')
else:
    print(f'Média {mP}.Reprovado')

