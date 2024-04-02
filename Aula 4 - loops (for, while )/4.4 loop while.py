"""
Loop While (enquanto)

Forma geral

while expressão_booleana:
    //execução do loop

O bloco do while será repetido enquanto a expressão booleana for verdadeira
Lembrando: Expressão booleana é toda expressão onde o resultado é verdadeira ou falso
"""
# programa similar range usando while:

numero = 0

while numero < 10:
    print(numero)
    numero += 1
    # OBS: Em um loop while, é importante que cuidemos do critério de parada, ou seja,
    # só para quando booleano for falso (por isso usamos break)
# exemplo 2:

resposta = ''
while resposta != 'sim':
    resposta = input('Já acabou jéssica? ').lower()

