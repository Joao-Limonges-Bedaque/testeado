#Crie uma função que recebe uma lista de numeros como parametro e retorne o numero de ocorrencia de um determinado numero da lista
def ocorencia(a,b):
    z = 0
    for x in a:
        if x == b:
            z = z+1
    return print(z)
c = [25093,423,444,444,13,13,1,1,1,1,0,0,9,44,4,4,1,1,1,1,0]
ocorencia(c,0)