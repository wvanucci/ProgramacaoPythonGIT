# Importando biblioteca PDB; função set_trace
# Comandos básicos do PDB
# l (listar onde estamos no código)
# n (próxima linha)
# p (imprime variável)
# c (continua a execução  - finaliza debuffging)
import pdb
nome = 'Jullio'
sobrenome = 'Machado'
pdb.set_trace()   # função para fazer pointbreak
nome_completo = nome+' '+sobrenome
curso= 'Programação Python'
final = nome_completo + ' faz o curso '+curso
print(final)