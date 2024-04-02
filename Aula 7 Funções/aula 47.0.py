"""
Funções com Parâmetro Padrão (Default Paramters)

- Funções onde a passage mde parâmetro seja opcional
exemplo, na função print informar ou não um parâmetro é opcional (vai processar):
print('Oi')
print()

#exemplo de função onde a passagem de parâmetro seja obrigatório
def quadrado(num):
    return num*2
print(quadrado(3))
print(quadrado())  #TypeError  nao especificou parametro
"""
def exponencial(num, potencia =2): #se atribuir um valor para o parametro ao utilizar a função o argumento é opcional (parametro = valor)
    return num**potencia

print(exponencial(2,3)) #2**3
print(exponencial(2)) #2**2 pq nao informei o argumento do parametro potencia e por definição ele é 2 (quase uma condição)


# Em função Python, os parametros com valores default (padrão) DEVEM sempre estar ao final da declaração
# Exemplo de ERRO
"""
def test(num=2,num1):
    return num**num1
# vai dar erro: OU coloca todos opcionais ou somente os últimos; o(s) primeiro(s) tem tem que ser
"""