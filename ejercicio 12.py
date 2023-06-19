#elabore un algoritmo que pida las 4 notas de n estudiantes e imprima las notas mas alta, la mas baja y el promedio.

n = int(input("Ingrese la cantidad de estudiantes: "))

notas_mas_altas = []
notas_mas_bajas = []
promedios = []

for i in range(n):
    notas = []
    for j in range(4):
        nota = float(input("Ingrese la nota {} del estudiante {}: ".format(j+1, i+1)))
        notas += [nota]

    notas_mas_altas += [max(notas)]
    notas_mas_bajas += [min(notas)]
    promedios += [sum(notas) / 4]

nota_mas_alta_general = max(notas_mas_altas)
nota_mas_baja_general = min(notas_mas_bajas)
promedio_general = sum(promedios) / n

print("La nota más alta es:", nota_mas_alta_general)
print("La nota más baja es:", nota_mas_baja_general)
print("El promedio general es:", promedio_general)
