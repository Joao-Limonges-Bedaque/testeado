#Crie uma função que recebe uma lista de palavras como parâmetro e retorne uma lista com palavras que começam com a letra "A"
def procura_A(a):
    b = []
    for x in a:
        z = []
        for y in x:
            z.append(y)
        if z[0] == 'A' or z[0] == 'a':
            b.append(x)
    return print(b)
c = ['ARARA','Aranca','Armada','torradeira','Baleira','outro','testando','teste','arapulcA','capacidade']
procura_A(c)