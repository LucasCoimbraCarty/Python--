"""
lista = [1,2,3,4,5]

lista[1] = "Cassio"

lista.insert(2,'Xd')

print(lista)

lista.pop(3)

print(lista)

for item in lista:
    print(item)

numeros = []
for i in range(5): # preencher lista com 5 itens
    n = int(input('Informe um Número: '))
    numeros.append(n) # insere número na lista
print(numeros)
"""

numeros = []
while True:
    n = int(input('Informe um Número: '))
    if n == 0:
        break
    numeros.append(n)
print(numeros)