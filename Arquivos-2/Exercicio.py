import json
# Exercício 1

# with open('notas.txt','r',encoding='utf-8') as arquivo:
#     alunos = {}
#     for linha in arquivo:
#         dados = linha.split(",")
#         cod = dados[0]
#         nome = dados[1]
#         notas = [float(dados[2]),float(dados[3]),float(dados[4]),float(dados[5])]
#         alunos[cod] = {'Nome': nome, 'Notas': notas}
#     json_converte = json.dumps(alunos, indent=4, ensure_ascii=False)

# with open('notas.json','w',encoding='utf-8') as arquivojson:
#     arquivojson.write(json_converte)

# Exercício 2

# with open('foods.txt','r',encoding='utf-8') as arquivo:
#     usuario = {}
#     for linha in arquivo:
#         dados = linha.split(",")
#         id = dados[1]
#         nome = dados[0]
#         comida = dados[2]
#         usuario[id] = {'Nome': nome, 'Comida': comida}
#     json_converte = json.dumps(usuario, indent=4, ensure_ascii=False)

# with open('foods.json','w',encoding='utf-8') as arquivojson:
#     arquivojson.write(json_converte)

# Exercício 3
with open('heroes.json','r',encoding='utf-8') as arquivo:
    conve = json.load(arquivo)

    lista = conve["members"]

    for heroi in lista:
        lista_pod = heroi['powers'] 

        if 'Flight' in lista_pod:
            print(f'Nome: {heroi['name']}')
            print(f'Poderes: {lista_pod}')
            print('\n')