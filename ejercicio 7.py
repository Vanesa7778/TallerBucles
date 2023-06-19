#algoritmo que pregunte al usuario que tabla de multiplicar quiere ver, debe generar la tabla de multiplicar desde cero hasta 10.

num = int(input("Ingrese el numero de que tabla de multiplicar quiere ver "))

print("Tabla de multiplicar del", num, ":")
for i in range(11):
    resultado = num * i
    print(num, "x", i, "=", resultado)
