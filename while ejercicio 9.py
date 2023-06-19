#elabore un algoritmo que permita ingresar n numeros de temperaturas y escriba la temperatura mas alta, las mas baja y la temperatura promedio.



n = int(input("Ingrese la cantidad de temperaturas: "))
suma_temperaturas = 0
contador = 0

while contador < n:
    temperatura = float(input("Ingrese una temperatura: "))
    suma_temperaturas += temperatura

    if contador == 0:
        temp_maxima = temperatura
        temp_minima = temperatura
    else:
        if temperatura > temp_maxima:
            temp_maxima = temperatura
        elif temperatura < temp_minima:
            temp_minima = temperatura

    contador += 1

promedio = suma_temperaturas / n

print("La temperatura más alta es:", temp_maxima)
print("La temperatura más baja es:", temp_minima)
print("La temperatura promedio es:", promedio)
