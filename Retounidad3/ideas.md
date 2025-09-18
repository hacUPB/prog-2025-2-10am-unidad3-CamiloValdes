# Simulación de la velocidad de perdida
El programa simulará el vuelo de una aeronave en el cual verificará en cada instante se la aeronave se encentra en condiciones seguras o si está entrando en perdida.
El  usuario debe ingresar los parametros basicos de la aeronave: Peso total, superficie alar, coeficiente de sustentación máximo y la densidad del aire por la que se este volando.
El programa calcula la velocidad minima de perdida de la aeronave
Despues se inicia una simulacion paso por paso (cada segundo de vuelo) en cada intervalo se pedira la velocidad actual de la aeronave y el programa la comparará con la velocidad de pérdida. Si la velocidad es mayor al stall speed, el avion está volando de forma segura pero si es igual o menor la aeronave entra en perdida y se debe de mostrar el siguiente mensaje "PRECAUCIÓN VELOCIDAD DE PERDIDA, AUMENTAR LA VELOCIDAD"
La simulacion se debe repetir hasta que el usuario lo determine 
Nota: Si se da el caso de perdida, el programa debe poder volver a hacer el proceso para confirmar que ya no hay velocidad de perdida, NO debe terminar si hay caso de perdida.


| Variable    | Tipo de variable | Comentario                                                                     |
| ----------- | ---------------- | ------------------------------------------------------------------------------ |
| W         | Entrada          | Peso total del avión ingresado por el usuario (en Newtons o kg).               |
| S         | Entrada          | Superficie alar ingresada por el usuario (en m²).                              |
| Cl   | Entrada          | Coeficiente máximo de sustentación, ingresado por el usuario.                  |
| D     | Entrada          | Densidad del aire, ingresada por el usuario (en kg/m³).                        |
| V_stall   | Cálculo/Salida   | Velocidad de pérdida calculada con la fórmula.                                 |
| V_actual | Entrada          | Velocidad actual del avión, pedida al usuario en cada iteración.               |
| estado    | Salida           | Mensaje que indica si el avión vuela seguro o entra en pérdida.                |
| contador        | Control de bucle | Contador de las iteraciones (ej. segundos de simulación).                      |


```
Inicio
    contador = 0
    Mientras contador < 10 :
          Escribir "Ingrese el peso:"
            leer W
          Escribir "Ingrese la superficie alar:"
            leer S
          Escribir "Ingrese el Coeficiente de sustentacion:"
            leer Cl
          Escribir "Ingrese la densidad del aire:"
            leer D
          V_stall = sqrt( (2*W) / (D*S*Cl))
          Lista[contador] = V_stall
          contador = contador + 1
            Escribir "Ingrese 0 si desea salir ó ingrese el valor de la velocidad para continuar"
            Escribir "Ingrese el valor de velocidad"
            leer V_actual
            Si V_actual == 0 entonces
              Escribir "Saliendo"
              Fin bucle
            Sino
              Si V_actual > V_stall entonces
                Escribir " Seguro: el avión está por encima de la velocidad de pérdida."
              Sino
                Escribir "PRECAUCIÓN VELOCIDAD DE PERDIDA, AUMENTAR LA VELOCIDAD"
              Fin Si
            Fin Si
    Fin Mientras
    Desde contador = 0 hasta contador = 10
         Escribir "valores registrados:"
         Escribir Lista[contador]
    Fin Desde
Fin

Función calcular_stall(W, S, CLmax, rho):
    devolver sqrt( (2*W) / (rho*S*CLmax) )
```
#Pedimos a la IA la base para el codigo sin, embargo este no es el codigo que nos dio la IA







# Simulación de Altitud y Potencia de Motor durante Ascenso
Cuando un avión asciende, la densidad del aire disminuye y, por tanto, la potencia disponible del motor también se reduce. Esto afecta directamente la capacidad del avión para seguir ganando altitud.
El reto será simular 10 segundos de ascenso en los que el usuario decide si aumentar, mantener o disminuir la potencia del motor, y observar cómo cambia la altitud alcanzada.



| Variable   | Tipo de variable | Comentario                                                                 |
| ---------- | ---------------- | -------------------------------------------------------------------------- |
| t        | Control de bucle | Contador de segundos de la simulación (1 a 10).                            |
| altitud  | Cálculo/Salida   | Altitud alcanzada en cada segundo (m).                                     |
| potencia | Entrada          | Potencia actual del motor (%), definida y ajustada por el usuario.         |
| densidad | Cálculo          | Densidad del aire según altitud, usando fórmula simplificada.              |
| roc      | Cálculo          | Tasa de ascenso (m/s), calculada según la potencia y densidad.             |
| decision | Entrada          | Elección del usuario: aumentar, mantener o disminuir potencia.             |
| estado   | Condicional      | Indica si el avión sigue ascendiendo bien o si se estanca (poca potencia). |


```
Inicio

  Escribir "Simulación de ascenso del avión por 10 segundos"

  Leer potencia_inicial
  altitud = 0
  potencia = potencia_inicial

  Para t desde 1 hasta 10 hacer
      Escribir "Segundo ", t
      Escribir "Potencia actual: ", potencia, "%"
      Escribir "Altitud actual: ", altitud, "m"

      Calcular densidad = 1.225 * exp(-altitud/10000)

      Llamar a función calcular_ROC(potencia, densidad)
      Guardar resultado en roc

      altitud = altitud + roc

      Escribir "Nueva altitud: ", altitud

      Si roc < 1 entonces
          Mostrar "¡Advertencia! El avión no asciende lo suficiente."
      Fin Si

      Escribir "¿Desea cambiar la potencia?"
      Escribir "1. Aumentar potencia"
      Escribir "2. Mantener potencia"
      Escribir "3. Disminuir potencia"
      Leer decision

      Si decision == 1 entonces
          potencia = potencia + 10
      Sino si decision == 3 entonces
          potencia = potencia - 10
      Fin Si

  Fin Para

  Escribir "Simulación terminada. Altitud final: ", altitud, "m"

Fin

Función calcular_ROC(potencia, densidad):
    devolver (potencia * densidad) / 100

```
#Uso de IA aplicado




| t (s) | Potencia (%) | Altitud antes (m) | Densidad | ROC (m/s) | Altitud después (m) | Decisión usuario | Comentario          |
| ----- | ------------ | ----------------- | -------- | --------- | ------------------- | ---------------- | ------------------- |
| 1     | 50           | 0                 | 1        | 1         | 1                   | Mantener         | Asciende            |
| 2     | 50           | 1                 | 1        | 1         | 2                   | Aumentar         | —                   |
| 3     | 60           | 2                 | 1        | 1         | 3                   | Mantener         | Asciende más rápido |
| 4     | 60           | 3                 | 1        | 1         | 4                   | Disminuir        | —                   |
| 5     | 50           | 4                 | 1        | 1         | 5                   | Mantener         | —                   |
| 6     | 50           | 5                 | 1        | 1         | 6                   | Mantener         | —                   |
| 7     | 50           | 6                 | 1        | 1         | 7                   | Aumentar         | —                   |
| 8     | 60           | 7                 | 1        | 1         | 8                   | Mantener         | —                   |
| 9     | 60           | 8                 | 1        | 1         | 9                   | Disminuir        | —                   |
| 10    | 50           | 9                 | 1        | 1         | 10                  | Mantener         | —                   |


#Uso de IA aplicado

# Simulación angulo de ataque - lifting y drag

El programa simulara 10 segundos de vuelo de una aeronave, el usuario podra aumentar o disminuir o mantener constante la velocidad. En cada segundo el drag, el lifting y el angulo de ascenso. Si el angulo de ascenso se vuelve negativo se debe alertar que el avion no puede seguir subiendo

| Variable | Tipo de variable              | Comentario                                                                         |
| -------- | ----------------------------- | ---------------------------------------------------------------------------------- |
| contador | De control (entero)           | Cuenta los segundos de simulación                                                  |
| W        | Entrada (entero)              | Peso del avión                                                                     |
| rho      | Entrada (entero)              | Densidad del aire                                                                  |
| S        | Entrada (entero)              | Superficie alar                                                                    |
| CL       | Entrada (entero)              | Coeficiente de sustentación                                                        |
| CD       | Entrada (entero)              | Coeficiente de arrastre                                                            |
| V        | Entrada/actualizable (entero) | Velocidad del avión, cambia según decisión del usuario                             |
| L        | Cálculo (entero)              | Sustentación                                                                       |
| D        | Cálculo (entero)              | Arrastre                                                                           |
| theta    | Cálculo (entero aproximado)   | Ángulo de ascenso en grados                                                        |
| decision | Condicional (entero)          | Indica si el usuario aumenta, disminuye, mantiene la velocidad o sale del programa |


Inicio
    Definir función calcular_angulo(rho, V, S, CL, CD, W):
        L = (rho * V^2 * S * CL) // 2
        D = (rho * V^2 * S * CD) // 2
        relacion = (L - D) // W
        theta = arctan(relacion) * (180 / pi)
        Retornar theta

    contador = 0
    Leer W, rho, S, CL, CD, V

    Mientras contador < 10 hacer:
        theta = calcular_angulo(rho, V, S, CL, CD, W)
        Escribir segundo actual, velocidad, ángulo

        Si theta < 0 entonces
            Mostrar " El avión no puede seguir ascendiendo"
            Terminar bucle

        Mostrar "Ingrese 1 para aumentar velocidad, 2 para disminuir, 3 para mantener, 0 para salir"
        Leer decision

        Si decision == 0 entonces
            Mostrar " Saliendo de la simulación"
            Terminar bucle
        Sino si decision == 1 entonces
            V = V + 10
        Sino si decision == 2 entonces
            V = V - 10
        Sino si decision == 3 entonces
            V = V (se mantiene igual)

        contador = contador + 1
    Fin mientras
Fin
