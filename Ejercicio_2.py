print(" ")
print(" Ordonez Martinez Valeria")
print(" ")
def mas_larga(lista_palabras):
    # Empezamos a contar desde 0 en la lista
    palabra_larga = lista_palabras[0]
    
    for palabra in lista_palabras:
        # Se comparaque plabra es mas larga
        if len(palabra) > len(palabra_larga):
            palabra_larga = palabra
    #Devolver la palabra mas larga
    return palabra_larga

#Lista de palabras
palabras = ["Hola", "Gimnasio", "Verde", "Ozuna"]
#Llamamos a la funcion
resultado = mas_larga(palabras)
#Imprimimos la palabra mas larga
print("La palabra más larga es:", resultado)
print(" ")
