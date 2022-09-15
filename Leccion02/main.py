# #Operadores aritméticos(+, -, *, /, //, **, %)
# operandoA = 3
# operandoB = 2
#
# suma = operandoA + operandoB
#
# #print('Resultado de la suma: ', suma)
# #interpolación
# print(f'Resultado de la suma: {suma}')



# operandoA = 3
# operandoB = 2
#
# suma = operandoA + operandoB
#
# #print('Resultado de la suma: ', suma)
# #interpolación
# print(f'Resultado suma: {suma}')
#
# resta = operandoA - operandoB
# print(f'Resultado resta: {resta}')
#
# multiplicacion = operandoA * operandoB
# print(f'Resultado multiplicación: {multiplicacion}')
#
# division = operandoA / operandoB
# print(f'Resultado division: {division}')
#
# division = operandoA // operandoB
# print(f'Resultado division(int): {division}')
#
# modulo = operandoA % operandoB
# print(f'Resultado modulo: {modulo}')
#
# exponente = operandoA ** operandoB
# print(f'Resultado exponente: {exponente}')



# #asignacion
# miVariable = 10
# print(miVariable)
#
# #reasignacion
# miVariable = miVariable+1
# print(miVariable)
# #incremento con reasignacion
# miVariable+=1
# print(miVariable)
# #miVariable = miVariable - 2
# miVariable-=2
# print(miVariable)
# #miVariable = miVariable * 3
# miVariable*=3
# print(miVariable)
# #miVariable = miVariable / 3
# miVariable/=2
# print(miVariable)



# #Operadores de comparación
# a = 4
# b = 6
# resultado = (a == b)
# print(f'Resultado de comparar == : {resultado}')
#
# resultado = (a != b)
# print(f'Resultado de comparar != : {resultado}')
#
# resultado = (a > b)
# print(f'Resultado de comparar > : {resultado}')
#
# resultado = (a >= b)
# print(f'Resultado de comparar >= : {resultado}')
#
# resultado = (a < b)
# print(f'Resultado de comparar < : {resultado}')
#
# resultado = (a <= b)
# print(f'Resultado de comparar <= : {resultado}')



# #Ejercicio numero Par o Impar en python
# a = int(input('Escribe un valor numérico: '))
# print(a % 2)
# if (a % 2) == 0:
#     print(f'El valor de a {a} es número par')
# else:
#     print(f'El valor de a {a} es impar par')



# #Algoritmo Mayor de edad
# edadAdulto = 18
# edadPersona = int(input("Proporciona tu edad: "))
# if( edadPersona >= edadAdulto):
#     print(f'La Persona con edad {edadPersona} es adulto')
# else:
#     print(f'La Persona con edad {edadPersona} es menor de edad')



# #Operadores Lógicos (and, or, not)
# a = True
# b = False
# resultado = a and b
# #print(resultado)
#
# resultado = a or b
# #print(resultado)
#
# resultado = not a
# print(resultado)


#AND
# valor = int(input('Escribe el Valor: '))
# valorMinimo = 0
# valorMaximo = 5
#
# #dentroRango = ((valor>=valorMinimo) and (valor<=valorMaximo))
# dentroRango = valor>=valorMinimo and valor<=valorMaximo
#
# if(dentroRango):
#     print(f'El Valor {valor} esta Dentro de Rango')
# else:
#     print(f'El Valor {valor} esta Fuera de Rango')


# #OR
# vacaciones = False
# diaDescanso = True
#
# if vacaciones or diaDescanso:
#     print('Puede asistir al juego')
# else:
#     print('Tiene deberes por hacer')



# #NOT
# vacaciones = False
# diaDescanso = False
#
# if not(vacaciones or diaDescanso):
#     print('Tiene deberes por hacer')
# else:
#     print('Puede asistir al juego')



# #EDADES ENTRE VEINTES Y TREINTAS
# edad = int(input('Introdice tu Edad: '))
# # veintes = edad >= 20 and edad < 30
# # print(veintes)
# #
# # treintas = edad >= 30 and edad < 40
# # print(treintas)
#
# if (edad >= 20 and edad < 30) or (edad >= 30 and edad < 40):
#     print('Dentro de rango (20\'s) o (30\'s)')
#     # if veintes:
#     #     print('Dentro de los 20\'s')
#     # elif treintas:
#     #     print('Dentro de los 30\'s')
#     # else:
#     #     print('Fuera de Rango')
# else:
#     print("No está dentro de los 20's ni 30's")



#Tienda de Libros
print('Proporcione los siguientes datos del Libro:')
nombreLibro = input('Proporciona el nombre: ')
idLibro = int(input('Proporciona el ID: '))
precioLibro = float(input('Proporciona el precio: '))
#Castear con *bool()* solo hace comprobación si hay texto o no indistintamente de lo que se escriba
envioLibro = input('Indica si el envio en gratuito (True/False): ')

if envioLibro == 'True':
    envioLibro = True
elif envioLibro == 'False':
    envioLibro = False
else:
    envioLibro = ' Valor incorrecto, debe escribir True/False'
#f+triplecomilla envia a imprimir texto a consola en formato ya deseado
print(f'''
    Nombre: {nombreLibro}
    Id: {idLibro} 
    Precio: {precioLibro}
    Envío Gratuito?: {envioLibro}
''')