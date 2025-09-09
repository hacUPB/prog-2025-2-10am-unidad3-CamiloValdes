# Primera idea 
En el mantenimiento aeronáutico, los manuales se organizan según el ATA 100, que clasifica los sistemas de la aeronave en capítulos numerados.
El programa debe permitir al usuario ingresar el número de un capítulo ATA y mostrar el sistema correspondiente.
El usuario podrá realizar consultas múltiples dentro de esta opción, hasta que decida salir digitando un número especial (por ejemplo, 0).
De esta manera, el programa ayudará al estudiante a familiarizarse con la clasificación ATA y la importancia de cada sistema en el avión.

# Segunda idea 
Un avión entra en pérdida (stall) cuando su velocidad es tan baja que las alas ya no generan suficiente sustentación para contrarrestar el peso.
El programa pedirá al usuario ingresar los datos del avión:

Peso total de la aeronave, Superficie alar, coeficiente de sustentación máximo, densidad del aire.

Luego calculará la velocidad de pérdida con la fórmula correspondiente.
El usuario también ingresará una velocidad real de vuelo, y el programa determinará:
Si la velocidad es mayor que la de pérdida, el avión está en condiciones seguras.
Si es igual o menor, el avión entraría en pérdida.
El programa repetirá el proceso en un ciclo hasta que el usuario decida salir.

| Variable   | Tipo de variable | Comentario                                                                    |
| ---------- | ---------------- | ----------------------------------------------------------------------------- |
| `W`        | Entrada          | Peso total del avión ingresado por el usuario (en Newtons o kg).              |
| `S`        | Entrada          | Superficie alar ingresada por el usuario (en m²).                             |
| `CLmax`    | Entrada          | Coeficiente máximo de sustentación, ingresado por el usuario.                 |
| `rho`      | Entrada          | Densidad del aire, ingresada por el usuario (en kg/m³).                       |
| `V_stall`  | Cálculo/Salida   | Velocidad de pérdida calculada con la fórmula.                                |
| `V_actual` | Entrada          | Velocidad actual del avión, pedida al usuario en cada iteración.              |
| `opcion`   | Condicional      | Variable que controla si el usuario desea continuar o terminar la simulación. |
| `estado`   | Salida           | Mensaje que indica si el avión vuela seguro o entra en pérdida.               |
| `i`        | Control de bucle | Contador opcional para las iteraciones (ej. segundos de simulación).          |


# Tercera idea La sustentación es la fuerza aerodinámica que permite que un avión se mantenga en vuelo.
El programa solicitará al usuario los siguientes datos:

Velocidad de vuelo.

Altitud (para calcular una densidad del aire aproximada).

Superficie alar, coeficiente de sustentación, peso total de la aeronave.

Con estos datos, calculsará la fuerza de sustentación. Luego comparará este valor con el peso del avión y mostrará el estado de vuelo:
Si la sustentación es mayor que el peso, el avión asciende.
Si la sustentación es igual al peso, el avión se mantiene en vuelo recto y nivelado.
Si la sustentación es menor que el peso, el avión desciende.
El usuario podrá repetir el cálculo varias veces, probando diferentes condiciones de vuelo, hasta que decida salir.
