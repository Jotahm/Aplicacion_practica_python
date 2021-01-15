# CALCULADORA BÁSICA - PROYECTO N1

# Hagámoslo sencillo: calculadora sumatoria de dos ítems.

# Declaramos las variables
# Utilizamos input para que se guarde el dato introducido
num1 = input("Introduce un número: ")
num2 = input ("Introduce otro número: ")

# Realizamos la suma y guardamos resultado
res = float(num1) + float(num2) # Poniendo float permitimos operar con decimales ; en caso contrario, está concatenando dos cadenas

# Imprimimos el resultado y un mensaje de despedida

print ("La suma es:", res)
print ("Gracias por usarme")
