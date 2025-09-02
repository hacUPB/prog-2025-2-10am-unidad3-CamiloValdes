'''
for cont in range (5, 20, 1):  #Genera la secuencia de numeros
    print(cont)
'''
# No se pueden ingresar valores negativos
# No se puede pasar hasta que no ingrese en numero positivo
'''
numero = int(input("Ingrese un numero entero positivo"))
while numero < 0:
    numero = int(input("Ingrese un numero entero positivo"))

acum = 0
for cont in range (1, numero, 2): 
    if numero % 2 == 0: 
        acum = acum + cont
    print(f"La suma de lois pares es: {acum}")
'''

mensaje = "Universidad Pontificia Bolivariana"
veces = int(input("Ingrese el numero de veces que quiere que se imprima el mensaje"))
for cont in range (veces ):
    print(f"{cont+1}. {mensaje}")
