# Estrutura de dados (Coleção de dados)
# Definidas entre chaves {}
# Estrutura não ordena e não indexada 
Conjunto = {"Maçã", "Banana", "Manga"}
Conjunto = {"Maçã", "Banana", "Manga", "Banana"}
print(Conjunto)

#Conjuntos são heterogêneos
Conjunto = {"Fiap", 34, 50, True, "a", "a"}
print(len(Conjunto))
print(34 in Conjunto)
print(35 in Conjunto)
for i in Conjunto:
    print(i)

if 34 in Conjunto:
    print("Está contido")
else:
    print("Não está contido")

#Inserindo itens ao conjunto
#add()

nomes = {"Paulo", "Ana", "Pedro", "Maria"}
nomes.add("Antônio")
print(nomes)
nomes.remove("Paulo")
print(nomes)
nomes.discard("Ana")
print(nomes)

#Preenchendo conjuntos com input()
numeros = set()
for i in range(5):
    n = int(input('Número: '));
    numeros.add(n)
print(numeros)

x = {"Apple","Orange","Cherry"}
y = {"Google","Microsoft","Apple"}
print(x, y)

z = x.intersection(y) #ÚTIL PARA VERIFICAR SE EXISTE 1 ITENS IGUAL EM 2 LISTAS
print(z)

#difference 
z = x.difference(y) #ÚTIL PARA VERIFICAR SE EXISTE ITENS DIFERENTES EM 2 LISTAS
print(z)