def verificador(palavra):
    cont = 0
    vogais = 'aeiou'
    for caraters in x:
        if caraters.lower() in vogais:
            cont += 1
    return palavra 


x = input('Digite algo: ')
print(verificador(x))