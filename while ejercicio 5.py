monto = float(input("Ingrese el monto de la factura (0 para finalizar): "))
totalPagar = 0

while monto != 0:
    totalPagar += monto
    monto = float(input("Ingrese el monto de la factura (0 para finalizar): "))

if totalPagar > 1000:
    descuento = totalPagar * 0.1
    totalPagar -= descuento

print("Total a pagar: $", totalPagar)
