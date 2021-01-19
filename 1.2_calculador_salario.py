# EJERCICIO PRÁCTICO

# Escriba un programa para recordarle al usuario las horas y la tarifa por hora para calcular salario bruto

horas = input("¿Cuántas horas has trabajado?: ")
salario = input("¿Cual es el honorario por cada hora trabajada?: ")
horas = float(horas)

salario_total = float(horas) * float(salario)


print ("Tu salario es de " + str(salario_total) + " euros. ")
print ("Gracias por usarme. Pasa un buen día.")