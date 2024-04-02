# verificar a data (com as condições de ano bissexto)
# vou fazer uma função

def vertificar_data():
    lista = [int(input('Qual é o dia: ')), int(input('mês: ')), int(input('ano:'))]
    if 1 <= lista[1] <= 12 and lista[1] !=2 and 1<=lista[0]<=30 and lista[2] != 0:
        return 'É uma data válida'
    elif list[1] == 2 and 1<=lista[0]<=30 and lista[2] != 0:
        if lista[2]%400 ==0 or lista[2]%4 == 0 and lista[2]%100 != 0:
            return 'É uma data válida!'
        elif 1<=lista[0] <= 28 and lista[2]!=0:
            return 'É uma data válida'
        else:
            return 'não é uma data vállida'
    else:
        return 'não é uma data válida'

print(vertificar_data())

