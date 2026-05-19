op = 0
notas = [7]
aluno = ['g']

def menu(op):
    while op == 0:
        op = int(input("1. Cadastrar Aluno \n2. Registrar nota\n3. Calcular e exibir a média de um aluno\n4. Sair\nDigite a opção que deseja: "))
        match op:
            case 1:
                #função cadastrar
                pass
            case 2:
                #função registrar
                pass
            case 3:
                calcular_media(notas,aluno)
            case 4:
                print('Programa finalizado!')
                break
            case _:
                print('\n!Digite uma poção válida!\n')
                op = 0
        
def calcular_media(notas,aluno):
    soma = 0
    if notas == []:
        print('0')
    else:
        for i in notas:
            soma += i
        media = soma / len(notas)
        search = input("Digite o nome do aluno que desejá ver a média: ")
        if search in aluno:
            if media >= 6:
                print(f"Aprovado, Nota é {media}")
            elif media >= 4 and media <= 5.9:
                print(f"Exame, Nota é {media}")
            elif media < 4:
                print(f"Reprovado, Nota é {media}")
            return media

menu(op)