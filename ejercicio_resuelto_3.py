
#Crea un programa que dada una lista de números enteros:

#Imprima todos aquellos que sean menores que 10.
#Imprima todos aquellos que sean múltiplos de 5.
#Extra:

#Repite los ejercicios anteriores pero en vez de imprimir uno a uno los valores, crea una nueva lista para cada uno que contengan los elementos en cuestión y, posteriormente, imprímela.

menores = []
multiplos = []
lista = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]

for elemento in lista:
    if elemento < 10:
        menores.append(elemento)
        
    if elemento % 5 == 0:
        multiplos.append(elemento)
       
print ("Los números múltiplos de 5 son: ", multiplos)
print ("Los números menores de 10 son: ", menores)
