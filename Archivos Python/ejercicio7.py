peso = input ("Ingrese su peso (en kg): ") 
estatura = input ("Ingrese su estatura: ")
imc = round(float(peso)/float(estatura)**2,2)
print ("Tu indice de masa corporal es :" + str(imc))
