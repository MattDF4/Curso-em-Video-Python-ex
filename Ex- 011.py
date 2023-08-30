largura = float(input('Qual a largura da parede?:'))
altura = float(input('Qual a altura da parede?:'))
area = largura*altura
print(f'Sabendo que cada litro de tinta pode pintar 2m quadrados, e a área da parede é {area}, vou precisar de {area/2:.3f} litros de tinta.')
