# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 3.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de práctica numérica

# Condicionales anidados elif

# Objetico
# Verificar la calificación de un estudiante según su
# puntaje en un examen
puntaje = 37

# Alumno:
# Deberá crear una serie de considiconales
# con if y elif de forma tal de cargar en
# la variable nota la nota del alumno según
# las siguientes condiciones:

nota = ""

# Si el puntaje es mayor igual a 90 --> nota = "A"
# Si el puntaje es mayor igual a 80 --> nota = "B"
# Si el puntaje es mayor igual a 70 --> nota = "C"
# Si el puntaje es mayor igual a 60 --> nota = "D"
# Si el puntaje es menor a  60      --> nota = "F"

if puntaje >= 90:
    nota = "A"
elif puntaje >= 80 and puntaje < 90:
    nota = "B"
elif puntaje >= 70 and puntaje < 80:
    nota = "C"
elif puntaje >= 60 and puntaje < 70:
    nota = "D"
else:
     nota = "F"

# Recuerde utilizar un solo bloque condicional
# armado de if y múltiples elif
# Puede consultar el ejemplo de clase 2 como referencia

# Imprimir en pantalla la variable nota
print('La nota es:', nota)