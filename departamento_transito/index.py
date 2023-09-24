print('-=-' * 10)
print('DEPARTAMENTO DE TRANSITO')
print('-=-' * 10)
nome = str(input('Seu nome completo: ')).strip().title()
ano_atual = int(input('Qual o ano atual ? '))
nasc = int(input('Qual ano de nascimento ? '))
idade = ano_atual - nasc
if idade >= 18:
    print('-=-' * 8)
    print('Nome: {}'.format(nome))
    print('Idade: {} anos'.format(idade))
    print('APTO para tirar a carteira de motirista.')
    print('-=-' * 8)
else:
    print('-=-' * 8)
    print('Nome: {}'.format(nome))
    print('Idade: {}'.format(idade))
    print('INAPTO para tirar a carteira de motorista')
    print('-=-' * 8)
