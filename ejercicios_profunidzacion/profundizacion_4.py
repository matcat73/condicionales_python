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
Objetivo:
Realizar un programa que solicite ingresar
tres valores decimales de temperatura
De las temperaturas ingresadas se determinará:
1 - ¿Cuál es suma de todas las temperaturas ingresadas?
2 - ¿Cuál es el promedio de las temperaturas ingresadas?

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

Utilizando el operador suma o el operador incremento
deberá almacenar la suma de todas las temperaturas
ingresadas en una nueva variable llamada "temperatura_total"

Luego, mediante el uso de la variable "temperatura_total"
y teniendo en cuenta que se ingresaron tres temperaturas.
Deberá calcular el promedio de todas las temperaturas
y almacenar el resultado en una variable llamada
"temperatura_promedio"

- Al final imprimir en pantalla la variable 
  temperatura_promedio
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio

temperatura_1 = float(input('Ingrese Valor de temperatura 1:'))
temperatura_2 = float(input('Ingrese Valor de temperatura 2:'))
temperatura_3 = float(input('Ingrese Valor de temperatura 3:'))

if(temperatura_1 > temperatura_2 and temperatura_2 > temperatura_3):
  temp_max = temperatura_1
  temp_med = temperatura_2
  temp_min = temperatura_3
if(temperatura_1 > temperatura_3 and temperatura_3 > temperatura_2):
  temp_max = temperatura_1
  temp_med = temperatura_3
  temp_min = temperatura_2
if(temperatura_2 > temperatura_1 and temperatura_1 > temperatura_3):
  temp_max = temperatura_2
  temp_med = temperatura_1
  temp_min = temperatura_3
if(temperatura_2 > temperatura_3 and temperatura_3 > temperatura_1):
  temp_max = temperatura_2
  temp_med = temperatura_3
  temp_min = temperatura_1
if(temperatura_3 > temperatura_1 and temperatura_1 > temperatura_2):
  temp_max = temperatura_3
  temp_med = temperatura_1
  temp_min = temperatura_2
if(temperatura_3 > temperatura_2 and temperatura_2 > temperatura_1):
  temp_max = temperatura_3
  temp_med = temperatura_2
  temp_min = temperatura_1

temperatura_total = temperatura_1 + temperatura_2 + temperatura_3

temperatura_promedio = temperatura_total / 3

print(f'La temperatura máxima es {temp_max}, la media es {temp_med} y la mínima es {temp_min}')

print('La temperatura promedio ingresada es:', temperatura_promedio)