"""
**kwargs
É um parâmetro, mas diferene do & args que coloca os valores em tupla, o **kwargs exige que utilizemos parãmetro nomeados,
e transforma esses parâmetros em um dicionário
"""


# exemplo

def cores_favoritas(**kwargs):
    print(kwargs)


cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', vanesa='brnaco')  # cria um dic

#exemplo 2
print()

def cores(**kwargs):
    for pessoa, cor in kwargs.items(): #interando com método items() key=pessoa e values=cor
        print(f'A cor favorita de {pessoa.title()} é {cor.lower()}')

cores(marcos='verde', julia='amarelo', Fernanda='azul', vanesa='Branco')  # cria um dic

#OBS: os parâmetros *args e **kwargs não são obrigatórias

#exemplo mais complexo
print('Exemplo complexo')
print()

def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        #print(kwargs['geek']) chave do dic
        return 'Você recebeu um cumprimento Pythônico Geek!'
    elif 'geek' in kwargs:
        return f'{kwargs["geek"]} Geek'
    return 'Não tenho crt quem vc é'


print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='Oi'))
print(cumprimento_especial(geek='especial'))