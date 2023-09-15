#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
#O programa será interrompido quando o número solicitado for negativo.
v = c = 0
while True:
    print('-'*20)
    v = int(input('Valor para tabuada: '))
    if v < 0:
        print('FIM DO PROGRAMA.')
        break
    else:
        while c < 10:
            c += 1
            print(f'{c}x{v}= {c*v}')
    c = 1
