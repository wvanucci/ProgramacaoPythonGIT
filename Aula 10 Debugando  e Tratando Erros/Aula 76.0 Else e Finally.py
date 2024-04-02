"""
Else/Finally

Dica de quando e onde tratar código:
Toda entrada deve ser tratada!

OBS: A função do uário é tdestruir o sistema

else ≥ executado se NÃO ocorre o erro (se nao entrar nos blocos except)
finally ≥ é SEMPRE executado, independente se houve exceção ou não
    Utilizado para fechar ou desalocar recursos

tratamento genérico
def dividir(a, b):
    try:
        return a/b
    except ValueError:
        return 'Valor incorreto'
    except ZeroDivisionError:
        return ' X divisão por zero'
    except:
        return 'Ocorreu problema'

print(dividir(1,'n'))
"""

def dividir(a, b):
    try:
        return int(a)/int(b)
    except (ValueError, ZeroDivisionError, NameError) as erro:
        return f'Ocorreu erro: {erro}'
    except ZeroDivisionError:
        return ' X divisão por zero'
    except:
        return 'Ocorreu problema'

n1 = input('Numero 1')
n2 = input('Numero 2')

print(dividir(n1,n2))