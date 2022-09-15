class Cubo:
    """
    Clase para Crear Cubos
    """
    def __init__(self, base, altura, profundidad):
        self.base = base
        self.altura = altura
        self.profundidad = profundidad

    def calcular_area(self):
        return self.altura*self.base*self.profundidad


ancho = int(input('Proporciona el ancho: '))
alto = int(input('Proporciona el alto: '))
profundo = int(input('Proporciona lo profundo: '))
cubo1 = Cubo(ancho, alto, profundo)
print(f'Volúmen cubo: {cubo1.calcular_area()}')
