#ex6
notas = []
while True:
    Nt = float(input('Digite a nota dos alunos: '))

    if Nt < 0:
        break

print(f'A lista de notas é {notas}')
print(f'A lista e numerada é {enumerate(notas)}')