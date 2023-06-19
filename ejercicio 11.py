#elabore un algoritmo que pregunte cuantas temperaturas se van a introducir, pida esas temperaturas, y escriba la temperatura mas alta, la mas baja y la temperatura promedio.

cant= int(input("Ingrese la cantidad de temperaturas a introducir: "))

temperaturas = []

for i in range(cant):
    temperatura = float(input("Ingrese la temperatura {}: ".format(i + 1)))
    temperaturas += [temperatura]

temperaturaMaxima = max(temperaturas)
temperaturaMinima = min(temperaturas)
temperaturaPromedio = sum(temperaturas) / cant

print("Temperatura más alta:", temperaturaMaxima)
print("Temperatura más baja:", temperaturaMinima)
print("Temperatura promedio:", temperaturaPromedio)
