# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%
s = float(input('Qual o salário do funcionário? R$'))
if s >= 1250:
    aumento = s + s * 0.1
else:
    aumento = s + s * 0.15
print('Quem ganhava R$ {:.2f}, passa a ganhar R$ {:.2f}.'.format(s, aumento))
