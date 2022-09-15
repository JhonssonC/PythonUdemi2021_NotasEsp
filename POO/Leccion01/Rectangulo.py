# class Rectangulo:
#     '''
#     Clase que permite generar objetos rectangulos
#     '''
#     def __init__(self, area = 0):
#         self.base = int(input('Proporciona la base: '))
#         self.altura = int(input('Proporciona la altura: '))
#
#     def calcular_area(self):
#         self.area = self.base * self.altura
#         print(f'Área rectángulo: {self.area}')
#
#
# mirectangulo = Rectangulo()
# mirectangulo.calcular_area()


class Rectangulo:
    '''
    Clase que permite generar objetos rectangulos
    '''
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        self.area = self.base * self.altura
        return self.area

base = int(input('Proporciona la base: '))
altura = int(input('Proporciona la altura: '))
mirectangulo = Rectangulo(base, altura)
print(f'Área rectángulo: {mirectangulo.calcular_area()}')

base = int(input('Proporciona la base: '))
altura = int(input('Proporciona la altura: '))
mirectangulo2 = Rectangulo(base, altura)
print(f'Área rectángulo: {mirectangulo2.calcular_area()}')