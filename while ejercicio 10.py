#elabora un algoritmo que pida 3 notas de n estudiante e imprima la nota mas alta, la mas baja y el promedio.

cantidad = int(input("Ingrese la cantidad de notas: "))
contador = 0
sumaNotas = 0

while contador < cantidad:
    nota = float(input("Ingrese una nota: "))
    sumaNotas += nota

    if contador == 0:
        notaMaxima = nota
        notaMinima = nota
    else:
        if nota > notaMaxima:
            notaMaxima = nota
        elif nota < notaMinima:
            notaMinima = nota

    contador += 1

promedio = sumaNotas / cantidad

print("La nota más alta es:", notaMaxima)
print("La nota más baja es:", notaMinima)
print("El promedio de notas es:", promedio)


