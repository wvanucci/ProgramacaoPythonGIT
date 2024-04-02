"""
Utilizar tuplas SEMPRE  que não precisamos modificar os dados contidos em uma coleçã0:
Exemplo:
    meses = ('janeiro', 'fevereiro', ...,)
    a ordem  dos meses não se alteram, portanto seria interessante criar conforme tupla (depende muito a situação)
    na tupla meses não podemos adicionar valores ( o .append não funciona pois tupla é imutavel)
    por isso seria necessario usar tupla para não usar comando de add

Nas tuplas podemos acessar valores como nas listas. Assim como interar usando for e/ou while

A MAIORIA DOS MÉTODOS QUE VIMOS EM LISTAS SÃO POSSÍVEIS EM TUPLA. SOMENTE MéTODOS DE MUTáVEIS NÃO SÃO.
"""

# porque utilizar tuplas:
# 1 -  TUPLAS SÃO MAIS RÁPIDAS DO QUE LISTAS (PARA BIG DATA, DATA SCIENCE É MELHOR PARA OPERAÇÕES). tuplas vai parecer
        #uma variavel
# 2 - DEIXA O CÓDIGO MAIS SEGURO (POR SER IMUTÁVEIS)
# 3 - NA TUPLA NÃO TEMOS PROBLEMA DE SHALLOW COPY (OLHAR EXEMPLO NA AULA DE LISTA 1.4)