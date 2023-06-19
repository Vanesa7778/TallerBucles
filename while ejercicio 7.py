#Leer numeros enteros del teclado, hasta que el usuario ingrese el 0.Finalmente, mostrar la sumatoria de todos los numeros ingresados.

num = int(input("Ingrese un número entero (0 para terminar): "))
suma = 0

while num != 0:
    suma += num
    num= int(input("Ingrese un número entero (0 para terminar): "))

print("La sumatoria de los números ingresados es:", suma)
