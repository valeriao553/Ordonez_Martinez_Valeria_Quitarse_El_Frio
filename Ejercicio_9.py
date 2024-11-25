print(" ")
print("Ordonez Martinez Valeria")
print(" ")
#Definimos la función contar_vocales
def contar_vocales(palabra):
    # Inicializamos un diccionario para contar las vocales
    vocales = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
     # Convertimos la palabra a minúsculas para hacer la comparación sin importar mayúsculas/minúsculas
    palabra = palabra.lower()
    #Bucle for
    for letra in palabra:
        # Si la letra es una vocal, aumentamos su contador
        if letra in vocales:
            vocales[letra] += 1
    #Devolvemos el resultado
    return vocales
#Pedimos al usuario que ingrese una palabra
palabra = input("Ingresa una palabra: ")
print(" ")
#Llamamos a la función
resultados = contar_vocales(palabra)
# Imprimimos los resultados
print("Número de veces que aparece cada vocal en la palabra:")
for vocal, cantidad in resultados.items():
    print(f"La vocal '{vocal}' aparece {cantidad} veces.")
    print(" ")
