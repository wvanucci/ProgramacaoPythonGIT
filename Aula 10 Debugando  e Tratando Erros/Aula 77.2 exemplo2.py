# Importando biblioteca PDB; função set_trace
# Comandos básicos do PDB
# l (listar onde estamos no código)
# n (próxima linha)
# p (imprime variável)
# c (continua a execução  - finaliza debuffging)
"""
nome = 'Jullio'
sobrenome = 'Machado'
import pdb; pdb.set_trace()   # função para fazer pointbreak
nome_completo = nome+' '+sobrenome
curso= 'Programação Python'

final = nome_completo + ' faz o curso '+curso
print(final)

"""

# Vantagem: Realizar debug em um lugar específico (import pdb; pdb.set_trace() ), colocando o comando
# onde você quer utilizar. No python, 3.7 + não precida importar pdb ( é uam função integrada Built-In)
# é só utilizar breakpoint()

nome = 'Jullio'
sobrenome = 'Machado'
breakpoint()  # função para fazer pointbreak
nome_completo = nome+' '+sobrenome
curso= 'Programação Python'

final = nome_completo + ' faz o curso '+curso
print(final)