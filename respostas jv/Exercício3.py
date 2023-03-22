#Crie uma função que recebe uma lista de números como parâmetro e retorne o maior numero da lista
def maiorLista(a):
    print(f'O maior número digitado foi :   {max(a)}')
b = []
while True:
    c = int(input('Digite m número para adicionar a lista ou digite 0 para terminar a lista \n:     '))
    if c == 0 :
        break
    else:
        b.append(c)
maiorLista(b)