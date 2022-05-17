nome = str(input('Digite seu nome completo: ')).strip()
#.strio() elimina os espaços antes de depois
print('Analisando seu nome...')
print('Seu nome em letras maiúsculas é: {}.'.format(nome.upper()))
print('Seu nome em letras minúsculas é: {}.'.format(nome.lower()))
print('Seu nome tem ao todo {} letras.'.format(len(nome) - nome.count(' ')))
#vai contar quantos espaços tem
#print('Seu primeito nome tem {} letras.'.format(nome.find(' ')))
#encontra no nome onde está o primeiro espaço, por isso diz quantas letras tem o primeiro nome
#Outra maneira de fazer:
separa = nome.split()
print ('Seu primeiro nome é {} e ele tem {} letras.'.format(separa[0], len(separa[0])))

