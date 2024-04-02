"""Para fixar

Temos dados iteráveis:
dados:a1, a2,...an

temos uma função
função: f(x)
Utilizamos a função map(f,dados)onde map irá  'mapear' cada elemento dos dados e aplicar a função.
O Map Object que é gerado: f(a1), f(a2), f(...), f(an)
"""

#Mais um exemplo
    # lista de cidade e temperatura em celsius
cidades = [('Berlim', 29),('Cairo',36), ('Buenos Aires',19), ('Los Angeles', 26), ('Tokio',27), ('Nova york', 28), ('Londres', 22)]
 #mostrar osdas em farenheit
print(cidades)
c_para_f = lambda dado: (dado[0], f'{((9/5)*dado[1] +32):.4f}')

print(list(map(c_para_f, cidades)))

