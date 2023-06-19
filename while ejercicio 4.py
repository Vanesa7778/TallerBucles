#hacer un programa que pida dos numeros y muestre todos los numeros que van desde el primero al segundo, validar que el primer numero sea menor que el segundo.

num1= int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

while num1>= num2:
    print("El primer número debe ser menor que el segundo. Inténtelo nuevamente.")
    num1 = int(input("Ingrese el primer número: "))
    num2= int(input("Ingrese el segundo número: "))
    
numero_actual = num1
print("Los números son:")
while numero_actual <= num2:
    print(numero_actual)
    numero_actual += 1




