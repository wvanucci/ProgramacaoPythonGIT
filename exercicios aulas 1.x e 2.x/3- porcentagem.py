"""ganhadores de um premio de 780 000,00 reais tem q ser dividido na seguinte qunatidade:
1º 46%
2º 32%
3º o restante"""

valorTotal = 780000.00
primeiro = valorTotal*0.46
segundo = valorTotal*0.32
terceiro = valorTotal*(1-(0.46+0.32))
print(f'O primeiro ganhador ficou com R${primeiro:.3f}, o segundo ficou com R${segundo:.3f} e o '
      f'terceiro com uma quantia de R${terceiro:.3f}')
