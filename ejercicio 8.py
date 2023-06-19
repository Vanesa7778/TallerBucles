#un maestro de escuela necesita un algoritmo que capture n notas de un estudiante y calcule el promedio for python.

n = int(input("Ingrese la cantidad de notas para sacar su promedio: "))

notas = []
suma = 0

for i in range(n):
    nota = float(input("Ingrese la nota ", i+1, ": "))
    suma += nota

promedio = suma / n

print("El promedio de las notas es:", promedio)
