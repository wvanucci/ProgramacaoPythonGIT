from collections import Counter

print(Counter('Wilson Vanucci'))

# outro exemplo: mostrar quantidade de palavras que mais aparecem
print('\n OUTRO EXEMPLO:\n')

texto = """ Lorem ipsum sapien ipsum maecenas auctor nunc vestibulum tincidunt dictumst, nunc magna lectus pretium et id
 volutpat pretium justo aliquam, ad laoreet faucibus in est viverra consequat fermentum. ultrices vivamus nostra mattis 
 eros euismod nisi convallis sodales facilisis varius gravida luctus potenti facilisis elit, risus sagittis in mi dui 
 lacus vestibulum fermentum phasellus viverra aptent nam sapien. convallis sagittis fames lacus velit eleifend eget 
 libero, auctor tempus netus maecenas sed quisque viverra hendrerit, feugiat metus mi laoreet maecenas rutrum. maecenas
 nulla laoreet dictumst nunc vel massa pharetra, suspendisse purus metus vehicula nullam auctor. 
llamcorper molestie diam libero, tortor egestas nostra iaculis, vitae etiam. elementum donec dui cras accumsan
ro urna turpis, senectus fusce lacinia per cursus rhoncus diam dui curae dui, justo non sit sem ac
"""

palavras = texto.split()
print(palavras)
print(Counter(palavras))

#podemos usar loop for para ver as palavras mais usadas, mas usamos most common
reser= Counter(palavras)
print(reser.most_common(5)) #5 palavras com mais ocorrência (gera uma lista de tupla)

