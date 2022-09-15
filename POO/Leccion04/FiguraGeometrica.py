#Para definir una clase como abstracta se debe extender esta de otra clase:
#ABC = Abstract Base Class
from abc import ABC, abstractmethod #Separamos por coma varias clases del modulo abc

class FiguraGeometrica(ABC):
    def __init__(self, ancho, alto):
        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            self._ancho = 0
            print(f'Valor Erroneo Ancho: {ancho}')
        if self._validar_valor(alto):
            self._alto = alto
        else:
            self._alto=0
            print(f'Valor Erroneo Alto: {alto}')

    @property
    def alto(self):
        return self._alto

    @property
    def ancho(self):
        return self._ancho

#Quitar los setter para que los atributos sean de solo lectura, mejora a considerar
    @alto.setter
    def alto(self, alto):
        if self._validar_valor(alto):
            self._alto = alto
        else:
            print(f'Valor Erroneo Alto: {alto}')

    @ancho.setter
    def ancho(self, ancho):
        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            print(f'Valor Erroneo Ancho: {ancho}')

    def __str__(self):
        return f'Figura Geometrica: [Alto: {self._alto}, Ancho: {self._ancho}]'

    def _validar_valor(self, valor):
        return True if 0<valor<10 else False

#CLASES ABSTRACTAS EN PYTHON
#Contienen metodos abstractos que se usan para obligar a definir un metodo en las clases hijas
#un metodo abstracto no tiene implementacion
#cuando una clase tiene un metodo abstracto se denomina clase abstracta y no se puede crear instancias ni ubjetos de esta
#En primer lugar se debe definir la clase como abstracta y extenderla de otra (abc) (ver importaciones)
#En segundo lugar cramos el metodo abstracto

    @abstractmethod
    def calcular_area(self):
        pass

