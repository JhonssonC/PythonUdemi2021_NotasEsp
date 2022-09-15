#CICLO WHILE
# condicion =True
#
# while condicion:
#     print('Ejecutando ciclo While')
#
# else:
#     print('Fin del ciclo While')

# contador = 0
# while contador < 3:
#     print(contador)
#     contador += 1 #contador = contador+1
# else:
#     print('Fin ciclo While')



# #ITERAR UNA CADENA CON FOR
# cadena = 'Hola'
#
# for letra in cadena:
#     print(letra)
# else:
#     print('Fin Ciclo For')

#
# #ROMPER CICLOS CON BREAK
# for letra in 'Holanda':
#     if letra== 'a':
#         print(f'Letra encontrada: {letra}')
#         break
# else:
#     print('Fin ciclo for')



#PALABRA CONTINUE = IR A LA SIGUIENTE ITERACION
# for i in range(6):
#     if i % 2 == 0:
#         print(f'Valor: {i}')

for i in range(6):
    if i % 2 != 0:
        continue
    print(f'Valor: {i}')