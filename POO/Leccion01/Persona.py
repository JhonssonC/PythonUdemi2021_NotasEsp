
# #CLASES Y OBJETOS EN PYTHON - P1
# #Una clase es un plantilla de la cual vamos a poder crear instancias u objetos
# #Se utiliza notacion para crear nombres de clases siempre empieza con mayuscula (ej: Persona o PersonaAdulta)
# #Puede ser distinto el nombre del archivo de la clase pero si es recomendable siempre respetar la notacion
# #pass: palabra reservada para indicar que no se va a añadir mas codigo a un nuevo nivel
# class Persona:
#     pass
#
# print(type(Persona))



# #CLASES Y OBJETOS EN PYTHON - P2
# #Se trabaja con los objentos y no con las clases (por mantener organizacion en el codigo) aunq en proximas clases se
# #podra aprender a trabajar con las clases directaente
# #Metodo __init__ metodo inicializador o constructor, aunq en python el constructor esta oculto
# #y se lo envia a llamar por el lenguaje, el metodo init sirve para inicializar y agregar los atributos de la clase
# #doble guion bajo al inicio y doble guion bajo al final = metodo especial al trabjar como clases
# #doble guion bajo = double underscore = dunder
# #metodo dunder init = metodo init
# #en clases python hay 2 tipos de atributos (atributos de clase, y atributos de instancia)
#
# class Persona:
#     def __init__(self):
#         self.nommbre = 'Juan'
#         self.apellido = 'Perez'
#         self.edad = 28
#         #No es común asignar valores por default a los atributos,
#         #más adelante veremos como hacerlo con parametros del metodo __init__
#
# persona1 = Persona() #Persona() llama de manera indirecta el metodo __init__
#
# print(persona1.nommbre)
# print(persona1.apellido)
# print(persona1.edad)





# #CREACION DE OBJETOS CON ARGUMENTOS
# #Constructor: Metodo para crear un objeto
# class Persona:
#     def __init__(self, nombre, apellido, edad):
#         self.nommbre = nombre
#         self.apellido = apellido
#         self.edad = edad
#
# persona1 = Persona('Jhonsson', 'Cordova', 31)
#
# print(persona1.nommbre)
# print(persona1.apellido)
# print(persona1.edad)





# #CREACION DE MÁS OBJETOS DE UNA CLASE
# #REFERENCIAS DE MEMORIA DE OBJETOS Y EJECUCION PASO A PASO
# class Persona:
#     def __init__(self, nombre, apellido, edad):
#         self.nommbre = nombre
#         self.apellido = apellido
#         self.edad = edad
#
# persona1 = Persona('Jhonsson', 'Cordova', 31)
# print(f'Objeto Persona 1: {persona1.nommbre} {persona1.apellido} {persona1.edad}')
#
# persona2 = Persona('Andrea', 'Loaiza', 20)
# print(f'Objeto Persona 2: {persona2.nommbre} {persona2.apellido} {persona2.edad}')





# #MODIFICAR ATRIBUTOS DE UN OBJETO
# class Persona:
#     def __init__(self, nombre, apellido, edad):
#         self.nommbre = nombre
#         self.apellido = apellido
#         self.edad = edad
#
# persona1 = Persona('Jhonsson', 'Cordova', 31)
# print(f'Objeto Persona 1: {persona1.nommbre} {persona1.apellido} {persona1.edad}')
#
# persona1.nommbre = 'Juan Carlos'
# persona1.apellido = 'Juarez'
# persona1.edad = 25
# print(f'Objeto Persona 1: {persona1.nommbre} {persona1.apellido} {persona1.edad}')
#
# persona2 = Persona('Andrea', 'Loaiza', 20)
# print(f'Objeto Persona 2: {persona2.nommbre} {persona2.apellido} {persona2.edad}')




# #METODOS DE INSTANCIA EN PYTHON
# class Persona:
#     def __init__(self, nombre, apellido, edad):
#         self.nommbre = nombre
#         self.apellido = apellido
#         self.edad = edad
#
#     #En python es muy utilizada (lo mas comun) la notacion de quion bajo para separar palabras en metodos
#     #aunq tambien se puede utilizar la notacion de camello
#     #def mostrarDetalle
#     def mostrar_detalle(self):
#         print(f'Persona: {self.nommbre} {self.apellido} {self.edad}')
#
# persona1 = Persona('Jhonsson', 'Cordova', 31)
# #print(f'Objeto Persona 1: {persona1.nommbre} {persona1.apellido} {persona1.edad}')
# persona1.mostrar_detalle()
#
# persona2 = Persona('Andrea', 'Loaiza', 20)
# #print(f'Objeto Persona 2: {persona2.nommbre} {persona2.apellido} {persona2.edad}')
# persona2.mostrar_detalle()




# #MÁS DE SELF Y ATRIBUTOS EN OBJETOS
# #self es lo mismo q this en otros lenguajes(java, c#, c++, etc), puede tambien tener otro nombre (solo el primer parametro)
# class Persona:
#     def __init__(self, nombre, apellido, edad):
#         self.nommbre = nombre
#         self.apellido = apellido
#         self.edad = edad
#
#     #En python es muy utilizada (lo mas comun) la notacion de quion bajo para separar palabras en metodos
#     #aunq tambien se puede utilizar la notacion de camello
#     #def mostrarDetalle
#     def mostrar_detalle(self):
#         print(f'Persona: {self.nommbre} {self.apellido} {self.edad}')
#
# persona1 = Persona('Jhonsson', 'Cordova', 31)
# #print(f'Objeto Persona 1: {persona1.nommbre} {persona1.apellido} {persona1.edad}')
# persona1.mostrar_detalle()
# #agregar atribitos al vuelo, ningun otro objeto podra acceder a este atributo (unicamente definido para este objeto)
# persona1.telefono = '55441122'
# print(persona1.telefono)
# #Persona.mostrar_detalle(persona1) #otra forma de llamar, como una forma poco comun de hacerlo
#
# persona2 = Persona('Andrea', 'Loaiza', 20)
# #print(f'Objeto Persona 2: {persona2.nommbre} {persona2.apellido} {persona2.edad}')
# #persona2.mostrar_detalle()
# Persona.mostrar_detalle(persona2)
# print(persona2.telefono)




#
# #ROBUSTECIENDO EL METODO INIT
# class Persona:
#     def __init__(self, nombre, apellido, edad, *args, **kwargs):
#         self.nommbre = nombre
#         self.apellido = apellido
#         self.edad = edad
#         self.valoes = args
#         self.terminos = kwargs
#
#
#     def mostrar_detalle(self):
#         print(f'Persona: {self.nommbre} {self.apellido} {self.edad} {self.valoes} {self.terminos}')
#
# persona1 = Persona('Jhonsson', 'Cordova', 31, '0996155789', 2,3,5, m='manzana', p='pera')
# persona1.mostrar_detalle()
#
#
# persona2 = Persona('Andrea', 'Loaiza', 20)
# Persona.mostrar_detalle(persona2)





# #ENCAPSULAMIENTO EN PYTHON
# class Persona:
#     def __init__(self, nombre, apellido, edad):
#         self.__nombre = nombre
#         self.apellido = apellido
#         self.edad = edad
#
#
#
#     def mostrar_detalle(self):
#         print(f'Persona: {self.__nombre} {self.apellido} {self.edad}')
#
# persona1 = Persona('Jhonsson', 'Cordova', 31)
# persona1.mostrar_detalle()
# #acontinuacion se evidencia un atributo publico
# #persona1.nommbre = 'Juanito'
#
# #persona1._nombre = 'Juanito'#no se deberia hacer para codigo en produccion
# #persona1.mostrar_detalle() #si permite el cambio pero python no es como otros lenguajes de programacion que no permiten modificadores de acceso
# #acontinuacion se evidencia a lo que se conoce como atributo encapsulado
#
# #Para una mayor restriccion se utiliza el doble guion bajo (otra notacion para que no ´pueda ser modificado el atributo)
# #no es practica muy comun pero si es posible utilizarlo
# persona1.__nombre = 'Juanito'
# persona1.mostrar_detalle()



#
# #METODOS GET Y SET EN PYTHON
# class Persona:
#     def __init__(self, nombre, apellido, edad):
#         self._nombre = nombre
#         self.apellido = apellido
#         self.edad = edad
#
#     #metodos get y set
#     #get = obtener / recuperar
#     #set = colocar / modificar
#     #para evitar la modificacion del atributo fuera de la clase utilizamos un decorador
#     #Decorador=modifica el comportamiento del metodo
#     @property #sirve para indicar que va a utilizar el atributo _nombre
#     # = encapsula, entonces vamos a poder accederlo unicamente a traves del metodo
#     # = ya no va a ser necesario usar parentesis para llamar al metodo
#     def nombre(self):
#         print('Llamando metodo get nombre') #para comprobar
#         return self._nombre
#
#     #Lo siguiente hace que el metodo se pueda invocar desde fuera de la clase como si se estubiera
#     # tratando de un atributo de nuestra clase
#     @nombre.setter
#     def nombre(self, nombre):
#         print('Llamando metodo set nombre') #para comprobar
#         self._nombre = nombre
#
#
#
#     def mostrar_detalle(self):
#         print(f'Persona: {self._nombre} {self.apellido} {self.edad}')
#
# persona1 = Persona('Jhonsson', 'Cordova', 31)
# print(persona1.nombre)
# persona1.nombre = 'Andrea Loaiza'
# #persona1.mostrar_detalle()
#
# print(persona1.nombre)
#
# persona1._nombre = 'Cambio con una mala practica' #esto es posible pero es una mala practica
# print(persona1._nombre) #esto es posible pero es una mala practica




#
# #ENCAPSULANDO TODOS LOS ATRIBUTOS EN UNA CLASE
# class Persona:
#     def __init__(self, nombre, apellido, edad):
#         self._nombre = nombre
#         self._apellido = apellido
#         self._edad = edad
#
#     @property
#     def nombre(self):
#         print('Llamando metodo get nombre') #para comprobar
#         return self._nombre
#
#
#     @nombre.setter
#     def nombre(self, nombre):
#         print('Llamando metodo set nombre') #para comprobar
#         self._nombre = nombre
#
#     @property
#     def apellido(self):
#         print('Llamando metodo get apellido')  # para comprobar
#         return self._apellido
#
#     @apellido.setter
#     def apellido(self, apellido):
#         print('Llamando metodo set apellido')  # para comprobar
#         self._apellido = apellido
#
#     @property
#     def edad(self):
#         print('Llamando metodo get edad')  # para comprobar
#         return self._edad
#
#     @edad.setter
#     def edad(self, edad):
#         print('Llamando metodo set edad')  # para comprobar
#         self._edad = edad
#
#
#
#     def mostrar_detalle(self):
#         print(f'Persona: {self._nombre} {self._apellido} {self._edad}')
#
# persona1 = Persona('Jhonsson', 'Cordova', 31)
# #Al no tener un set nombre se convierte en una propiedad de solo lectura
#
# persona1.nombre = 'Andrea'
# persona1.apellido = 'Loaiza'
# persona1.edad = 25
#
# persona1.mostrar_detalle()






# #USO DE MODULOS Y CLASES EN PYTHON
# class Persona:
#     def __init__(self, nombre, apellido, edad):
#         self._nombre = nombre
#         self._apellido = apellido
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
#     @property
#     def apellido(self):
#         return self._apellido
#
#     @apellido.setter
#     def apellido(self, apellido):
#         self._apellido = apellido
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
#         print(f'Persona: {self._nombre} {self._apellido} {self._edad}')
#
# persona1 = Persona('Jhonsson', 'Cordova', 31)
#
# persona1.nombre = 'Andrea'
# persona1.apellido = 'Loaiza'
# persona1.edad = 25
#
# persona1.mostrar_detalle()




#
# #COMPROBACION DEL MODULO PRINCIPAL EN PYTHON
# class Persona:
#     def __init__(self, nombre, apellido, edad):
#         self._nombre = nombre
#         self._apellido = apellido
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
#     @property
#     def apellido(self):
#         return self._apellido
#
#     @apellido.setter
#     def apellido(self, apellido):
#         self._apellido = apellido
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
#         print(f'Persona: {self._nombre} {self._apellido} {self._edad}')
#
# if __name__ == '__main__':
#     persona1 = Persona('Jhonsson', 'Cordova', 31)
#
#     persona1.nombre = 'Andrea'
#     persona1.apellido = 'Loaiza'
#     persona1.edad = 25
#
#     persona1.mostrar_detalle()
#
#     # en python existen nombres reservados ejemplo donder name = "__name__"
#     print(__name__)






#DESTRUCTOR DE OBJETOS EN PYTHON
class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre


    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad



    def mostrar_detalle(self):
        print(f'Persona: {self._nombre} {self._apellido} {self._edad}')

    #agregacion del metodo destructor
    #todas las clases en python heredan de la clase Object,
    #por lo tanto se heredan todos los metodos dobleunder "donder"
    def __del__(self):
        print(f'Persona: {self._nombre} {self._apellido} {self._edad}')


if __name__ == '__main__':
    persona1 = Persona('Jhonsson', 'Cordova', 31)

    persona1.nombre = 'Andrea'
    persona1.apellido = 'Loaiza'
    persona1.edad = 25

    persona1.mostrar_detalle()
