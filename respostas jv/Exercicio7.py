#Crie uma função que recebe uma lista de numeros como parametro e retorne uma lista om apenas os nusmeros impares
def lista_Par(a):
    b = []
    for x in range(len(a)):
        if (a[x] % 2) != 0:
            b.append(a[x])
    return print(b)

c = [10,62,32,99,13,14,66,45,94723,75,231,7,43,100]
lista_Par(c)