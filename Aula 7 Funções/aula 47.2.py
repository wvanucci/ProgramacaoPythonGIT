# escopo  - evitar problemas

#variáveis globais

#variáveis locais

instrutor = 'Legolego' #var Global
def dizoi():
    prof = 'Dale Grêmio'
    instrutor = 'Python' #vari local
    return f'oi {instrutor}'

print(dizoi())   # a função trabbalha com varv local se existir uma glogal com o mesmo nome
#print(prof) #só esta declarado na função, nao pode chamar ela para o processamento vai dar NameError

#sE PUDER EVITE VARIAVEL GLOBAL

#Pode ocorrer UnboundLocalError variavel local esta declarada no global e nao dentro da funçao
"""Exemplo do ERRO
total = 0
def inc():
    total= total +1
    return total

print(inc())
"""

#Mas como contornar esse problema?
print(f'\n exemplo 1\n')
total  = 0
def inc():
    global total #avaisa que queremos utilziar uma variável global e se chama total

    total = total +1
    return total
print(inc())

print(f'\n exemplo 2\n')

#podemos ter funções que são declaradas dentro de funções e tambem tem uma especial de escopo de variavel

def fora():
    contador = 0
    def dentro():
        nonlocal contador       #não local, não local e nem global, está na função de cima
        contador = contador + 1
        return contador
    return dentro()   # a função fora é retornar a função dentro

print(fora())  #teste
#print(dentro()) ## mesma ideia de variavel local, o que esta nao funçao nao esta declarada NameError