n = -1
while n < 0:
    n = int(input("O número limite para primo que você quer ver: "))

for i in range(3,n,2):
    if n % i == 0:
        print(i)