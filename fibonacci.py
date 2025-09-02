'''
numero = int(input("Ingrese el número de terminos de la serie: "))
if numero <=0:
    print("Por favor, ingrese un número entero positivo")
elif numero == 1:
    print("Serie de fibonacci")
    print(0)
else:
    a = 0
    b = 1
    contador = 2 
    print("Serie de fibonacci")
    print(a)
    print(b)

    while contador < numero:
        siguiente = a + b
        print(siguiente)
        a = b
        b = siguiente
        contador += 1
'''

#Tabla de multiplicar 


numero = int(input("Ingrese el numero de la tala que desea"))
if numero <= 0:
    print("El número debe ser mayor que cero.")
else:
    contador = 1
    while contador <= 15:
        print(f" {numero}x{contador}={numero * contador}")
        contador += 1
        