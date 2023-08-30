from math import hypot, pow
cateto1 = float(input('Digite o primeiro cateto:'))
cateto2 = float(input('Digite o segundo cateto:'))
hipoten = hypot(cateto1, cateto2)
print(f'A soma dos catetos ao quadrado ({pow(cateto1,2):.2f} e {pow(cateto2,2):.2f}), resultará em: \n\nHipotenuza: {hipoten:.2f}')
