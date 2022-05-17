#Conversor de moedas (real para dólar)
# 1 dólar vale 4,70 euro 5,08, libra 6,14
n = float(input('Digite quanto você tem na sua carteira: R$'))
dolar = n / 4.7
euro = n / 5.08
libra = n / 6.14
print('Com R$ {:.2f}, você consegue comprar: \n$ {:.2f} dólares, \n€ {:.2f} euros, \n£ {:.2f} libras esterlinas.'.format(n, dolar, euro, libra))
# {:.2f} com apenas duas casas decimais flutuantes

