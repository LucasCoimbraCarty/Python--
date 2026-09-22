# Exercicio 1
# with open('XDDDD.txt', 'w', encoding='utf-8') as arquivo:
#     for i in range(10):
#         num = int(input("Digite um número: "))
#         arquivo.write(f"{num}\n")

# Exercicio 2
# totalT = 0
# with open('XDDDD.txt', 'r', encoding='utf-8') as arquivo:
#     for linha in arquivo:
#         totalT += int(linha)
#     print(totalT)

# Exercicio 3 
# with open('infinito.txt', 'w', encoding='utf-8') as arquivo:
#     while num != 0:
#         num = int(input("Digite um número: "))
#     print('Adicionar 0 finalizou o programa!\n')

# Exercicio 4
while True:
    num = int(input("Digite um número: "))
    par_ver = num % 2
    if num == 0:
        print('Adicionar 0 finalizou o programa!\n')
        break;
    if par_ver == 0: 
        with open('par.txt', 'a', encoding='utf-8') as arquivo:
            arquivo.write(f'{num} \n')
    else:
        with open('impar.txt', 'a', encoding='utf-8') as arquivo:
            arquivo.write(f'{num} \n')

# Exercicio 5

ar_par = open('par.txt', 'r', encoding='utf-8')
ar_im = open('impar.txt', 'r', encoding='utf-8')
for linha in ar_par:
    n = ar_par.read()
    print(n)
# x = ar_im.read()

# print(type(n))