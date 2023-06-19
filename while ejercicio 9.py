#elabore un algoritmo que permita ingresar n numeros de temperaturas y escriba la temperatura mas alta, las mas baja y la temperatura promedio.

n = int(input("Ingrese la cantidad de temperaturas: "))

if n > 0:
    
    contador = 1
    temperatura = float(input("Ingrese la temperatura {}: ".format(contador)))
    temperaturaMaxima = temperatura
    temperaturaMinima = temperatura
    sumaTemperaturas = temperatura

    while contador < n:
        contador += 1
        temperatura = float(input("Ingrese la temperatura {}: ".format(contador)))
        sumaTemperaturas += temperatura

        if temperatura > temperaturaMaxima:
            temperaturaMaxima = temperatura

        elif temperatura < temperaturaMinima:
            temperaturaMinima = temperatura

    temperaturaPromedio = sumaTemperaturas / n

    print("Temperatura más alta:", temperaturaMaxima)
    print("Temperatura más baja:", temperaturaMinima)
    print("Temperatura promedio:", temperaturaPromedio)

else:
    print("La cantidad de temperaturas debe ser mayor a 0.")