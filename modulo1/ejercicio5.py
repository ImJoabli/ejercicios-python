precio_producto = float(input("introduce el precio original del producto: "))

porcentaje_descuento = float(input("introduce el porcentaje de descuento del producto: "))

descuento = precio_producto * (porcentaje_descuento / 100)

precio_final = precio_producto - descuento

print("el precio del producto con el descuento aplicado es de: ", precio_final)