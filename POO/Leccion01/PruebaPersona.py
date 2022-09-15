# #USO DE MODULOS Y CLASES EN PYTHON
# #from = modulo o archivo (nombre del archivo)
# #import = la clase dentro del archivo (un archivo o modulo puede tener muchas clases)
#
# from Persona import Persona
#
# persona1 = Persona('Jhonssin', 'Davila', 31)
# persona1.mostrar_detalle()





# #COMPROBACION DEL MODULO PRINCIPAL EN PYTHON
# from Persona import Persona
#
# #esta comprobacion se utiliza como codigo de prueba para ejecutar codigo dentro de un modulo y hacer pruebas
# if __name__ =='__main__':
#     persona1 = Persona('Jhonssin', 'Davila', 31)
#     persona1.mostrar_detalle()
#
#     print(__name__)




#DESTRUCTOR DE OBJETOS EN PYTHON
from Persona import Persona

#,center, metodo de string para dar formato rapido al texto, muy util para consola
print('Creacion de onjetos'.center(30,'-'))
persona1 = Persona('Jhonssin', 'Davila', 31)
persona1.mostrar_detalle()

print('Eliminacion de Objetos'.center(30,'-'))
del persona1
#es raro encontrar la notacion de eliminacion ya que existe un recolector de basura ne python
#esto es que los objetos no apuntados por una variable son eliminados por el "garbage collector"
#o al terminar la ejecucion dle programa