# #LISTAS
# #Definir una lista de tipo str
# nombres=[ 'Juan', 'Karla', 'Ricardo', 'María' ]
# #imprimir la lista de nombres
# print(nombres)
# #Acceder a los elemenstos de una lista
# print(nombres[0])
# print(nombres[1])
# print(nombres[2])
# print(nombres[3])
# #se puede utilizar valores negativos para acceder a los elementos d3e la lista
# print(' a la inversa...')
# print(nombres[-1]) #ultimo elemento
# print(nombres[-2])
# print(nombres[-3])
# print(nombres[-4])
#
# #RANGOS DE LISTA
# #imprimir un rango
# print(nombres[0:2])#recupera los elementos 0 y 1
# #Ir del nicio de la lista al indice (sin incluirlo)
# print(nombres[:3])
# #Desde el indice indicado hasta el final
# print(nombres[1:])
# #Cambiar un valor
# nombres[3] = 'Ivone'
# print(nombres)
# #Iterar lista
# for nombre in nombres: #listas se definen en plural
#     print(nombre)
# else:
#     print('No existen mas nombres en la lista')
#
# #Preguntar largo de una lista
# print(len(nombres))
# #Agregar un elemento
# nombres.append('Lorenzo')
# print(nombres)
# #Insertar en un indice especifico
# nombres.insert(1, 'Octavio')
# print(nombres)
# #Remover un elemento
# nombres.remove('Octavio')
# print(nombres)
# #Remover el ultimo valor agregado
# nombres.pop()
# print(nombres)
# #Eliminar un indice indicado
# del nombres[0]
# print(nombres)
# #Limpiar l alista
# nombres.clear()
# print(nombres)
# #Borrar la lista por completo, hasta de memoria
# del nombres
# print(nombres)
# #UNA LISTA ES MUTABLE O MODIFICABLE




# #UNA TUPLA ES SIMILAR A UNA LISTA PERO ES INMUTABLE, NO SE PUEDE MODIFICAR NI ELIMINAR
#
# #Definir una tupla
# frutas = ('Naranja', 'Plátano', 'Guayaba') #toda tupla debe tener minimo 1 coma y debe ser inmediatamente despues del primer valor en el caso de que sea una tupla de un solo valor
# print(frutas)
# #Saber el largo de una tupla
# print(len(frutas))
# #Acceder a un elemento
# print(frutas[0])
# #Navegacion Inversa
# print(frutas[-1])
# #Acceder a un rango de valores
# print(frutas[0:2])#Sin incluir el ultimo indice
# #Recorrer elementos de tupla
# for fruta in frutas:
#     print(fruta, end='  ') #end especifica el caracter que se imprime despues de imprimir lo requerido (por defecto \n )
#
# #Cambiar valor de tupla
#
# #frutas[0] = 'Pera' #esto no funciona
#
# #para cambiar los valres de una tupla hay q primero cambiar el tipo a lista y luego la volvemos a transformar en tupla
# frutasLista = list(frutas)
# frutasLista[0] = 'Pera'
# frutas = tuple(frutasLista)
#
# del frutasLista
# print('\n', frutas)
#
# #eliminar la tupla
# del frutas
# print(frutas)



# #COLECCIONES DE TIPO SET EN PYTHON
# #A DIFERENCIA DE LA LISTA O LA TUPLA UN SET NO MANTIENE UN ORDEN Y TAMPOCO PERMITE ALMACENAR ELEMENTOS DUPLICADOS
# # NO ES POSIBLE MODIFICAR LOS ELEMENTOS ALMACENADOS EN UN SET PERO SI ES POSIBLE AGREGAR MAS ELEMENTOS O ELIMINARLOS
#
# planetas = {'Marte', 'Jupiter', 'Venus'}
# print(planetas)
# #largo
# print(len(planetas))
# #revisar si un elemento esta presente
# print('Marte' in planetas) #Funciona igual en listas y tuplas
# #Agregar un nuevo elemento
# planetas.add('Tierra')
# print(planetas)
# #No admite elementos duplicados
# planetas.add('Tierra')
# print(planetas)
# #Eliminar elementos posiblemente arrojando un error en caso de no encontrar la llave
# planetas.remove('Tierra')
# print(planetas)
# #Eliminacion de elemento no existente
# #planetas.remove('Tierras') #Envia un error a consola
# #print(planetas)
#
# #Eliminar elementos sin arrojar un error en caso de no encontrar la llave
# planetas.discard('Jupiters')
# print(planetas)
#
# #Limpiar set
# planetas.clear()
# print(planetas)
#
# #Eliminar Set
# del planetas
# print(planetas)




#DICCIONARIOS
#dict (key, value)
diccionario = {
    'IDE':'Integrated Development Environment',
    'OOP':'Object Oriented Programming',
    'DBMS':'Database Management System',
}
print(diccionario)
#Largo
print(len(diccionario))
#Acceder a un elemento (key)
print(diccionario['IDE'])
#Otra forma de recuperar un elemento
print(diccionario.get('OOP'))
#Modificando elementos
diccionario['IDE'] = "INTEGRATED DEVELOPMENT ENVIRONMENT"
print(diccionario)
#Recorrer los elementos
#solo key
for termino in diccionario:
    print(termino)
#otra forma
for termino in diccionario.keys():
    print(termino)
#solo value
for valor in diccionario.values():
    print(valor)
#key y value
for termino, valor in diccionario.items():
    print(termino, valor)

#Comprobar existencia de algun elemento
print('IDE' in diccionario)

#agregar un elemento
diccionario['PK'] = 'Primary Key'
#En caso de duplicidad se sobreescribe el valor de la key especificada
print(diccionario)

#Remover un elemento
diccionario.pop('DBMS')
print(diccionario)

#Limpiar el diccionario
diccionario.clear()
print(diccionario)

#Eliminar diccionario
del diccionario
print(diccionario)