# EJERCICIO PRÁCTICO
# Crea un programa en el que se calcule el salario de un trabajador en el que las primeras 40 horas cobra "p" y de ahí en adelante "p*1.5" la hora. Utiliza los siguientes conceptos:

#def computepay(horas, retribución):
    #return 42.37

#hrs = input("Ingrese horas:")
#p = computepay(10,20)
#print("Paga",p)

horas = input ("¿Cuantas horas has trabajado?: ")
paga = input ("¿A cuánto se paga cada hora?: ")
h = float (horas)
p = float (paga)

def computepay(h,p):
    if h > 40:
        salario = (40*p + ((h-40) * 1.5) * p)
        print (salario)
    else:
        salario = h* p
        print (salario)
    
    return salario

p = computepay(h,p)
