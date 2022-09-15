# #FUNCIONES EN PYTHON
# #la palabra reservada def sirve para identificar una funcion (decalracion)
# #posterior a def se escribe el nombre de la funcion pudiendo ser en el formato mi_funcion o miFuncion
# # (sin espacios, separando por guion bajo o letras mayuscular para cada palabra despues de la primera palabra en minusculas)
# #como en las variables (notación de camello o de altas y bajas)
#
# #notacion de guion bajo
# #def mi_funcion_en_python
# #notacion de camello o de altas y bajas
# #def miFuncionEnPython
#
# def mi_funcion():
#     print('Saludos desde mi función')
#
# mi_funcion()
# mi_funcion()
# mi_funcion()
# mi_funcion()



# #parametro en la funcion, argumentos con lo que se llama a la funcion
# def mi_funcion(nombre, apellido):
#     print('Saludos desde mi función')
#     print(f'Nombre: {nombre}, Apellido: {apellido}')
#
# mi_funcion('Jhonsson', 'Córdova')
# mi_funcion('Andrea', 'Loaiza')




# #SUMA DE DOS VALORES- PALABRA RETURN EN FUNCIONES
# def suma(a, b):
#     return (a+b)
#
# # resultado = suma(5, 3)
# # print(f'Resultado sumar: {resultado}')
#
# print(f'Resultado sumar: {suma(5, 3)}')



#
# #VALORES POR DEFAULT A LOS PARAMETROS DE UNA FUNCION
# # def suma(a:int=0, b:int=0) -> int: #pista o indicio de lo que va a regresar la funcion (->) es opcional,
#     # no es necesario especificar el tipo de dato de retorno o de los parametros, puede considerarse como redundante
# def suma(a=0, b=0):
#     return (a+b)
#
# resultado = suma()
# print(f'Resultado sumar: {resultado}')
#
# print(f'Resultado sumar: {suma(2, 8)}')


# #CANTIDAD DE ARGUMENTOS VARIABLE EN FUNCIONES CON PYTHON
# def listarNombres(*nombres): #a *nombres python lo asimila como una tupla (en la doc de python se los encuentra representados como *args)
#     for nombre in nombres:
#         print(nombre)
#
# listarNombres('Jhonsson', 'Andrea', 'Danny', 'Melita', 'Fanny')
# listarNombres('Laura', 'Carlos')



# #ARGUMENTOS VARIABLES LLAVE-VALOR EN PYTHON
# def listarTerminos(**terminos): #a *terminos python lo asimila como un diccionario (en la doc de python se los encuentra representados como **kwargs)
#     for llave, valor in terminos.items():
#         print(f'{llave} : {valor}')
#
# listarTerminos(
#     IDE= 'Integrated Development Environment', PK='Primary Key'
# )
#
# listarTerminos(DBMS='Database Managemente System')




# #DISTINTOS TIPOS DE DATOS COMO ARGUMENTOS EN PYTHON
# def desplegarNombres(nombres):
#     for nombre in nombres:
#         print(nombre)
#
# nombres = ['Juan', 'Karla', 'Guillermo']
# desplegarNombres(nombres)
# desplegarNombres('Carlos')
# desplegarNombres((10, 11))
# desplegarNombres([10, 11])




#FUNCIONES RECURSIVAS EN PYTHON
#Una funcion recursiva es la que se llama a si mismo un numer x de veces para cumplir un objetivo
#Ejemplo Factorial de un numero
# 5! = 5 * 4 * 3 * 2 * 1
# 5! = 5 * 4 * 3 * 2 *
# 5! = 5 * 4 * 6
# 5! = 5 * 24
# 5! = 120

def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero -1)

numero = 7
resultado = factorial(numero)
print(f'El factorial de {numero} es {resultado}')

