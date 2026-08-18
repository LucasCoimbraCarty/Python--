def cp():
    cp1 = float(input("Digite a Nota do Cp1: "))
    cp2 = float(input("Digite a Nota do Cp2: "))
    cp3 = float(input("Digite a Nota do Cp3: "))
    if cp1 < cp2 and cp1 < cp3:
        soma_cp = ((cp2 + cp3) / 2) * 0.2
    elif cp2 < cp1 and cp2 < cp3:
        soma_cp = ((cp1 + cp3) / 2) * 0.2
    elif cp3 < cp2 and cp3 < cp1:
        soma_cp = ((cp2 + cp1) / 2) * 0.2
    elif cp1 == cp2 and cp1 == cp3 and cp2 == cp3:
        soma_cp = ((cp2 + cp1) / 2) * 0.2
    print(soma_cp)
    return soma_cp

def sprint():
    sprint1 = float(input("Digite a Nota do Sprint1: "))
    sprint2 = float(input("Digite a Nota do Sprint2: "))
    soma_s = ((sprint1 + sprint2) / 2) * 0.2
    print(soma_s)
    return soma_s

def Gs():
    Gs = float(input("Digite a Nota da GS: "))
    Gs = Gs * 0.6
    print(Gs)
    return Gs

def semestre(gs_total,sprint_total,cp_total):
    soma_sem = gs_total + sprint_total + cp_total
    print(f"A média é {soma_sem}")
    return soma_sem

print("Média Fiap")

while True:
    op = int(input("1 - Cp | 2 - Sprint | 3 - Gs | 4 - Resultado | 5 - Sair \nDigite a opção: "))
    match op:
        case 1:
            cp_total = cp()
        case 2:
            sprint_total = sprint()
        case 3:
            gs_total = Gs()
        case 4:
            tudo = semestre(gs_total,sprint_total,cp_total)
        case 5:
            print('Obrigado por testar!')
            break;
        case _:
            print("Digite um valor válido")