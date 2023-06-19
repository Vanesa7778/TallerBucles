#Digite un número, si el numero supera a 10, multiplique los 10  primeros numeros, si no sumelos.

num = int(input("Ingrese un número: "))

if num > 10:
    resultado = 1
    for i in range(1, 11):
        resultado *= i
else:
    resultado = sum(range(1, num + 1))

print("El resultado es:", resultado)
