#elabore un algoritmo que pida un numero entero mayor que cero y que escriba sus divisores.Validar que el usuario haya ingresado un numero mayor a cero.

numero = int(input("Ingrese un número entero mayor que cero: "))
if numero >=0:
  print("Los divisores de", numero, "son:")

  for i in range(1, numero + 1):
    if numero % i == 0:
        print(i)
elif numero <= 0:
    print("El número ingresado es incorrecto. Por favor, intente nuevamente.")
