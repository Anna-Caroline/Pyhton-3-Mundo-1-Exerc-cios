# Procurando uma string dentro de outra
#  Programa pra verificar se existe a palavra silva dentro do nome de uma pessoa
nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))
# in é um operador do python e não um método
