import requests

'''
1) Obter CEP
2) Receber o CEO (1) e realizar a requisição
3) Imprimir os dados recebidos
'''

def main():
    escolher_cep()

def escolher_cep():
    cep = input('Digite um Cep:') #01538001
    url = f'https://viacep.com.br/ws/{cep}/json/'
    requisicao(url)

def requisicao(url):
    try:
        requisicao = requests.get(url)

        if requisicao.status_code == 200:
            resposta_json = requisicao.json()

            print(f'Cep: {resposta_json['cep']}')
            print(f'Logradouro: {resposta_json['logradouro']}')
            print(f'Complementos: {resposta_json['complemento']}')
            print(f'Bairro: {resposta_json['bairro']}')
            print(f'Localização: {resposta_json['localidade']}')
            print(f'Estado: {resposta_json['estado']}')

        elif requisicao.status_code == 404:
            print('Não foi possível encontrar o endereço!')

        elif requisicao.status_code == 500:
            print('Ocorreu algum erro no Servidor!')

        else:
            print(requisicao.status_code)

    except ConnectionError as exp:
        print(f'Houve um erro de conexão \n{exp}')
    except Exception as exp:
        print(f'Erro..boa! \n{exp}')

if __name__ == "__main__":
    main()