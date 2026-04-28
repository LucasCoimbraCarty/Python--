#ex5
import random

lista = []

for i in range(10):
    num = random.randint(1, 10)
    lista.append(num)

print(lista)

while True:
    esc = int(input('Digite um número e veremos quantas vezes ele está na lista: '))
    print(f'O número parece {lista.count(esc)}X')