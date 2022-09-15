from Cuadrado import Cuadrado
from FiguraGeometrica import FiguraGeometrica
from Rectangulo import Rectangulo


print('Creación de objeto Cuadrado'.center(50, '-'))

cuadrado1 = Cuadrado(lado=5, color='rojo')
cuadrado1.alto=9
cuadrado1.ancho=9
# print(cuadrado1.ancho)
# print(cuadrado1.ancho)
# print(cuadrado1.color)
print(f'Calculo del area de un cuadrado: {cuadrado1.calcular_area()}')



#MRO - Method Order Resolution en Python
#Cuando se utilizan Herencia multiple es importante llevar un orden en la inicializacion de las clases padre
#Permite conocer la jerarquia de clases
#print(Cuadrado.mro()) #el metodo ".mro()" permite conocer el orden de acceso a las clases
# padre (orden establecido al definir la clase hija Cuadrado en este caso - class Cuadrado(FiguraGeometrica, Color):)


print(cuadrado1)



print('Creación de objeto Rectángulo'.center(50, '-'))
rectangulo1 = Rectangulo(ancho=9, alto=8, color='Verde')
rectangulo1.ancho=9
rectangulo1.alto=15
print(f'Cálculo del area del rectangulo: {rectangulo1.calcular_area()}')
#print(Cuadrado.mro())
print(rectangulo1)


#CLASES ABSTRACTAS EN PYTHON
#prueba de clase abstracta:
#la siguiente linea da error, no se puede instanciar una clase abstracta
#figura = FiguraGeometrica() #TypeError: Can't instantiate abstract class FiguraGeometrica with abstract method calcular_area

#Method Resolution Order modificado a razon de la herencia de ABM definido en la clase Figurageometrica
print(Cuadrado.mro())