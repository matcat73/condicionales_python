# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 3.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Objetizo:
Realizar un programa que solicite ingresar
tres valores decimales de temperatura
De las temperaturas ingresadas se determinará:
1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
3 - ¿Cuál es el promedio de las temperaturas ingresadas?

IMPORTANTE: Para ordenar las temperatuas debe utilizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido. Recomendamos pensar bien este problema de lógica con un lápiz y papel.

Alumno:
- Deberá solicitar tres números decimales por consola,
cada nuḿero de temperatura lo debe almacenar
en variables llamadas:
-> temperatura_1
-> temperatura_2
-> temperatura_3

Luego, mediante el uso de condicionales, deberá determinar
cuales de ellas es la mayor temperatura. Deberá almacenar
el valor de la temperatura más alta en una nueva variable
llamada:
--> temperatura_max

Luego, mediante el uso de condicionales, deberá determinar
cuales de ellas es la menor temperatura. Deberá almacenar
el valor de la temperatura más baja en una nueva variable
llamada:
--> temperatura_min

- Al final imprimir en pantalla la variable temperatura_max
  y temperatura_min
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio

temperatura_1 = float(input('Ingrese Valor de temperatura 1:'))
temperatura_2 = float(input('Ingrese Valor de temperatura 2:'))
temperatura_3 = float(input('Ingrese Valor de temperatura 3:'))

if temperatura_1 > temperatura_2 and temperatura_1 > temperatura_3:
  temperatura_max = temperatura_1
elif temperatura_2 > temperatura_1 and temperatura_2 > temperatura_3:
  temperatura_max = temperatura_2
elif temperatura_3 > temperatura_1 and temperatura_3 > temperatura_2:
  temperatura_max = temperatura_3

if temperatura_1 < temperatura_2 and temperatura_1 < temperatura_3:
  temperatura_min = temperatura_1
elif temperatura_2 < temperatura_1 and temperatura_2 < temperatura_3:
  temperatura_min = temperatura_2
elif temperatura_3 < temperatura_1 and temperatura_3 < temperatura_2:
  temperatura_min = temperatura_3

print('La temperatura máxima es:', temperatura_max)
print('La temperatura mínima es:', temperatura_min)