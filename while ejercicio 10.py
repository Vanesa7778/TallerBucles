#elabora un algoritmo que pida 3 notas de n estudiante e imprima la nota mas alta, la mas baja y el promedio.

cantidad = int(input("Ingrese la cantidad de estudiantes: "))

if cantidad > 0:
    
    contadorEstudiantes = 0

    while contadorEstudiantes < cantidad:
        contadorEstudiantes += 1
        print("Estudiante", contadorEstudiantes)

        nota1 = float(input("Ingrese la primera nota: "))
        nota2 = float(input("Ingrese la segunda nota: "))
        nota3 = float(input("Ingrese la tercera nota: "))

        notaMaxima = max(nota1, nota2, nota3)
        notaMinima = min(nota1, nota2, nota3)
        promedio = (nota1 + nota2 + nota3) / 3

        print("Nota más alta:", notaMaxima)
        print("Nota más baja:", notaMinima)
        print("Promedio:", promedio)
        print()
elif cantidad <= 0:
    print("La cantidad de estudiantes debe ser mayor a 0.")

