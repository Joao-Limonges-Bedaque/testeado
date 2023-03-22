#Crie uma função que recebe uma lista de string como parametro e retorna a string mais longa
def mais_Longa(a):
    b = []
    z = []
    for x in a:
        z.append(len(x))
    return print(a[z.index(max(z))])
c = ['ARARA','Aranca','Armada','torradeira','Baleira','outro','testando','teste','arapulcA','capacidades']
mais_Longa(c)