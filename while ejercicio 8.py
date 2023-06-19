#elabore un algoritmo que pida un numero entero mayor que 0 y que escriba sus divisores.Validar que el usuario haya ingresado un numero mayor a 0.


num = int(input("Ingrese un número  mayor que 0: "))

while num<= 0:
    print("El número es incorrecto debe ser mayor que 0. Inténtelo nuevamente.")
    num = int(input("Ingrese un número entero mayor que 0: "))

print("Los divisores de", num, "son:")
divisor = 1

while divisor <= num:
    if num % divisor == 0:
        print(divisor)
    divisor += 1
