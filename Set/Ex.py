""" Ex1 - Criar e manipular Sets() 
    Crie dois conjuntos de sets, um com números pares e outro com números ímpares. Os números deve variar de 1 a 10

    Ex 2 - Remover Duplicatas
    Dada uma lista com alguns elemntos duplicados, converta a lista em uma set para remover duplicatas e depois converta de volta para
    a lista

    Exe3 - Contar elementos únicos
    Dada uma lista com vários elements (alguns duplicados), crie um set a partir desta lista e conte a quantidade de elementos únicos
"""
x = {}
z = {}
for i in range(1,10,2):
    x = {i}
    print(x)

for i in range(0,10,2):
    z = {i}
    print(z)

lista = ("a","a",1,"ni","ger")
lista = set(lista)
lista = list(lista)
print(lista)

lista2 = ("b","b",1,"ni","ger")
