"""
Conjuntos

-Conjuntos em qualquer linguagem de programação, estamos fazendo referência à Teoria dos Conjuntos
da Matemática

 - Aqui no python, os conjuntos são chamados de Sets

Dito isso, da mesma forma que na matamática:
- Sets (conjuntos) não possuem valores duplicados;
- Sets (conjuntos) não possuem valores ordenados;
- Elementos não são acessados via índice, ou seja, conjuntos não são indexados;

Conjuntos são bons para utilizar quando precisamos armazenar elementos
mas não nos importamos com a ordenação deles. Quando não precisamos se preocupar
com cchaves, valores e itens duplicados

Os conjuntos (sets) são referenciados em Python com chaves {}

Diferença entre Conjuntos(set) Mapas(Dicionários) em Python:
    -um dict tem keys e valeus;
    -um conjunto tem apenas valeus;
"""
#Definindo um conjunto:
    #forma 1
s = set({1,2,3,4,5,5,6,7,2,3}) #repare que temos valores repetidos
print(s)
print(type(s))
        #OBS: Ao criar um conjunto, caso seja adicionado um valor existente,
        #o mesmo será ignorado sem gerar erro e não fará parte do conjunto

    # Forma 2 (usual)
s = {1,2,3,3,4,5}
print()
print(s)
print(type(s))


