caramelos = int(input("Introduce la cantidad de caramelos: "))

gente = int(input("Introduce la cantidad de gente a la que se repartiran los caramelos: "))

division_resultado = caramelos // gente

resto_division = caramelos % gente 

print("en total son: ", division_resultado, "de caramelos, y sobran", resto_division, "caramelos" )