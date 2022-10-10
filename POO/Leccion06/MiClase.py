# #VARIABLES DE CLASE EN PYTHON
# #Una variable de clase es aquella que se comparte en todas las clases o instancias creadas
# #a partir de la clase
# #las variables de clase se asocian con la clase en si misma y se comparten con todos los objetos creados a partir de la clase
#
# class MiClase:
#
#     variable_clase = 'Valor variable clase'
#
#     def __init__(self, variable_instancia):
#         self.variable_instancia = variable_instancia
#
#
# #Para acceder a la variable de clase debemos hacer referencia a la clase en primera instancia de la siguiente manera:
# print(MiClase.variable_clase)
#
# #A diferencia de la variable de instancia es necesario crear un objeto en primer lugar
# miClase = MiClase('Valor variable instancia')
# #Valor de variable de instancia es un valor por cada objeto, a diferencia del de variable de clase es uno en la clase, no necesita instancia ni objeto
# print(miClase.variable_instancia)
#
# #Desde el objeto tambien se puede recuperar al variable de clase
# print(miClase.variable_clase)
#
#
# miClase2 = MiClase('Otro Valor de variable instancia')
# print(miClase2.variable_instancia)
# print(miClase2.variable_clase)



# #CREACION DE VARIABLES DE CLASE AL VUELO EN PYTHON
#
# class MiClase:
#
#     variable_clase = 'Valor variable clase'
#
#     def __init__(self, variable_instancia):
#         self.variable_instancia = variable_instancia
#
# print(MiClase.variable_clase)
# miClase = MiClase('Valor variable instancia')
# print(miClase.variable_instancia)
# print(miClase.variable_clase)
#
# #Se puede asignar variables de clase al vuelo de la siguiente forma:
# MiClase.variable_clase2 = 'Valor variable 2'
# #no es necesario definirlo en la clase, se puede hacer gracias a que Python es dinamico
#
#
# miClase2 = MiClase('Otro Valor de variable instancia')
# print(miClase2.variable_instancia)
# print(miClase2.variable_clase)
#
# #se accede desde la clase
# print(MiClase.variable_clase2)
#
# #o desde objeto:
# print(miClase2.variable_clase2)






# #METODOS ESTATICOS EN PYTHON
# #tambien llamados metodos de clase
#
# class MiClase:
#
#     variable_clase = 'Valor variable clase'
#
#     def __init__(self, variable_instancia):
#         self.variable_instancia = variable_instancia
#
#     #Metodo estatico = metodo asociado a la clase en si misma
#     #Metodo estatico al igual que variable de clase
#     @staticmethod
#     def metodo_estatico(): #no recibe el parametro self al ser estatico
#         #Los metodos estaticos (contexto estatico junto con las variables de clase)
#         #no pueden acceder a las variables de instancia ni metodos de instancia (contexto dinamico)
#         #siempre acceder a variable de clase desde un metodo de clase accediendo primero a la clase y posteriormente a
#         #la variable
#         print(MiClase.variable_clase)





# #METODOS DE CALSE EN PYTHON
# class MiClase:
#
#     variable_clase = 'Valor variable clase'
#
#     def __init__(self, variable_instancia):
#         self.variable_instancia = variable_instancia
#
#     #El metodo estatico no tiene relacion directa con la clase por lo que puede traquilamente ser una funcion mas
#     # del archivo, los metodos estaticos sirven para definir una relacion logica con la clase pero q no tiene q ver
#     # nada con la clase en si.
#     @staticmethod
#     def metodo_estatico():
#         print(MiClase.variable_clase)
#
#
#     #Un metodo de clase a diferencia de un metodo estatico si recibe un contexto de clase
#     # si recibe parametro de clase
#     @classmethod
#     def metodo_clase(cls):#recibimos un parametro q accede a las variables de clase
#         print(cls.variable_clase)
#
# MiClase.metodo_estatico()
#
# MiClase.metodo_clase()#no se pasa el parametro






#CONTEXTO ESTATICO Y CONTEXTO DINAMICO EN PYTHON
class MiClase:

    variable_clase = 'Valor variable clase'

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia

    @staticmethod
    def metodo_estatico():
        print(MiClase.variable_clase)


    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase)


    #metodo de instancia
    def metodo_instancia(self):
        self.metodo_clase()
        self.metodo_estatico()
        print(self.variable_clase)
        print(self.variable_instancia)

MiClase.metodo_clase()

#una vez que ya se ha cargano la clase en memoria un objeto si puede acceder a las variables y metodos de clase
#pero no de una forma inversa osea que una clase no puede acceder a las variables y metodos de instancia
#en resumen:
# el contexto dinamico si puede acceder al contexto estatico
# pero el contexto estatico no puede acceder al contexto dinamico
miObjeto1 = MiClase('Variable_instancia')
miObjeto1.metodo_clase()

miObjeto1.metodo_instancia()