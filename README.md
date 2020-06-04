Multiproceso: python Morales_David_ExamenMultiprocessing.py

Para el multiproceso es importante usar el numero de cores que tiene el equipo, sino los resultados seran peores.
Para realizar esto primero dividi la lista de numeros en n pedazos (n es el numero de cores), una vez dividida la lista, 
realize lo mismo que en el secuencial, seleccionar el numero mayor y luego contar cuantas veces se repite. 
Una vez realizado esto sume los resultados que me devuelven todos los procesos para asi tener el numero de veces que se repite
el numero mayor en toda la lista.

![Alt text](img/procesos.png?raw=true "Procesos")


MPI: mpiexec -n 4 python Morales_David_ExamenMPI.py

Para MPI dividi la lista en el n pedazos (n es el numero de procesos -1), esto lo realice en el proceso 0 o Master, una vez que
divide envio cada pedazo de matriz al resto de procesos (trabajadores) y este proceso 0 quedara en espera de los resultados.
Para los trabajadores comienzan en espera hasta que reciban el pedazo de matriz asignado, una vez que reciben el pedazo de 
matriz realizo lo mismo que en el secuencial, contar cuantas veces se repite el numero mayor en ese pedazo de matriz. Una
vez hecho esto envio este conteo al proceso 0 o maestro que se encuentra en espera de estos resultados.
Volviendo al proceso 0 una vez que recibe el resultado suma esos conteos y asi tendriamos el conteo global de toda la lista.

![Alt text](img/mpi.png?raw=true "MPI")
