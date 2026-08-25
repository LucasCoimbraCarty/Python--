tupla = (2,'a',4,5,5)
print(tupla)

# tupla[0] = 10 vai dar erro se tentar isso
# print(tupla)

tupla = (3,10,9,111,12)
print(tupla[1:3])

tupla = (1,2,3)
lista = list(tupla)
print(lista)

tupla_l = tuple(lista)
print(tupla_l)

def soma (a,b):
    c = a+b
    d = a*b
    return c, d

x = soma(10,15)
print(x)
# x[0] = 10 vai dar erro porque é uma tupla, não pode ser alterada
