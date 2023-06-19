#un maestro de escuela necesita un algoritmo que capture n notas de un estudiante y calcule el promedio.

num = int(input("Ingrese la cantidad de notas: "))
contador = 1
suma = 0

while contador <= num:
    nota = float(input("Ingrese la nota {}: ".format(contador)))
    suma += nota
    contador += 1

promedio = suma / num

print("El promedio de las notas es:", promedio)
