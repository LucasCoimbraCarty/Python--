lista = [2,6,6,7,3,1,9,10,8,6]

menor = lista[0]
maior = lista[0]

for num in lista:
    if menor > num:
        menor = num
    if maior < num:
        maior = num
    
print(f"O menor valor da lista é {menor}")
print(f"O maior valor da lista é {maior}")