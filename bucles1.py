'''
numero = 100
while numero >=0:
    print(numero)
    numero -= 5    #numero = numero - 5
'''

# Solicitar 2 números enteros al usuario e imprimir los pares entre ellos


numero1 = int(input("Ingrese el primer numero"))
numero2 = int(input("Ingrese el segundo numero"))

if numero1 > numero2:
    mayor = numero1
    menor = numero2
else:
    mayor = numero2
    menor = numero1
'''
while menor <= mayor:
    if menor % 2 == 0:
        print(menor)
    menor += 1
'''
if menor % 2 == 1:
    menor += 1
while menor <= mayor:
    print(menor)
    menor += 2
    
