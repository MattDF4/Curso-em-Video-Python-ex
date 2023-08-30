km = int(input('Quantos Km serão rodados na viagem?:'))
if km <= 200:
    print(f'Você irá desembolsar cerca de: R${km*0.50:.2f}')
else:
    print(f'Então você irá pagar: R${km*0.45:.2f}')
