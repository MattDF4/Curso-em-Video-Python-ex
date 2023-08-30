salario = float(input('Qual o seu salario?: R$'))
aumento = (15*salario)/100
salaaum = salario + aumento
print(f'O funcionario que anteriomente ganhava R${salario:.2f}, recebeu um auemnto de R${aumento:.2f}(15%), pois então agora recebe: R${salaaum:.2f}.')
