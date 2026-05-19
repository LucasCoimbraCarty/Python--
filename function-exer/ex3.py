import random

def dados():
    lista = [0,0,0,0,0,0]
    for i in range(1000):
        x = random.randint(1, 6)
        match x:
            case 1:
                lista[x - 1] += 1
            case 2:
                lista[x - 1] += 1
            case 3: 
                lista[x - 1] += 1
            case 4:
                lista[x - 1] += 1
            case 5:
                lista[x - 1] += 1
            case 6:
                lista[x - 1] += 1
    return lista

#Main
dado = dados()
for i in range(len(dado)):
    print(f"O número {i+1} apareceu {dado[i]} vezes")