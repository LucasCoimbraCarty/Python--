"""
Exercício 1
Escreva um programa em Python para calcular o salário de um funcionário. Implemente um função calcular_salário,
e permite receber salário atual de um funcionário e retornar o salário com reajuste de aumento, sendo que:
- Caso o salário seja maior que R$2000, o funcionário recebrá 7% de aumento
- Caso contrário, o funcionário recebrá 15% de aumento
"""

def calcular_salário(v):
    if v >= 2000:
        v = v * 1.07
        print(f"Pelo bônus de 7% agora você receberá R${v}")
    else:
        v = v * 1.15
        print(f"Pelo bônus de 15% agora você receberá R${v}")

v = float(input("Digite o valor do seu salário: "))
calcular_salário(v)