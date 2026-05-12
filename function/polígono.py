def validar_lado(lados):
    if lados < 3 or lados > 5:
        nota = print('VALOR INVÁLIDO')

def lado_num(lados):
    match lados:
        case 3:
            print('Triângulo')
        case 4:
            print('Quadrilátero')
        case 5:
            print('Pentágono')

Lad = int(input('Digite quantos lados tem a figura: '))
Lad = validar_lado(Lad)
Lad = lado_num(Lad)