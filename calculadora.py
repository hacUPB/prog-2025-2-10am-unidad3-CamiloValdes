'''
control = True  #Variable booleana 

while control == True:
    numero1 = int(input("Ingrese el primer numero"))
    numero2 = int(input("Ingrese el segundo numero"))
    print("S. sumar\n R. restar\n M. multiplicar\n D, dividir\n E. Salir")
    opcion = input("Elija una opción")
    match opcion:
            case 's':
                print("Modo 1 seleccionado: suma ")
                resultado = numero1 + numero2
            case 'R':
                print("Modo 1 seleccionado: resta")
                resultado = numero1 - numero2
            case 'M':
                print("Modo 3 seleccionado multiplicacion")
                resultado = numero1 * numero2
            case 'D':
                print("Modo 4 seleccionado; division")
                resultado = numero1 / numero2
            case 'E':
                control = False
            case _:
                print("Modo no válido")
    print(f"Resultado = {resultado}")
'''

# OTRA FORMA

#control = True  #Variable booleana 

while True:
    numero1 = int(input("Ingrese el primer numero"))
    numero2 = int(input("Ingrese el segundo numero"))
    print("S. sumar\n R. restar\n M. multiplicar\n D, dividir\n P, potencia\n E. Salir")
    opcion = input("Elija una opción")
    opcion = opcion.upper()                                               #Se convierte  todo a mayuscula 
    match opcion:
            case 's':
                print("Modo 1 seleccionado: suma ")
                resultado = numero1 + numero2
            case 'R':
                print("Modo 1 seleccionado: resta")
                resultado = numero1 - numero2
            case 'M':
                print("Modo 3 seleccionado multiplicacion")
                resultado = numero1 * numero2
            case 'D':
                print("Modo 4 seleccionado; division")
                resultado = numero1 / numero2
            case 'P':
                print("Modo 5 seleccionado; potencia")
                resultado = numero1 ** numero2
            case 'E':
                break
            case _:
                print("Modo no válido")
    print(f"Resultado = {resultado}")