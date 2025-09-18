
print("Ingresa tu nombre y apellido")
nombre = input ()
print("Bienvenido: ")
print(nombre)
#Opción 2
print("Bienvenido: ", nombre)
#Calcular el IMC de esa persona
#Leer peso, altura
peso = input ("Ingresa tu peso en kg: ")
peso = float(peso)
altura = input ("Ingresa tu talla en metros: ")
altura = float(altura)
#Cálculos
imc = peso/altura**2
#Mostrar imc
print("Tu IMC = ", imc)

if imc < 18.5:
    mensaje = "Bajo peso"
elif imc < 25:
    mensaje = "Peso normal"
elif imc < 35:
    mensaje = "Obecidad tipo 1"
elif imc < 40:
    mensaje = "Obecidad tipo 2"
else:
    mensaje = "Obecidad extrema"

print (f"Paciente {nombre}, tiene un IMC de {imc:0.2f} y su condicion es {mensaje}." )



#Condicional simple 
#Se le pide al usuario que ingrese un numero entero y que muestre un mensaje si el numero es divisible por 3.

print("Ingrese el numero entero")
nume