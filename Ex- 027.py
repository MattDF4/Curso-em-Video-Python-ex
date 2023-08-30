nomec = str(input('Digite seu nome completo:')).strip().split()
print('='*60)
print(f'O primeiro nome: {nomec[0]}')
print('='*30)
print(f'O último nome: {nomec[len(nomec)-1]}')
#Apenas {nomec[-1] também funciona, o Ptthon interpretará como o código acima fez também.
