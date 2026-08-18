"""
DOCSTRING
- Tem como objetivo explicar o funcionamento de uma função
- É um comentário sempre localizado na 1a linha de função
- Deve estar entre três aspas duplas
- Contribuir para a documentação de um código fonte e melhorar o seu entendimento

ANOTAÇÕES DE TIPO 
- Anotações de tipo(type hint) são utilizadas para indiciar os tipos de dados das variáveis (parâmetros das funções)
- Objetivo: Tornar o código mais legível e organizado
"""
def somar(a:float, b:float) -> float:
    """
    Esta função realiza a média soma de dois números do tipo float e retorna o resultado
    """
    return a+b

def media(a:int, b:int, c:int) -> float:
    """
    Esta função realiza a média aritmética de 3 números (int) e retorna o resultado
    """
    if type(a) == int and type(b) == int and type(c) == int:
        n = (a+b+c) / 3
        return
    else:
        print('Os valores devem ser do tipo int')
        return None

def entrada_dados() -> int:
    """
    Está função permite o usuário digitar um número e retorná-los
    """
    n = int(input('Número: '))
    return n 

#principal 
result = somar(5, 10)
print(f'Soma{result}')
n1 = entrada_dados()
n2 = entrada_dados()
n3 = entrada_dados()
result2 = media(n1,n2,n3)
print(f'Média: {result2}')