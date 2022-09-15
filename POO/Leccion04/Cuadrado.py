from Color import Color
from FiguraGeometrica import FiguraGeometrica

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        #super().__init__(lado)#el metodo super llama a los metodos de la clase padre pero en este caso lo hace al primero que encuentra de izquierda a derecha
        #una forma adecuada para herencia multiple (metodos de clases padre) es hacer lo siguiente
        FiguraGeometrica.__init__(self, lado, lado)#inicializa los atributos de la clase padre FiguraGeometrica
        Color.__init__(self, color)#inicializa los atributos de la clase padre Color

    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)}, {Color.__str__(self)}'

    def calcular_area(self):
        return self.alto * self.ancho