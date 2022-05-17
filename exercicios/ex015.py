#Aluguel de carros
n = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos quilômetros rodados? '))
r = 60*n + 0.15*km
print('O valor a ser pago é de {}'.format(r))
