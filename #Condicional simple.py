#Condicional simple 
#Se le pide al usuario que ingrese un numero entero y que muestre un mensaje si el numero es divisible por 3.

numero = int(input("Ingrese un numero entero:"))
residuo = numero % 3

if residuo == 0:
    mensaje = "El numero es divisible por 3"
print(mensaje)