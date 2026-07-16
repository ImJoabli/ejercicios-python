a_pagar = float(input("Introduce el precio a pagar: "))
porcentaje_propina = float(input("Introduce el porcentaje de propina (ej: 10, 15, 20): "))

monto_propina = a_pagar * (porcentaje_propina / 100)
total = a_pagar + monto_propina

print("La propina es:", monto_propina)
print("El total a pagar es:", total)