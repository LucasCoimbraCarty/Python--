import math

def bhaskara(a,b,c):
    if a == 0:
        if b == 0:
            print("Não Possui raiz!")
        else:
            print(f"A raiz é {-c/b}")
    elif b == 0:
        delta = -4*a*c
        x = math.sqrt(delta)
        print(f"A raíz é {x/(2*a)}")
    elif c == 0:
        raiz1 = (-b + math.sqt(b**2)) / (2*a)
        raiz2 = (-b + math.sqt(b**2)) / (2*a)
        print(f"As raizés são {raiz1} e {raiz2}")
    else:
        delta = b**2 - 4*a*c
        x = math.sqrt(delta)
        raiz1 = (-b + x) / (2*a)
        raiz1 = (-b + x) / (2*a) 
#Main
a = float(input('Digite o valor de A: '))
b = float(input('Digite o valor de B: '))
c = float(input('Digite o valor de C: '))
bhaskara(a,b,c)