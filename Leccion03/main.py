# #condicion = False
# #condicion = 10# = a verdadero si se aplica if directo, osea si no esta vacia el resultado es True
# #condicion = ''# = a falso si se aplica if directo, osea si esta vacia el resultado es False
# condicion = 'hola'
#
# #la identacion basta que sea un espacio, lo recomendable es que haya tabulación
# #if condicion: #Dentro de un if (condicion) no es igual a (condicion=True) xq condicion puede no ser buleano o tener otro tipo de dato
# if condicion==True: # de esta forma se asegura que el valor de una variable sea booleano y no de otro tipo
#  print('Condición Verdadera')
# elif condicion == False:
#  print('Condición Falsa')
# else:
#  print('Condición no Reconocida')



# #NUMERO A TEXTO 1-3
# numero = int(input('Proporciona un valor entre 1 y 3: '))
# numeroTexto=''
# if numero == 1:
#    numeroTexto = 'Número uno'
# elif numero == 2:
#    numeroTexto = 'Número dos'
# elif numero == 3:
#    numeroTexto = 'Número tres'
# else:
#    numeroTexto='Valor fuera de rango'
#
# print(f'Número proporcionado: {numero} - {numeroTexto}')




# #SINTAXIS SIMPLIFICADA (OPERADOR TERNARIO) DE IF-ELSE
# condicion = False
#
# # if condicion:
# #     print('Condocion Verdadera')
# # else:
# #     print('Condicion Falsa')
#
# print('Condicion Verdadera') if condicion else print('Condicion Falsa')




# #ESTACION SEGÚN MES DEL AÑO
# mes = int(input('Proporciona mes del año (1 - 12): '))
# #"None" equivale a "Null" de otros lenguajes
# estacion = None
# if mes == 1 or mes == 2 or mes == 12:
#     estacion = 'Invierno'
# elif mes == 3 or mes ==4 or mes == 5:
#     estacion = 'Primavera'
# elif mes == 6 or mes == 7 or mes == 8:
#     estacion = 'Verano'
# elif mes == 9 or mes == 10 or mes == 11:
#     estacion = 'Otoño'
# else:
#     estacion = 'Mes Incorrecto'
#
# print(f'Para el mes {mes} la estación es: {estacion}')




#ETAPAS DE VIDA SEGUN LA EDAD
edad = int(input('Proporciona tu edad: '))

if 0 <= edad <10:
    mensaje = 'La infancia es increible...'
elif 10 <= edad <20:
    mensaje = 'Muchos cambios y mucho estudio...'
elif 20 <= edad <30:
    mensaje = 'Amor y comienza el trabajo...'
else:
    mensaje = 'Etapa de vida NO reconocida'

print(f'Tu edad es: {edad}, {mensaje}')