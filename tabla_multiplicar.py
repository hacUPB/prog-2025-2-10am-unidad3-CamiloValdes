numero = int(input("Introduce un número entero positivo: "))

if numero <= 0:
    print("El número debe ser mayor que cero.")
else:
    contador = 1
    while contador <= 10:
        print(f"{numero} * {contador} = {numero * contador}")
        contador += 1
