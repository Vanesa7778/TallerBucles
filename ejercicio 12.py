#elabore un algoritmo que pida las 4 notas de n estudiantes e imprima las notas mas alta, la mas baja y el promedio.

cantidad = int(input("Ingrese la cantidad de estudiantes: "))

notasAltas = []
notasBajas = []
promedios = []

for i in range(cantidad):
    notas = []
    for j in range(4):
        nota = float(input("Ingrese la nota {} del estudiante {}: ".format(j+1, i+1)))
        notas += [nota]

    notasAltas += [max(notas)]
    notasBajas += [min(notas)]
    promedios += [sum(notas) / 4]

notaAltaGeneral = max(notasAltas)
notaBajaGeneral = min(notasBajas)
promedioGeneral = sum(promedios) / cantidad

print("La nota más alta es:", notaAltaGeneral)
print("La nota más baja es:", notaBajaGeneral)
print("El promedio general es:", promedioGeneral)
