def somar(n1,n2):
    soma = n1 + n2
    print(f'A soma é {soma}')

def subtrair(n1,n2):
    subt = n1 - n2
    print(f'A subtração é {subt}')

def multiplicar(n1,n2):
    mult = n1 * n2
    print(f'A multiplicação é {mult}')

def divisão(n1,n2):
    div = n1 * n2
    print(f'A multiplicação é {div}')

def menu(op):
    while op == 0:
        print('\n 1 - Adição \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão \n 5 - Sair \n')
        op = int(input("Digite a opção que deseja: "))
        match op:
            case 1:
                somar(n1,n2)
            case 2:
                subtrair(n1,n2)
            case 3:
                multiplicar(n1,n2)
            case 4:
                divisão(n1,n2)
            case 5:
                break
            case _:
                print('\nDigite opção válida ')
                op = 0

op = 0
n1 = float(input('Digite o 1° número: '))
n2 = float(input('Digite o 2° número: '))

menu(op)
