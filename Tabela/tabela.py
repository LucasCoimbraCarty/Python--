linhas = int(input('Quantidade de linhas: '))
colunas = int(input('Quantidade de colunas: '))

matriz = []
for i in range(linhas):
    linhas = []
    for j in range(colunas):
        n = int(input('Número: '))
        linhas.append(n)
    matriz.append(linhas) #insere cada linha da matriz
print(matriz)