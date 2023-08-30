#desenvolva um programa que leia o comprimento de três retas e diga ao usuário se ele pode ou não formar um triângulo
reta1 = float(input('Valor da 1º reta:'))
reta2 = float(input('Valor da 2º reta:'))
reta3 = float(input('Valor da 3° reta:'))
print('-=-'*10)

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Com esses valores, se PODE ter um triângulo!')
else:
    print('Não será possível formar um triângulo.')
