# arquivo = open("exemplo.txt","w",encoding='utf-8')

# arquivo.write("Olá, esse é um arquivo")
# arquivo.close()

with open("exemplo.txt","a",encoding='utf-8') as arquivo:
    arquivo.write("Esse Texto deve aparecer no final do arquivo.")
    arquivo.write('Esse texto está grudado no inteiror. \n')

with open("D:\\Python\\Python--","a",encoding='utf-8') as arquivo:
    arquivo.write("Esse Texto deve aparecer no final do arquivo.")
    