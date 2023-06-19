#digite un numero, si el numero supera a 10 , multiplique los 10 primeros numeros , sino , sumelos.

numero = int(input("Ingrese un número: "))

if numero > 10:
    resultado = 1
    contador = 1
    while contador <= 10:
        resultado *= contador
        contador += 1
    print("El resultado de multiplicar los 10 primeros números es:", resultado)
else:
    resultado = 0
    contador = 1
    while contador <= 10:
        resultado += contador
        contador += 1
    print("El resultado de sumar los 10 primeros números es:", resultado)
