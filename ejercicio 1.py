#suma de los n primeros numeros, solicite al usuario el numero de elementos a sumar.
num  = int(input("Ingrese la cantidad de elementos a sumar: "))

if num > 0:
    suma = 0
    for i in range(1, num + 1):
        suma += i
    
elif num < 0:
    
    print("El número de elementos debe ser positivo.")

    