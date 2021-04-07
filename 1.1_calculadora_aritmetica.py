# CALCULADORA
# EN PROCESO, ¿Qué más funciones podríamos añadirle a la calculadora?

# Declaramos las variables
# Utilizamos input para que se guarde el dato introducido
num1 = input("Introduce un número: ")
signo = input ("Introduce signo aritmético: ")
num2 = input ("Introduce otro número: ")

if signo == "+": # declarando la suma
    res = int(num1) + int(num2)

if signo == "-": # declarando la resta
    res = int(num1) - int(num2)

if signo == "*": # declarando la multiplicación
    res = int(num1) * int(num2)

if signo == "/": # declarando la división
    res = int(num1) / int(num2)

print ("El resultado es:", res)
print ("Gracias por usarme")
