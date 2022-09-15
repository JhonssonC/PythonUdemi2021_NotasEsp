from Persona import *

persona1 = Persona('Juan', 28)
#cuando se llama a un objeto se manda a llamar al metodo de clase object __str__() por defecto
print(persona1)


empleado1 = Empleado('Karla', 30, 5000)
print(empleado1)# en este caso se hereda el __str__() reescrito, se puede nuevamente sobreescribir