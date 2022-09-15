# #HERENCIA EN PYTHON
# class Persona:
#     def __init__(self, nombre, edad):
#         self._nombre = nombre
#         self._edad = edad
#
#     @property
#     def nombre(self):
#         return self._nombre
#
#
#     @nombre.setter
#     def nombre(self, nombre):
#         self._nombre = nombre
#
#
#     @property
#     def edad(self):
#         return self._edad
#
#     @edad.setter
#     def edad(self, edad):
#         self._edad = edad
#
#
#
#     def mostrar_detalle(self):
#         print(f'Persona: {self._nombre} {self._edad}')
#
#     def __del__(self):
#         print(f'Eliminación de Persona: {self._nombre} {self._edad}')
#
#
# #Herencia simple, la clase padre se ubica entre parentesis, estando por defecto la clase Object,
# # mas adelante se vera la herencia multiple (se separa por comas los padres)
# class Empleado(Persona):
#     def __init__(self, nombre, edad, sueldo):
#         #super() = metodo que nos permite acceder a los metodos de la clase padre, hay q inicializar el/los padre(s)
#         #con los atributos requeridos por el/los padre(s)
#         super().__init__(nombre, edad)
#         self._sueldo = sueldo
#
#
#
# empleado1 = Empleado('Jhonsson', 28, 5000)
# print(empleado1.nombre)
# print(empleado1.edad)
# print(empleado1._sueldo)





#SOBREESCRITURA DEL METODO __str__
class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre


    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre


    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad



    def mostrar_detalle(self):
        print(f'Persona: {self._nombre} {self._edad}')

    def __del__(self):
        print(f'Eliminación de Persona: {self._nombre} {self._edad}')

    #REDEFINIENDO METODO DONDER SRT (__srt__())
    #sobreescritura del comportamiento
    def __str__(self):
        return f'Persona [Nombre: {self._nombre}, Edad: {self._edad}]'



class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self._sueldo = sueldo

    def __str__(self):
        return f'Empleado:[Sueldo:{self._sueldo}] {super().__str__()}'


