vproduto = float(input('Qual o preço desse produto? R$'))
desconto = (5*vproduto)/100
aumento = (12*vproduto)/100
valorf = vproduto - desconto
print(f'Este produto, que originalmente custava R${vproduto:.2f}, recebeu uma oferta de 5% de desconto se o pagamento for à vista e passou a custar:R${valorf:.2f}')
print(f'Caso o pagamento seja parcelado, haverá um aumento de 12%, sendo assim o preço será: R${vproduto+aumento:.2f}.')
