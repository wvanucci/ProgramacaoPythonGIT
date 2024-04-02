"""Nas funções podemos ter (NESTA ORDEM de precedência):
-Obrigatórios
-*args
-paramêtros default (não obrigatório)
- **kwargs


"""


def minha_fun(num, nome, *args, solteiro=False, **kwargs):
    print(num)
    print(nome)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(args)
    print(f'{kwargs}\n')


minha_fun(8, 'Julia')
minha_fun(18, 'Felicity', 4, 5, 3, solteiro=True)
minha_fun(34, 'Felipe', eu='não', voce='vai')
minha_fun(19, 'Carla', 9, 4, 3, java=False, python=True)

# por quê é imopirtante manter a ordem dos parâmetros
print()
"""
#CERTO
def mostra_info(a,b, *args, instrutor = 'Geek', **kwargs):
    return [a,b,args,instrutor,kwargs]
print(mostra_info(1,2,3,sobrenome='Univer',cargp='Instrutor'))
a=1
b=2
args=(3,)
instrutor = 'Geek'
kwargs={sobrenome:'university', cargo ='instrutor'}
"""


# modo errado

def mostra_info(a, b, instrutor='Geek', *args, **kwargs):
    return [a, b, args, instrutor, kwargs]


print(mostra_info(1, 2, 3, sobrenome='Univer', cargp='Instrutor'))
# Saída: [1, 2, (), 3, {'sobrenome': 'Univer', 'cargp': 'Instrutor'}] note que argas está vazia, ou seja 3 levou
# instrutor por isso, a ordem de precedência é importante

print()


# Desempacotrar ocm **kwargs

def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"


nomes = {'nome': 'Felicity', 'sobrenome': 'Jones'}

print(mostra_nomes(nomes))  #vai dar errado

print(mostra_nomes(**nomes)) #avisa que a variavel nomes é dic e desempacota (como foi feito no args)