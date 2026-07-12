horas = int(input("introduce un número de horas: "))
minutos = int(input("introduce un número de minutos: "))
segundos = int(input("introduce un número de segundos: "))

total_segundos = (horas * 3600) + (minutos * 60) + segundos

print("en total son: ", total_segundos, "segundos",)