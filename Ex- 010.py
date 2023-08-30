reais = float(input('Quantos reais você possui?: R$'))
dolar = reais/4.78
euros = reais/5.32
libras = reais/5.14
print(f'Com essa quantidade de reais (R${reais:.2f}), você poderá comprar cerca de: \nU${dolar:.2f} dólares. \n€${euros:.2f} Euros.  \n£${libras:.2f} Libras.')
