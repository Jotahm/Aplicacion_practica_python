"""
Crea un programa que:

Pida al usuario un número por pantalla.
Calcule todos los divisores de ese número y los muestre por pantalla en formato lista [].
Calcule solo los divisores pares de ese número y los muestre en el mismo formato.
"""

numero = input("Por favor, introduce un número y te calculo sus divisores:\n ")
numero = int(numero)
divisores = []
divisores_pares = []

for elemento in range (1, numero + 1):
     if 100 % elemento == 0:
        divisores.append(elemento)
     if numero % elemento == 0:
         if elemento % 2 == 0:
             divisores_pares.append(elemento)
        
        
print ("Los divisores del número ", numero, "son los siguientes: ", divisores)

print ("Los divisores pares del número ", numero, "son los siguientes: ", divisores_pares)
