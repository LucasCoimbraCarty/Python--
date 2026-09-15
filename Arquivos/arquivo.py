arquivo = open('arquivo.txt', 'r')

# texto = arquivo.read()
# print(texto)

for linha in arquivo:
    print(linha)

arquivo = open('arquivo.txt', 'w')

# arquivo.write('Este texto deverá ser escrito e arquivado \n')

nome = input('Digite seu nome: ')
arquivo.write(nome + '\n')

idade = int(input('Digite sua idade: '))
arquivo.write(str(idade) + '\n')

arquivo = open('nomearquivo.txt','a')

arquivo.write("Este texto será escrito no arquivo\n")

arquivo.close()

with open('arquivo.txt', 'r') as arquivo:
    for linha in arquivo:
        print(linha)

print('Fechado e Aberto')

with open('arquivo.txt', 'r', encoding='utf-8') as arquivo: #Tratar caracteres
    for linha in arquivo:
        print(linha)