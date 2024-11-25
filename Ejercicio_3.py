print(" ")
print("Ordonez Martinez Valeria")
print(" ")
def filtrar_palabras(lista, n):
    # Lista vacía para las palabras que cumplen con la condición
    resultado = []
    #Crear bucle for 
    for palabra in lista:
        # Si la palabra tiene más de n en la palbara vamos a regresar el resultado
        if len(palabra) > n:
            resultado.append(palabra)
     # Devolvemos el resultado
    return resultado
#Lista de palabras
lista_de_palabras = ["morado", "rojo", "verde", "azul", "negro"]
n = 5
#Llamamos a la función 
palabras_filtradas = filtrar_palabras(lista_de_palabras, n)
#Imprimimos el resultado
print("Palabras con más de", n, "caracteres:", palabras_filtradas)
print(" ")
