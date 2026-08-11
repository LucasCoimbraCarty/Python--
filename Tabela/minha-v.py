import random

matriz = [(),
          (),
          (),
          (),
          ()]

def gerar(matriz):
    n = 0
    while n <= 5:
        matriz.append(random.randint(1, 20))
        n+= 1
    print(matriz)

def somar():
    pass

def menor_e():
    pass

def olhar():
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz[i][j], end="\t")
        print()

print('EXERCÍCIO 3 E 4 (19 MATRIZ)')
print('1 - Gerar Matriz | 2 - Somartório elementos diagonal | 3 - Menor número matriz | 4 - Olhar Matriz')
op = int(input("Digite o que quer fazer? "))

match op:
    case 1:
        gerar(matriz)
    case 2:
        pass