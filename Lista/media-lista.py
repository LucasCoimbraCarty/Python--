
#Ex2
numero = []
pares = []
soma = 0
media = 0
for i in range(1,11,1):
    n = int(input(f'Digite {i}° número: '))
    media += n
    numero.append(n)
    if n % 2 == 0:
        soma += n
        pares.append(n)
    
print(f'Média aritmética {media/10}')
print(f'Soma pares {soma}')
