numero = int(input('Digite um número inteiro:'))
print('-='*10)
print('[1] Para BINÁRIO')
print('[2] Para OCTAL')
print('[3] Para HEXADECIMAL')
print('-='*10)
escolha = int(input('Diga a sua escolha:'))
print('-'*10)
if escolha == 1:
    print(f'Convertendo |{numero}| para BINÁRIO temos: \033[0;34m{bin(numero)[2:]}')
elif escolha == 2:
    print(f'Convertendo |{numero}| para OCTAL temos: \033[0;34m{oct(numero)[2:]}')
elif escolha == 3:
    print(f'Convertendo |{numero}| para HEXADECIMAL temos: \033[0:34m{hex(numero)[2:]}')
else:
    print('Escolha \033[0;31mINVÁLIDA.')
