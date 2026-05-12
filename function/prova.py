# def valida_média(n1, n2):
#     while True:
#         media = (n1 + n2) / 2
#         if media < 6:
#             print('Reprovado!')
#             break
#         elif n1 < 0 or n2 < 0 or n1 > 10 or n2 > 10:
#             print('Digite uma nota válida')
#             n1 = float(input('Digite a 1° nota (0 a 10): '))
#             n2 = float(input('Digite a 2° nota (0 a 10): '))
#         else:
#             print('Aprovado')
#             break

# n1 = float(input('Digite a 1° nota: '))
# n2 = float(input('Digite a 2° nota: '))
# print(valida_média(n1, n2))

def validar_nota(nota):
    while nota < 0 or nota > 10:
        nota = float(input('Digite a 1° nota (0 a 10): '))
    return nota

def status(N1, N2):
    media = (N1 + N2) / 2 
    if media >= 6:
        print(f'Aprovado, sua média é {media}')
    else:
        print(f'Reprovado, sua média é {media}')

N1 = float(input('Informe a nota da 1° prova: '))
N1 = validar_nota(N1)

N2 = float(input('Informe a nota da 2° prova: '))
N2 = validar_nota(N2)

status(N1, N2)