"""
dfinição de funções - são pequenos partes itgos que realizam tarefas específicas
    ex: print() len() max() min() [são funções nativas do python]
- pode ou nao receber entradas de dados e retornar uma saída de dados
-uteis para executar procedimento similares por repetidas vezes

OBS: se escrever uma função realiza várias tarefas dentro dela; é bom fazer uma verificação para que a função seja
simplificada
"""
#exemplo de função

cores = ['verde', 'amarelo','azul','branco']

#utilizando a função integrada (built - in) print do Python

print(cores) # note usei a função print para imprimir o dado; nesse caso o dado é a lista cores

cores.append('roxo') #função da lista; o append()
print(cores)

#verificar o que faz o print (built - in)
print(help(print))

#DRY - don't repeat yourself, nao repita você mesmo/ não repita seu código
"""
como definiar função?
    def nome_da_funcao(parametro_de_entrad):
        bloco_da_funcao
IPC:  nome da função SEMPRE com letras minúsculas e se for nome composto separar por underline [_];
    parametros  de entrada - se tem mais dadso separar por vírgula
    bloco da função é o corpo da função; o processamento da função (código)
OBS: def significa 'reservado'
"""