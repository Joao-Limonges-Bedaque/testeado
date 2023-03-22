#Desenvolva o diagrama de classe e implementa em python, o seguinte caso:
'''
Uma classe tera um atributo 'Raio' e doi metodos : um para calcular a area do circulo e outro para calcular o perimetro (min 2 objetos)
'''
class circulo:
    def __init__(self,raio):
        self.raio = raio
    def perimetro(self):
        perimetro = self.raio * 2 *3.14
        print(f' o perímetro é {perimetro}')
    def area(self):
        area = 3.14*self.raio**2 
        print(f' a área é {area}')
c1 = circulo(1)
c2 = circulo(10)

c1.perimetro()
print('\n')
c2.perimetro()
print('\n')

c1.area()
print('\n')
c2.area()
print('\n')