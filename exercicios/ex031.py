#  Desenvolva um programa que pergunte a distância de uma viagem em Km.
#  Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
dist = float(input('Digite a distância da viagem em Km: '))
print('Você está prestes a relizar uma viagem de {}Km!'.format(dist))
'''if dist <= 200:
    p = dist * 0.5
else:
    p = dist * 0.45'''
p = dist * 0.5 if dist <= 200 else dist * 0.45
print('E o preço da sua passagem será de R$ {:.2f}.'.format(p))


