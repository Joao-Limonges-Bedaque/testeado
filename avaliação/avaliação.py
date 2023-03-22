#Desenvolva o diagrama de classe e implementa em python, o seguinte caso:
'''
Uma classe chamada "pessoa" que terá os seguintes atributos : nome,idade e altura. Alem diso, teremos um método chamado "imprimir_informacoes" que irá imprimir os valores dos
atributos da pessoa na tela (min 2 objetos).
'''
class pessoa:
    def __init__(self,nome,idade,altura):
        self.nome = nome
        self.idade = idade
        self.alura = altura
    def imprimir_informacoes(self):
        print(f'O nome da pessoa é {self.nome}')
        print(f'Sua idade é {self.idade}')
        print(f'sua altura é {self.alura}')
p1 = pessoa('Glória',16,1.65)
p2 = pessoa('Zilmar',16,1.76)
print('\n')
p1.imprimir_informacoes()
print('\n')
p2.imprimir_informacoes()