import random

Nr = random.randint(1, 10)
n = -1
c = 0

print('Joguinho Merda de número, você é obrigado a jogar, de 1 a 10')

while n != Nr:
    n = int(input('Digite um número, será que você acerta? '))
    if n > Nr:
        print('Número é menor')
    else:
        print('Número é maior')
    c += 1

print(f'Parabéns negro, acertou, foi {c} tentativas')