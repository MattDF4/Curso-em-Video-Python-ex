#Faça um programa que jogue par ou ímpar com o computador.
#O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
from time import sleep
v = 0
sequencia = 0
print('''
-----------------------------------------
|             PAR OU IMPAR              |
|          VOCÊ  VS  COMPUTADOR         |
-----------------------------------------''')
while True:
    pc = int(randint(1, 10))
    print('-'*25)
    ioup = str(input('Deseja ser ÍMPAR ou PAR?: ')).upper().strip()[0]
    eu = int(input('Diga sua jogada: '))
    sleep(0.5)
    print('.')
    sleep(0.5)
    print('.')
    sleep(0.5)
    print('.')
    if ioup == 'Í':
        #Se for par:
        if (eu + pc) % 2 == 0:
            print(f'Você \033[31mPERDEU\033[m, o total par foi: {eu+pc}.')
            print(f'Sua jogada: \033[4m{eu}\033[m, jogada do PC: \033[4m{pc}\033[m')
            break
        #Se for ímpar:
        else:
            print(f'VOCÊ \033[32mVENCEU!\033[m O total ímpar foi: {eu+pc}.')
            print(f'Sua jogada: \033[4m{eu}\033[m, jogada do PC: \033[4m{pc}\033[m')
            sequencia += 1
    elif ioup == 'I':
        if (eu + pc) % 2 == 0:
            print(f'Você \033[31mPERDEU\033[m, o total par foi: {eu+pc}.')
            print(f'Sua jogada: \033[4m{eu}\033[m, jogada do PC: \033[4m{pc}\033[m')
            break
        #Se for ímpar:
        else:
            print(f'VOCÊ \033[32mVENCEU!\033[m O total ímpar foi: {eu+pc}.')
            print(f'Sua jogada: \033[4m{eu}\033[m, jogada do PC: \033[4m{pc}\033[m')
            sequencia += 1
    else:
        # Se for par:
        if (eu + pc) % 2 == 0:
            print(f'VOCÊ \033[32mVENCEU!\033[m O total par foi: {eu + pc}.')
            print(f'Sua jogada: \033[4m{eu}\033[m, jogada do PC: \033[4m{pc}\033[m')
            sequencia += 1
        # Se for ímpar: 
        else:
            print(f'Você \033[31mPERDEU\033[m, o total ímpar foi: {eu + pc}.')
            print(f'Sua jogada: \033[4m{eu}\033[m, jogada do PC: \033[4m{pc}\033[m')
            break
print('-'*25)
print(f'A sua sequência de vitórias foi de: \033[97m{sequencia} vitórias seguidas\033[m')
print('''

FIM DO PROGRAMA''')