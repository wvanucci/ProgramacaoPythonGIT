
def soma_multiplos_numeros(a,b,c, **kwargs):
    print(a+b+c)

l=[1,2,3]
t=(1,2,3)
c={1, 2,3}
soma_multiplos_numeros(*l)
soma_multiplos_numeros(*t)
soma_multiplos_numeros(*c)

dicionario = dict(a=1,b=2,c=3) #as keys (a b e c) etm que ser igual da funcao

soma_multiplos_numeros(**dicionario) #descompactando dict (só pega os valores)

#OBS: desvantagem; Os nomes da chave em um dicionário devem ser o mesmo dos parâmetros da funcao

soma_multiplos_numeros(**dicionario, lang='Python')