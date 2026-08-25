def maior_menor_media(lista: list) -> tuple:
    maior = max(lista)
    menor = min(lista)
    media = sum(lista) / len(lista)
    return maior, menor, media        


lista = []
for i in range(10):
    n = int(input('Numero: '))
    lista.append(n)
print(lista)

resultado = maior_menor_media(lista)

print(f'Maior: {resultado[0]}')       
print(f'Menor: {resultado[1]}')
print(f'Média: {resultado[2]}')
