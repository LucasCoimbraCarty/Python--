alunos = {}

for i in range(5):
    ra = input('Informe o RA: ')
    nome = input('Informe o Nome: ')
    alunos[ra] = nome

print(alunos)

notas = {'123': [8,6,5,9.8],
         '336': [7,6,5.5,10],
         '199': [6,8,9,0]}

print(notas['123'])
print(notas['123'][0])


rm_aluno = {}

for i in range(5):
    rm = input('Digite rm: ')
    notas_rm = []
    for j in range(6):
        n = float(input('Insira nota'))
        notas_rm.append = []
    rm_aluno[rm] = notas_rm
