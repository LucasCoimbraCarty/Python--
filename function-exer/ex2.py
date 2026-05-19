def triangular(num):
    i = 1
    while True:
        if i*(i+1)*(i+2) == num:
            return True
        elif i*(i+1)*(i+2) > num:
            return False
        i += 1
#Main
N = int(input("Informe um número para verificar se é triangular: "))
if triangular(N):
    print(f"O número {N} é triangular! ")
else:
    print(f"O número {N} não é triangular! ")