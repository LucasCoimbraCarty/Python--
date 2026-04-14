n = -1
x = 1
x2 = 0
while n < 0:
    n = int(input('Digite até onde você quer ver a sequência de Fibonacci: '))


for n in range(1,n-1,1):
    x = x + x2
    x2 = x2 + x
    print(f'{x} e {x2}')
    
print(f'O Resultado é {x}')