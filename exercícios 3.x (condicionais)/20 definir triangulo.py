print(' Verificando se os lados formam um triângulo'.upper())
lado1 = float(input('Lado A: '))
lado2 = float(input('Lado B: '))
lado3 = float(input('Lado C: '))
paraSerTriangulo = (lado1+lado2 > lado3) and (lado2+lado3 > lado1) and (lado1 + lado3 >lado2)
equilatero = lado1 == lado2 == lado3
isosceles = ((lado1 == lado2) and lado1 != lado3) \
            or ((lado3 == lado2) and lado2 != lado1) \
            or ((lado3 == lado1) and lado1!= lado2)
escaleno = lado1 != lado2 != lado3

if paraSerTriangulo and equilatero:
    print('Formam um trângulo equilátero')
elif paraSerTriangulo and isosceles:
    print('Formam um triângulo isosceles')
elif paraSerTriangulo and escaleno:
    print('Formam um triângulo escaleno')
else:
    print('Não formam um triângulo')

