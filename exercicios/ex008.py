medida = float(input('Digite uma distância em metros: '))
cm = medida * 100
mm = medida * 1000
#print('O valor em centímetros é igual a {}, \nE o valor em milímetros é igual a {}.'.format(cm,mm))
print('O valor em centímetros é igual a {:.0f}, \nE o valor em milímetros é igual a {:.0f}.'.format(cm,mm))
#mostra um número flutuante sem casas decimais :.0f