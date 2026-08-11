import random

def preencher_matriz(linhas, colunas):
    matriz = []
    for i in range (linhas):
        aux = []
        for j in range (colunas):
            aux.append(random.randint(1, 20))
        matriz.append(aux)
    return matriz

def exibir_matriz(matriz):
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[0])):
            print(matriz[linha][coluna], end="\t")
        print()

def diagonal_principal(matriz):
    total = 0
    i = 0
    j = 0
    while i < len(matriz):
        total += matriz[i][j]
        i += 1
        j += 1
    return total 


linhas = 5
colunas = 5
m = []
m = preencher_matriz(linhas, colunas)
exibir_matriz (m)

print(f"O somatório dos valores da diagonal principal dessa matriz é: {diagonal_principal(m)}")