n1 = float(input('Digite a 1º nota:'))
n2 = float(input('Digite a 2º nota:'))
nota = (n1+n2)/2
print('-='*15)
print('CALCULANDO A MÉDIA')
print('-='*15)
print('''|  MÉDIA: 6.0   |
| RANK DE NOTAS |
|\033[0;36m EXCELENTE\033[m   = 9.0 até 10.0 |
|\033[0;32m ÓTIMA\033[m       = 7.0 até 8.9  |
|\033[0;34m NA MÉDIA\033[m    = 6.0 até 6.9  |
|\033[0;31m RECUPERAÇÃO\033[m = 0.0 até 5.9  |''')
print('-='*15)
if nota >= 7 and nota <= 8.9:
    print(f'Você teve uma \033[0;32mÓTIMA\033[m nota. |\033[0;32m{nota:.1f}\033[m|')
elif nota >= 6 and nota <= 6.9:
    print(f'Você teve uma nota \033[0;34mNA MÉDIA\033[m; |\033[0;34m{nota:.1f}\033[m|')
elif nota <= 5.9:
    print(f'Sua nota não foi susficiente, ficou de \033[0;31mRECUPERAÇÃO.\033[m Nota: |\033[0;31m{nota:.1f}\033[m|')
elif nota >= 9:
    print(f'\033[0;36mPARABÉNS!\033[m Sua nota foi \033[0;36mEXCELENTE!\033[m |\033[0;36m{nota:.1f}\033[m|')
