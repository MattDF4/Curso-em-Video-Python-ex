num = int(input('Escolha um número:'))
lim = int(input('Deseja multiplica-lo até onde?:'))
for c in range(1, lim+1):
    print(f'{num}x{c}={num*c}')
