print(" ")
print("Ordonez Martinez Valeria")
print(" ")
# Definimos la funcion
def contar_mayusculas(cadena):
    contador = 0  # Creamos un contador que empieza en 0
    
    # creamos bucle for
    for letra in cadena:
        # Si la letra es mayúscula, sumamos 1 al contador
        if letra.isupper():
            contador += 1
    #Devolvemos resultado
    return contador

#Solicitamos al usuario ingresar el texto
cadena = input("Ingresar un texto: ")
print(" ")
#Llamamos a la función y guardamos el resultado
resultado = contar_mayusculas(cadena)
# Imprimir el reslutado de las palabra que hay
print("El texto tiene", resultado, "letras mayúsculas.")
print(" ")

