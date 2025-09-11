'''
Crear una funcion llamda menu()
Parametros de entrada: Ninguno
Lo que realiza: Muestra un menu y muestra a el usuario que seleccione una opcion.
Valor de retorno: La opción seleccionada 
'''
def menu():
    print("1. Entrada\n 2. Platos fuertes\n 3. Bebidas\n 4. Postres\n 5. Salir")
    opcion = int(input("Elija una opción"))
    return opcion

def entradas():
    print("1. Pandebono\t\t$3000")
    print("2. Empanada\t\t$3500") 

def fuertes():
    print("1. Bandeja Paisa\t\t$20000")
    print("2. Mojarra\t\t30000")

def bebidas():
    print("1. Limonada natural\t\t$5000")
    print("2. Cocacola\t\t$4000")

def postres():
    print("1. Pie de limon\t\t$7000")
    print("2. Brownie con helado\t\t$9000")

#Funcion principal
def main():

    eleccion = menu()
    print(eleccion)

    match(eleccion):
        case 1:
            entradas()
        case 2:
            fuertes()
        case 3: 
            bebidas()
        case 4:
            postres()
        case _:
            print("Opcion no valida")

#Aqui se llama la funcion principal
if __name__ == "__main__":
    main()
