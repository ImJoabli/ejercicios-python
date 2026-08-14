edad = int(input("Introduce tu edad: "))

precio_entrada = float(input("Introduce el precio de la entrada al Cine: "))

if edad <= 12 or edad >= 65:
    descuento = (precio_entrada * 50) / 100

    print("dado a que tu edad es ", edad, ", el precio a pagar será de:", precio_entrada - descuento)

else: 
    print("tendrás que pagar: ", precio_entrada)

    