km = float(input('A quantos Km por hora o carro estava andando?:'))
if km >= 81:
    print(f'O carro ultrapssou o limte de velocidade(80km/h), portanto será multado em: R${(km-80)*7:.2f}.')
else:
    print('O carro estava dentro do limite de velocidade.')
