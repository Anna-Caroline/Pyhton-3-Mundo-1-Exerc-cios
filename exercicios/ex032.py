# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from datetime import date
ano = int(input('Que ano você quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
# Número divisível por 4, então o ano é bissexto
# exceção do ano 1700 e 1900 que não eram bissextos apesar de serem divisíveis por 4
# exceto em anos múltiplos de 100 que não são múltiplos de 400
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} é bissexto.'.format(ano))
else:
    print('O ano de {} não é bissexto.'.format(ano))

