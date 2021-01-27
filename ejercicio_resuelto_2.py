# Crea un programa que:

# Le pregunte al usuario un número.
# Le indique al usuario si el número en cuestión es par o impar.
# Extra: Meteremos algunas cosas extra que quedarán referidas con comentarios

# El programa sencillo sería el siguiente:
#numero = input("Introduce el número que quieres comprobar: ")
#numero = int(numero)

#if numero % 2 == 0:
        print ("Tu número es par. ")
#else:
        print ("Tu número es impar. ")
    
# Aplicando algunas técnicas más, podemos hacer algo más elaborado: 



print ("Bienvenido a 'par o impar'. \n") # Mensaje de bienvenida al programa
print ("Utiliza 'hecho' para terminar\n") # EXTRA: Vamos a crear un bucle. Cuando queramos terminar introduciremos "hecho"
while True: # creamos el bucle
    numero = input("Introduce el número que quieres comprobar: ")
    if numero == "hecho":
        print ("Gracias por usarme. Hasta pronto.")
        break # si introducimos "hecho" el bucle finaliza
    try: # con este try, evitamos fallo de que el usuario introduzca algo que no sea una  cifra numérica
        numero = int(numero)
    except:
        print ("Por favor, introduce un número para comprobar o la palabra 'hecho' para terminar.")
        continue # continua el bucle
    numero = int(numero)
    if numero == 0: 
        print ("No sé, pregúntale a un matemático ;D ")
    elif numero % 2 == 0:
        print ("Tu número es par. ")
    else:
        print ("Tu número es impar. ")
