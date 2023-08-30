valorcasa = float(input('Diga o valor da casa: R$'))
salario = float(input('Diga o seu salario: R$'))
anos = int(input('Em quantos anos deseja pagar a casa?:'))
salario30 = (30*salario)/100
vmensal = valorcasa/(anos*12)
print('-='*20)

if vmensal <= salario30:
    print(f'\033[0;32mCOMPRA APROVADA!\033[m Você podera parcelar sua casa em |{anos*12}| veze de R${vmensal:.2f}.')
else:
    print(f'\33[0;31mCOMPRA NEGADA!\033[m Infelizmente,você não pode comprar a casa, pois 30% do seu salário (R${salario30:.2f}) é menor que a mensalidade.\nCustando: |R${vmensal:.2f}| cada parcela.')
