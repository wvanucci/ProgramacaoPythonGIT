"""
fuções com retorno

"""

numeros = [1,2,3]
ret = numeros.pop()  # remove ultimo elemento e guarda esse elemento
print(f'retorno de pop: {ret}')
print(numeros)

ret_print = print(numeros)

print(f'retorno de print: {ret_print}') #print nao retorna NADA

# exemplo
print("")
def quadrado_de_9():
    print(9*9)  #nao estamos retornando estamos usando a função print (imprimindo)

quadrado_de_9()

ret = quadrado_de_9()  #para usar a função em uma variavel deve colocar o return (lembrando que não retornar é o nada None)
print(f'Retorno {ret} \n')

print("______refatorar para retornar_______")
#ex

def quadrado_7():
    return 7*7

ret = quadrado_7()

print(ret) #agora a variavel recebe a função que retorna o valor, portanto o print retorna algo
print(quadrado_7()) # eu acho mais interessante fazer isso/ NOTE: print é diferente de retornar
