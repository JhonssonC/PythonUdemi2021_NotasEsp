#Prueba para modulo de constantes "constantes.py"
#valor constante independiente
from constantes import MI_CONSTANTE
#Valor constante de clase
from constantes import Matematicas as mate   #"as" reidentifica dentro de este modulo a la importacion de la clase Matemeticas, es decir en este modulo esa clase se llamará mate

#se accede al valor y se comprueba su valor
#variable independiente
print(MI_CONSTANTE)
#valiable de clase
print(mate.PI)

#Como se explicaba el contexto de constante en python no existe y se puede tratar a la constante como una variable
#pero al conocer la nomenclaruta de una constante es una practiva respetable no modificarla
#ya que una constante no debe modificarse

#No debemos cambiar el valor de una constante
#MI_CONSTANTE = 'Nuevo Valor'
#print(MI_CONSTANTE)

