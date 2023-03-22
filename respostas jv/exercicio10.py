#Crie uma função que recebe uma lista de numeros como parametro e retorne o segundo menor numero da lista
def segundo_menor(a):
    c.sort()
    for x in c:
        if x > c[0]:
            print(x)
            break
c = [25093,423,444,444,13,13,1,1,1,1,0,0,9,44,4,4,1,1,1,1,0]
segundo_menor(c)