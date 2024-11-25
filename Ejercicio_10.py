print(" ")
print("Ordonez Martinez Valeria")
print(" ")
#Definimos funcion
def es_bisiesto(año):
    #Agregamos la funcion para ver si el año es divisible por cuatr pero no por cien
    if año % 4 == 0:  
        if año % 100 != 0 or año % 400 == 0: 
            #Devolvemos valor true or false
            return True
    return False

# Pedimos al usuario que ingrese un año
año_usuario = int(input("Ingresa un año para saber si es bisiesto: "))

# Agregamos condicion para saber si el año es bisieto o no
if es_bisiesto(año_usuario):
    print(año_usuario, "es un año bisiesto.")
else:
    print(año_usuario, "no es un año bisiesto.")
    print(" ")


