km = float(input('Quantos Kilometros foram percorridos com o carro?:'))
dias = int(input('Por quantos dias você ficou com o carro?:'))
vpkm = km*0.15
vpdi = dias*60
print(f'Somando os valores de Kilometros rodados e dias sobre a posse do veículo, os qiuais foram, respectivamente;')
print('-'*20)
print(f'Por  km: R${vpkm:.2f}.')
print(f'Por dia: R${vpdi:.2f}.')
print('-'*20)
print(f'O valor total à pagar será: R${vpdi+vpkm:.2f}')
