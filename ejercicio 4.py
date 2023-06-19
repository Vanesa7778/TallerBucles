#Sumar pares desde 0 hasta el numero que indique el usuario for python

num= int(input("Ingrese un número: "))
suma_pares = 0

for i in range(0, num + 1, 2):
    suma_pares += i

print("el resultado de la suma de los numeros desde cero hasta  ", num, "es:", suma_pares)

