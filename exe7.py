from forex_python.converter import CurrencyRates

c = CurrencyRates()

real = float(input('Digita um valor em real: '))
dolar = c.convert('BRL', 'USD',real)
print('Esse valor em dolar será: {:.2f} '.format(dolar))
