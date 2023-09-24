print('-=-' * 10)
print('ESCOLA GENERAL')
print('APROVEITAMENTO DO ALUNO')
print('-=-' * 10)

nota1 = float(input('Sua pirmeira nota: '))
nota2 = float(input('Sua segunda nota: '))
media = (nota1 + nota2) / 2
print('-' * 20)
print('MEDIA: {}'.format(media))
if media >= 9:
    print('APROVEITAMENTO A')
else:
    if (media >= 8) and (media < 9):
        print('APROVEITAMENTO B')
    else:
        if (media >= 7) and (media < 8):
            print('APROVEITAMENTO C')
        else:
            if (media >= 6) and (media < 7):
                print('APROVEITAMENTO D')
            else:
                if (media >= 5) and (media < 6):
                    print('APROVEITAMENTO E')
                else:
                    print('APROVEITAMENTO F')

print('_' * 20)
