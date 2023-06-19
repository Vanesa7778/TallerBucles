#Hacer un programa que imprima la suma de todos los numeros impares desde 1 hasta n, y diga cuantos numeros impares hay.

numero= int(input("Ingrese un número: "))
suma = 0
contador = 0
num = 1

while num <= numero:
    suma += num
    contador += 1
    num += 2

print("La suma de los números impares es:", suma)
print("La cantidad de números impares es:", contador)
