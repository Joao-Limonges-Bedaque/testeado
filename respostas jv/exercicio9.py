#Crie uma função que recebe uma lista de numeros como parametro e retorne uma lista com apenas numeros menores que 10
def menor_10(a):
    z = []
    for x in a:
        if x < 10:
            z.append(x)
    return print(z)
c = [25093,423,444,444,13,13,1,1,1,1,0,0,9,44,4,4,1,1,1,1,0]
menor_10(c)