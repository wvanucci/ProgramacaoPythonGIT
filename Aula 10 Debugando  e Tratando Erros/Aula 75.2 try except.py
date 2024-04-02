"""

"""
def dicio(dicionario,chave):
    try:
        return dicionario[chave]
        # pode acontecer um erro de passar uma chave nao existente
    except KeyError:
        return None
    except TypeError:
        return None


dic = {'a':'eqwe', 'b':2}

print(dicio(dic,'a'))
print(dicio(dic,'c'))