celsius = float(input('Diga a temperatura em °C:'))
print('='*30)
print(f'Passando essa temperatura ({celsius}°C) para fahrenheit e para Kelvin, teremos:')
print('='*30)
print(f'Fahrenheit: {celsius*1.8+32:.1f}°F.')
print('-'*20)
print(f'Kelvin:     {celsius+273:.1f}°K.')
print('='*30)