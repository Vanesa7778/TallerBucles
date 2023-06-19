#Hacer un programa que imprima la suma de todos los numeros impares desde 1 hasta n , y diga cuantos numeros impares hay.

num = int(input("Ingrese un número: "))
sumaImpares = 0
cantidadImpares = 0

for i in range(1, num + 1, 2):
    sumaImpares += i
    cantidadImpares += 1

print("La suma de todos los numeros impares desde 1 hasta", num, "es:", sumaImpares)
print("La cantidad de números impares es:", cantidadImpares)
