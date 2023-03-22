#Desenvolva o diagrama de classe e implementa em python, o seguinte caso:
'''
Uma classe representa uma calculadora que realiza as operações basicas (adição, subtração, multiplicação e divisão),Criar no minimo dois objetos
'''
class calculator:
    def __init__(self,numero1,numero2):
        self.numero1 = numero1
        self.numero2 = numero2
    def soma(self):
        print(f'{self.numero1}  +  {self.numero2}  =  {self.numero1 + self.numero2}\n')
    def tira(self):
        print(f'{self.numero1}  -  {self.numero2}  =  {self.numero1 - self.numero2}\n')
    def multiplica(self):
        print(f'{self.numero1}  X  {self.numero2}  =  {self.numero1 * self.numero2}\n')
    def divide(self):
        print(f'{self.numero1}  ÷  {self.numero2}  =  {self.numero1/self.numero2}\n')
    def novo(self,numero1,numero2):
        self.numero1 = numero1
        self.numero2 = numero2
        print(f'Números trocados para {self.numero1} e {self.numero2}\n')
c1 = calculator(15,5)
c1.soma()
c1.tira()
c1.multiplica()
c1.divide()
c1.novo(20,4)
c1.soma()
c1.tira()
c1.multiplica()
c1.divide()