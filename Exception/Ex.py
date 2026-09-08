"""
Calcular a densidade de um material com base em sua massa e volume. Fórmula: densidade = massa / volume

- Obter as medidas (massa e volume)
- Calcular a densidade com base na fórmula acima restrições:
    - massa < 0 or volume < 0 | volume != 0

- Executar análise da densidade
    - função responsável por executar as funções dos itens 1 e 2
    - tratamento de exceções

"""

def obter_massa() -> float:
    massa = float(input("Massa do material: "))
    return massa

def obter_volume() -> float:
    volume = float(input("Volume do material: (em m³): "))
    return volume

def calcular_densidade(massa:float, volume:float) -> float:
    #validação
    if massa < 0 or volume < 0:
        raise ValueError("[ValueErro]: Massa e Volume não podem ser negativos")

    if volume == 0:
        raise ZeroDivisionError("[ZeroDivisionError]: O Volume do material não poder ser ZERO!")

    densidade = massa / volume

    return densidade

def executar_analise_densidade() -> None:
    try:
        massa = obter_massa()
        volume = obter_volume()

        calcular_densidade(massa, volume)
    except ValueError as erro:
        print(f'[ERRO FÍSICO]: {erro}')
        print(f'Divisão por Zero impede o cálculo da densidade')
    except ZeroDivisionError as erro:
        print(f'[ERRO FÍSICO]: {erro}')
        print(f'Divisão por Zero impede o cálculo da densidade')
    finally:
        print('--- Encerrando o ensaio ---')

while True:
    executar_analise_densidade()
    print('\n')