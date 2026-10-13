import requests
url = f'https://dummyjson.com/recipes?limit=50'

try:
    resposta = requests.get(url, verify=False)

    if resposta.status_code == 200:
        ing_busca = input('Ingrediente: ')

        dicionario = resposta.json()

        lista_receitas = dicionario['recipes']

        for receita in lista_receitas:
            lista_ingredientes = receita['ingredients']
            for ingrediente in lista_receitas:
                if ing_busca.lower() in ingrediente.lower():
                    print('-'*50)
                    print(receita['name'])
                    print(receita['ingredients'])

except Exception as erro:
    print(f'Erro, {erro}')