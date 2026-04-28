#Ex1
pares = []
impares = []
for i in range(1,11,1):
    n = int(input(f'Digite {i}° número: '))
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print(f'Números pares: {pares}')
print(f'Números impares: {impares}')