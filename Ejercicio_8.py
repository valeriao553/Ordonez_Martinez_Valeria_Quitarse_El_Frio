print(" ")
print("Ordonez Martinez Valeria")
print(" ")
# Lista con nombres de mis amigibbys
nombres = ["Maria", "Alexa", "Rodrigo", "Paola", "Angel", "Valentin", "Jose", "Yael", "Dayana", "Brianna"]
# Pedimos al usuario que ingrese una letra
letra = input("Ingresa una letra para ver cuántos nombres empiezan con ella: ")
# Inicializamos un contador en 0
contador = 0
#Bucle For
for nombre in nombres:
    if nombre[0].lower() == letra.lower():  # Comparamos la primera letra del nombre con la letra ingresada
        contador += 1
# Imprimimos el resultado
print("Hay", contador, "nombres que empiezan con la letra", letra)
print(" ")