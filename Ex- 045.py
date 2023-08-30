from random import randint
from time import sleep
itens = ['Pedra', 'Papel', 'Tesoura']
posi = randint(0,2)

print('''
----- ESCOLHA UMA OPÇÃO -----
| [1] PEDRA                 |
| [2] PAPEL                 |
| [3] TESOURA               |
-----------------------------''')
jogada = int(input('Qual a sua opção?:'))

print('Jo')
sleep(0.75)
print('Ken')
sleep(0.75)
print('Po!')

if jogada != 1 and jogada != 2 and jogada != 3:
    print('Opção \033[31mINVÁLIDA!')

if jogada == 1:
    print('-'*20)
    print(f'Você escolheu \033[97mPEDRA\033[m \nO Computador escolheu: \033[31m{itens[posi].upper()}\033[m')
    print('-'*20)
    if itens[posi].upper() == 'PEDRA':
        print('Deu \033[33mEMPATE!')
    elif itens[posi].upper() == 'PAPEL':
        print('Você \033[31mPERDEU!')
    else:
        print('Você \033[32mVENCEU!')

elif jogada == 2:
    print('-'*20)
    print(f'Você escolheu \033[97mPAPEL\033[m \nO Computador escolheu: \033[31m{itens[posi].upper()}\033[m')
    print('-'*20)
    if itens[posi].upper() == 'PEDRA':
        print('Você \033[32mVENCEU!')
    elif itens[posi].upper() == 'PAPEL':
        print('Deu \033[33mEMPATE!')
    else:
        print('Você \033[31mPERDEU!')
else:
    print('-'*20)
    print(f'Você escolheu \033[34mTESOURA\033[m \nO Computador escolheu: \033[31m{itens[posi].upper()}\033[m')
    print('-'*20)
    if itens[posi].upper() == 'PEDRA':
        print('Você \033[31mPERDEU!')
    elif itens[posi].upper() == 'PAPEL':
        print('Você \033[32mVENCEU!')
    else:
        print('Deu \033[33mEMPATE!')

