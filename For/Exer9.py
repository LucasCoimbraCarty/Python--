n = -1
x = 0
while n < 0:
    n = int(input('Digite um número para ser fatorado: '))
    x = n
    
for n in range(n-1,1,-1):
    x = x * n

print(x)