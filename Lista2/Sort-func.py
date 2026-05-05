'''
lista = [2,6,6,7,3,1,9,10,8,6]
lista_ord = []
num_max = max(lista) + 1
num_min = min(lista)

while num_min != num_max:
    for num in lista:
        if num_min >= num :
            lista_ord.append(num)
            #if lista[num] == :
            #lista_ord.pop(num)
    num_min += 1

    
print(f"A ordenação é {lista_ord}")
'''
lista = [2,6,6,7,3,1,9,10,8,6]

for i in range(len(lista)):
    for j in range(len(lista)):
        if lista[i] < lista[j]:
            x = lista[i]
            lista[i] = lista[j]
            lista[j] = x

print(lista)
