salario = float(input('Diga o valor do seu salário: R$'))
print('-'*35)

if salario >= 1250:
    print(f'Você receberá um aumento de 10%!, ou seja, seu salário agora é: R${(10*salario)/100+salario:.2f}')
else:
    print(f'Portanto você receberá um aumento de 15%; recebendo agora: R${(15*salario)/100+salario:.2f}')
