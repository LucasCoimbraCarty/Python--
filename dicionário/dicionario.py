dicionar = {'nome': 'Lucas',
            'idade': 18,
            'estado': 'São Paulo'}

dicionar['idade'] = 19
print(dicionar)
print(dicionar['nome'])

dicionar['cidade'] = 'São Paulo' # Novo valor
dicionar.pop('estado') # exclusão
print(dicionar)

# Inserir e criar dicionários
# fruta = {}
# chave = input('Digite nome: ')
# valor = float(input('Digite o valor da fruta: '))
# fruta[chave] = valor
# print(fruta)

for n in dicionar.keys():
    print(n) # exibe todos as chaves

for n in dicionar.values():
    print(n) # exibe todos os valores

for k, v in dicionar.items():
    print(k,v) # exibe todos os items

if 'Gabriel' in dicionar:
    print('A chave existe no dicionário')
else:
    print('A chave não existe')

alunos = {}