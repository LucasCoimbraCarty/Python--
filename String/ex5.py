def verificador(x):
    palavra = x.split(' ')
    return len(palavra)

x = input('Digite algo: ')
print(verificador(x))