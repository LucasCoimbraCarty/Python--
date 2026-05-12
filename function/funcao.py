# def par_ou_impar(numero):
#     if numero % 2 == 0:
#         print('Par')
#     else:
#         print('Impar')

# #Main
# N = int(input('Informe o número: '))
# par_ou_impar(N)

def calcular_area(base, altura):
    area = (base * altura) / 2
    return area

#Main
base = float(input('Informe a base: '))
altura = float(input('Informe a altura: '))
A = calcular_area(base, altura)
print(f'Área do triângulo: {calcular_area(base, altura)}')