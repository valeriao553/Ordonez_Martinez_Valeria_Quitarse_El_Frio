print(" ")
print("Ordonez Martinez Valeria")
print(" ")

def max_in_list(nums):
    # Empezamos a contar desde 0 en la lista
    max_num = nums[0]
    #Creamos buble for para saber cual es el numero mayor de la lista
    for num in nums:
        if num > max_num:
            max_num = num
    #Devolvemos el numero que sea mayor
    return max_num
# Lista de números
numeros = [13, 15, 11, 19, 12]
# Llamamos a la función para obtener el número más grande
resultado = max_in_list(numeros)
# Imprimimos el resultado
print("El número más grande es:", resultado)
print(" ")


