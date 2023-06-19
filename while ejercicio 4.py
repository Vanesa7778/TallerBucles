#hacer un programa que pida dos numeros y muestre todos los numeros que van desde el primero al segundo, validar que el primer numero sea menor que el segundo.

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

if num1 < num2:
    
    contador = num1
    
    print("Los números en el rango son:")
    while contador <= num2:
        print(contador)
        contador += 1
elif num1 > num2:
        print("El primer número debe ser menor que el segundo número.")


