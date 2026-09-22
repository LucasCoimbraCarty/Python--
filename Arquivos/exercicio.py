# 1

with open('ips.txt', 'r') as arquivo1, open('ips_unicos.txt', 'w') as arquivo2:
    lista = arquivo1.readlines()
    conjunto = set(lista)
    arquivo2.writelines(conjunto)

#2

with (open('notas.txt', 'r', encoding='utf-8') as arquivo,
      open('aprovados.txt', 'w', encoding='utf') as aprovados,
      open('reprovados.txt', 'w', encoding='utf-8') as reprovados):

    for linha in arquivo:
        lista = linha.split(',')        # lista com dados do aluno
        notas = lista[2:]               # lista apenas com as notas

        soma = 0                        # somatorio das notas
        for n in notas:
            soma += float(n)
        media = soma / 4

        if media >= 6:                  # escreve nos arquivos
            aprovados.write(f'{lista[0]},{lista[1]},{media:.2f}\n')
        else:
            reprovados.write(f'{lista[0]},{lista[1]},{media:.2f}\n')
 
#3 

with (open('foods.txt', 'r', encoding='utf-8') as arquivo):
    dicionario = {}
    for linha in arquivo:
        lista = linha.replace('\n', '').split(',')
        print(lista)
        if lista[2] in dicionario:
            dicionario[lista[2]] += 1
        else:
            dicionario[lista[2]] = 1
    print(dicionario)

    maior = 0
    nome = ''
    for chave, valor in dicionario.items():
        if valor > maior:
            maior = valor
            nome = chave
    print(f'{nome} - {maior}')