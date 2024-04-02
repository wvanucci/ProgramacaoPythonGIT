"""
chico = 1.5m e cresce 0.02m por ano e zé = 1.1 cresce 0.03m por anos. Quando zé é maior que chico
"""

chico = 1.5
ze = 1.1
ano = 0
while chico > ze:
    ano += 1
    chico += 0.02
    ze += 0.03
print(ano)