#Calculando descontos
n = float(input('Qual é o preço do produto?: R$'))
d = n * 0.05
p = n - d
print('O produto que custava R${:.2f}, está custando {:.2f}.'.format(n,p))