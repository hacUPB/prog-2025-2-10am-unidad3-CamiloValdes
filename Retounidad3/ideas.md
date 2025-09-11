# Primera idea 
En el mantenimiento aeronáutico, los manuales se organizan según el ATA 100, que clasifica los sistemas de la aeronave en capítulos numerados.
El programa debe permitir al usuario ingresar el número de un capítulo ATA y mostrar el sistema correspondiente.
El usuario podrá realizar consultas múltiples dentro de esta opción, hasta que decida salir digitando un número especial (por ejemplo, 0).
De esta manera, el programa ayudará al estudiante a familiarizarse con la clasificación ATA y la importancia de cada sistema en el avión.

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
| CLmax    | Entrada          | Coeficiente máximo de sustentación, ingresado por el usuario.                  |
| rho       | Entrada          | Densidad del aire, ingresada por el usuario (en kg/m³).                        |
| V_stall   | Cálculo/Salida   | Velocidad de pérdida calculada con la fórmula.                                 |
| V_actual | Entrada          | Velocidad actual del avión, pedida al usuario en cada iteración.               |
| estado    | Salida           | Mensaje que indica si el avión vuela seguro o entra en pérdida.                |
| i         | Control de bucle | Contador de las iteraciones (ej. segundos de simulación).                      |
| continuar | Condicional      | Variable de control para decidir si el usuario sigue o finaliza la simulación. |

```
Inicio

  Mostrar "Simulación de velocidad de pérdida (Stall Speed)"

  Leer W
  Leer S
  Leer CLmax
  Leer rho

  Llamar a función calcular_stall(W, S, CLmax, rho)
  Guardar resultado en V_stall

  Mostrar "La velocidad de pérdida calculada es:", V_stall

  Inicializar i = 1

  Mientras (verdadero)
      Mostrar "Iteración", i
      Leer V_actual

      Si V_actual == 0 entonces
          Mostrar "Simulación terminada por el usuario"
          Salir del bucle

      Si V_actual > V_stall entonces
          Mostrar " Seguro: el avión está por encima de la velocidad de pérdida."
      Sino
          Mostrar "PRECAUCIÓN VELOCIDAD DE PERDIDA, AUMENTAR LA VELOCIDAD"
      Fin Si

      Incrementar i = i + 1
  Fin Mientras

Fin

Función calcular_stall(W, S, CLmax, rho):
    devolver sqrt( (2*W) / (rho*S*CLmax) )
```








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

  Mostrar "Simulación de ascenso del avión por 10 segundos"

  Leer potencia_inicial
  altitud = 0
  potencia = potencia_inicial

  Para t desde 1 hasta 10 hacer
      Mostrar "Segundo ", t
      Mostrar "Potencia actual: ", potencia, "%"
      Mostrar "Altitud actual: ", altitud, "m"

      Calcular densidad = 1.225 * exp(-altitud/10000)

      Llamar a función calcular_ROC(potencia, densidad)
      Guardar resultado en roc

      altitud = altitud + roc

      Mostrar "Nueva altitud: ", altitud

      Si roc < 1 entonces
          Mostrar "¡Advertencia! El avión casi no asciende."
      Fin Si

      Mostrar "¿Desea cambiar la potencia?"
      Mostrar "1. Aumentar potencia"
      Mostrar "2. Mantener potencia"
      Mostrar "3. Disminuir potencia"
      Leer decision

      Si decision == 1 entonces
          potencia = potencia + 10
      Sino si decision == 3 entonces
          potencia = potencia - 10
      Fin Si

  Fin Para

  Mostrar "Simulación terminada. Altitud final: ", altitud, "m"

Fin

Función calcular_ROC(potencia, densidad):
    devolver (potencia * densidad) / 100
```
