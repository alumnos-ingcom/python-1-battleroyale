# ¡Testing Battle Royale!

Para que esto funcione correctamente, es necesario compensar las ideosincracias individuales.

Aun con el enunciado y función dada, hay suficientes variaciones como para que sea neceario adaptar los tests a cada implementación individual.

## Adaptaciones necesarias

En el ejercicio 1, algunos corrigieron `farrenheit` por `farenheit`, lo que hace que los tests no sean _exactamente_ intercambiables.

Esto lo pueden arreglar usando los sobrenombres en `import`: `from src.ejercicio1 import farrenheit as farenheit` o viceversa dependiendo de cual sea el cambio.

Uno de los conjuntos de tests, no sigue la consigna con respecto al nombre de los archivos por lo que hacer funcionar los tests de los demas será mas laborioso (pero usar `git mv` es mucho mas eficiente ;-) )

Cualquier cosa, lo conversamos en el canal #battleroyale.

## ¿Como determinamos al ganador?

Salvando las diferencias con respecto a las adaptaciones, el que mas tests pase _sin modificarlos_ .

Por otro lado, me gustaria que evaluen cada test, indicando con que puede ser mejorado (en el `docstring` del módulo o comentario arriba de los tests.)

## Uso de los tests

Para aquellos que no tengan terminado el Trabajo Practico, tener esta cantidad de tests es fantastico para que sus algoritmos sean más solidos.
