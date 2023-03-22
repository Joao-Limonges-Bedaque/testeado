#11 - CRIE UMA FUNÇÃO QUE RECEBE UMA LISTA DE NÚMEROS COMO PARÂMETRO E RETORNE A MÉDIA DOS NÚMEROS.

def media(a):
    media =0
    cont = 0
    for x in a:
        media += x
        cont +=1
    print(f'a media dos numeros é {media/cont}')
c = [12,6,6,18,18,9,12,15,20,4]
media(c)