#hacer un programa que pida dos  numeros y muestre todos los numeros que van desde el primero al segundo, validar que el primer numero sea menor que el segundo.

num1 = int(input("Escriba el primer numero: "))
num2 = int(input("Escriba el segundo numero: "))

if num1 < num2:
    print("Los números en el rango son:")
    for i in range(num1, num2 + 1):
        print(i)
elif num1 > num2:
    print("El primer número debe ser menor que el segundo número.")
