#Ex3
import random

num = []
soma = 0

for i in range(1,21,1):
    n = random.randint(1,50)
    num.append(n)
    soma += n

print(f'Lista dos números sorteados são {num}')
print(f'Soma de todos os números é {soma}')
print(f'O menor número da lista é {min(num)}')
print(f'O maior número da lista é {max(num)}')