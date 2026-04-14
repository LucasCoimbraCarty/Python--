n1 = int(input(f"Digite o 1° número: "))
nn = n1
nm = n1
for i in range(2,11,1):
    n1 = int(input(f"Digite o {i}° número: "))
    if n1 > nm :
        nm = n1
    elif n1 < nn:
        nm = n1

print(f'O maior número é {nm} e o menor é {nn}')