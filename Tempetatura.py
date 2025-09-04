'''
Variables de entrada     
Nombre                  tipo   
Opción                  str
temperatura             float / punto flotante

Variables de salida
Nombre                  Tipo
conversion              float / punto flotante

Variable de control
opcion                   
'''

opcion = 'Z'                #Asigno un valor deiferente de Q  #Para que la condicon del while sea verdadera y entre si o si 
while opcion != 'Q':
    opcion = input("F. Fahrenheit a Celsius\n  C. Celciusa Faharenheit\n Q. Salir\n")
    opcion = opcion.upper()             #Para hacer mayuscula la letra que ingrese el usuario 
    if opcion != 'Q':
        temperatura = float(input("Ingrese la temperatura a convertir:"))
        match opcion:
            case 'F':
                conversion = (temperatura - 32) * (5/9)
                print(f"{temperatura}°F = {conversion}°C")
            case 'C':
                conversion = ((temperatura * 9/5) + 32)
                print(f"{temperatura}°C = {conversion}°F")
            case _:
                print("Opcion no valida")
    else:
        print("Saliendo del programa...")

