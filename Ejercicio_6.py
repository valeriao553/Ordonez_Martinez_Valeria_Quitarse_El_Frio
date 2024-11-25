print(" ")
print("Ordonez Martinez Valeria")
print(" ")
# Pedimos el
año = int(input("Ingresar el año actual: "))
print(" ")
# Pedimos al usuario que ingrese sus dator
persona1 = input("Ingresa el nombre de la primera persona: ")
año_nacimiento1 = int(input("Ingrese el año es que nació " + persona1 + ": "))
print(" ")
persona2 = input("Ingresa el nombre de la segunda persona: ")
año_nacimiento2 = int(input("Ingrese el año es que nació " + persona2 + ": "))
print(" ")
persona3 = input("Ingresa el nombre de la tercera persona: ")
año_nacimiento3 = int(input("Ingrese el año es que nació " + persona3 + ": "))
print(" ")
#restamos el año actual al año de nacimiento de las personas
edad1 = año  - año_nacimiento1
edad2 = año  - año_nacimiento2
edad3 = año  - año_nacimiento3
#Imprimimos los resultados
print(persona1 + " cumplirá " + str(edad1) + " años en " + str(año))
print(persona2 + " cumplirá " + str(edad2) + " años en " + str(año))
print(persona3 + " cumplirá " + str(edad3) + " años en " + str(año))
print(" ")
