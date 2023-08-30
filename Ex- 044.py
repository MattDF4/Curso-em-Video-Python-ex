print('======== MERCADINHO - COMPRAS ========')
valort = float(input('Qual o valor total da compra?: R$'))

print('=='*19)

print('''
--------FORMAS DE PAGAMENTO--------
| \033[30m[1]\033[m À Vista Dinherio/Cheque     |
| \033[30m[2]\033[m À Vista Cartão              |
| \033[30m[3]\033[m 2x no Cartão                |
| \033[30m[4]\033[m 3x ou mais no cartão        |
-----------------------------------
''')

pagamento = int(input('Qual sua opção de pagamento?:'))
print('-'*10)

if pagamento != 1 and pagamento != 2 and pagamento != 3 and pagamento != 4:
    print('Opção \033[31mINVÁLIDA!')
elif pagamento == 1:
    print(f'\033[32mDESCONTO:\033[m 10%! \nPortando seu compra deu: \033[32mR${valort-((10*valort)/100)}.')
elif pagamento == 2:
    print(f'\033[32mDESCONTO:\033[m 5%! \nPortanto sua compra deu: \033[32mR${valort-((5*valort)/100)}.')
elif pagamento == 3:
    print(f'\033[32mDESCONTO:\033[m Não existe. \nValor total: \033[32mR${valort}\033[m. Parcelado em 2x, Preço por parcela: \033[32mR${valort/2:.2f}\033[m')
else:
    parcelas = int(input('Quantas vezes deseja parcelar?:'))
    print(f'Aplicando os \033[31m20% de juros\033[m;')
    print(f'VALOR A SER PAGO: \033[32mR${valort+(20*valort)/100}\033[m')
    print('-'*10)
    print(f'Parcelamento em {parcelas} parcelas;')
    print(f'Valor por parcela: \033[32mR${(valort+(20*valort)/100)/parcelas:.2f}')
