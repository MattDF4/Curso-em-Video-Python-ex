peso = float(input('Qual o seu peso?: KG '))
altura = float(input('Qual a sua altura?:'))
# IMC = PESO/ALTURA**2
imc = peso/(altura**2)
print('-='*22)

print('''        - CÁLCULO DE \033[97mIMC\033[m -
             TABELA:
| \033[34m18,5\033[m ou \033[34mmenos\033[m = \033[34mABAIXO DO PESO\033[m          |
| \033[34m18,6\033[m a \033[34m24,9\033[m   = \033[34mPESO IDEAL\033[m              | 
| \033[34m25,0\033[m a \033[34m29,9\033[m   = \033[34mLEVEMENTE ACIMA DO PESO\033[m |
| \033[34m30,0\033[m a \033[34m34,9\033[m   = \033[31mOBESIDADE Grau I\033[m        |
| \033[34m35,0\033[m a \033[34m39,9\033[m   = \033[31mOBESIDADE Grau II\033[m       |
| \033[34m40,o\033[m ou \033[34mMais\033[m  = \033[31mOBESIDADE MÓRBIDA\033[m       |''')

print('-='*22)

if imc <= 18.5:
    print(f'Seu \033[97mIMC\033[m é de: \033[97m{imc:.1f}\033[m, portanto você está \033[34mABAIXO DO PESO!')
elif imc >= 18.6 and imc <= 24.9:
    print(f'Seu \033[97mIMC\033[m é de: \033[97m{imc:.1f}\033[m, portanto você está no \033[34mPESO IDEAL!')
elif imc >= 25.0 and imc <= 29.9:
    print(f'Seu \033[97mIMC\033[m é de: \033[97m{imc:.1f}\033[m, portanto você está \033[34mLEVEMENTE ACIMA DO PESO!')
elif imc >= 30.0 and imc <= 34.9:
    print(f'Seu \033[97mIMC\033[m é de: \033[97m{imc:.1f}\033[m, portanto você está em \033[31mOBESIDADE Grau I!')
elif imc >= 35.0 and imc <= 39.9:
    print(f'Sei \033[97mIMC\033[m é de: \033[97m{imc:.1f}\033[m, portanto você está em \033[31mOBESIDADE Grau II!')
else:
    print(f'Seu \033[97mIMC\033[m é de: \033[97m{imc:.1f}\033[m, portanto você está em \033[31mOBESIDADE MÓRBIDA!')
