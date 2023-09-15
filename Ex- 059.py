#Crie um programa que leia dois valores e mostre um menu na tela:
valorp = float(input('Diga o priemiro valor:'))
valors = float(input('Diga o segundo valor:'))
subt = 0
divisao = 0
soma = valors + valorp
if valorp > valors:
    divisao = valorp/valors
    subt = valorp - valors
elif valors > valorp:
    divisao = valors/valorp
    subt = valors - valorp
else:
    divisao = valors/valorp
    subt = valors - valorp
multi = valors * valorp
print('''
-------------------------------
| Escolha:                    |
| [1] Para SOMAR              |
| [2] Para SUBTRAIR           |
| [3] Para DIVIDIR            |  
| [4] Para MULTIPLICAR        |
| [5] Para trocar de números  |
| [6] Sair do programa.       |
-------------------------------''')
print('')
escolha = 0
while escolha != 6:
    escolha = int(input('Escolha uma opção:'))
    if escolha == 1:
        print(f'A soma entre os valores resulta em: \033[97m{soma}\033[m')
        print('-'*20)
    elif escolha == 2:
        print(f'A subtração entre os valores resulta em: \033[97m{subt}\033[m')
        print('-'*20)
    elif escolha == 3:
        print(f'A divisão entre os valores resulta em: \033[97m{divisao:.2f}\033[m')
        print('-'*20)
    elif escolha == 4:
        print(f'A multiplicação entre os valores resulta em: \033[97m{multi}\033[m')
        print('-'*20)
    elif escolha == 5:
        valors = float(input('Digite o primeiro valor:'))
        valorp = float(input('Digite o segundo valor:'))
        print('-'*20)
    else:
        print('Opção inválida, tente novamente')
        print('')
print('FIM DO PROGRAMA.')
