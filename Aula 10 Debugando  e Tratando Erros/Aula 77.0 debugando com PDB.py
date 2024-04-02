"""
Debuggando com PDB
PDB - > Python Debugger

# OBS: podemos utilizar print() para verificar erros, mas é uma prática ruim
def dividir(a, b):
    try:
        return int(a)/int(b)
    except (ValueError, ZeroDivisionError, NameError) as erro:
        return f'Ocorreu erro: {erro}'

print(dividir(2,3))
"""
# Utilizar o debugger
# Em python podemos utilizar debug em pycharm e PDB
# Exlpicação no samsung note tablet

def dividir(a, b):
    try:
        return int(a)/int(b)
    except (ValueError, ZeroDivisionError, NameError) as erro:
        return f'Ocorreu erro: {erro}'

print(dividir(4,0))

