num = int(input('Digite um número:'))
ndd = 0
for c in range(1, num+1):
    if num % c == 0:
        ndd = ndd + 1
        print(end=f' \033[31m{c}\033[m')
    else:
        print(end=f' \033[30m{c}\033[m')
if ndd == 2:
    print(f'\nO número \033[31m{num}\033[m é PRIMO! \nPois foi é divisível apenas por \033[31m2\033[m números.')
else:
    print(f'\n\033[31m{num}\033[m não é um número primo \nPois é divisível por mais de duas vezes. (\033[31m{ndd}\033[m)')
