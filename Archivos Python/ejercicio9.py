c = float(input("Ingrese la cantidad de capital a invertir: "))
i = float(input("Ingrese el porcentaje de interes anual: "))
a = int(input("Por cuantos años lo invertira: "))
print("Usted ganara $ " + str(round(c*(i/100 + 1) **a,2)))