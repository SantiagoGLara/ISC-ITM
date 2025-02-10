# LENGUAJES DE INTERFAZ
u1 examen 100%

u2-u4 practicas

practicas 1 semana para entregarla, los 2 integrantes presentes al entregar. Por semana de retraso es -10pts.

## resolucion diagnostico
1. lenguaje de ensamblador es lenguaje de mas bajo nivel, para trabajar a nivel bajo
2. se encarga de ejecutar operaciones, con alu, unidad de control, buses de datos
4. nemonico: instruccion, se usan abreviaciones de palabras para distinguirlas. Arreglo de compuertas
5. registro: conjunto de flip flops para almacenar datos
6. diodo emisor de luz
7. compuerta logica, recibe 2 entradas y toma una decision
8. RAM: memoria volatil desde la que se cargan procesos a memoria
9. binario y hexadecimal
10. and(multiplicacion) or(suma) not(negacion)
11. unidad aritmetica logica
12. rotacion es rotar un grupo de bits, sin que se pierdan(derecha o izquierda), la diferencia con el corrimiento es que si se pierden 

## importancia del ensamblador
`el compilador` es una herramienta que nos ayuda a traducir las instrucciones a codigo maquina, por eso si tenemos errores sintacticos NO COMPILA, pero en el caso de ensamblador `no tiene compilador`, porque el ensamblador se traduce directamente a codigo binario.

Existen los registros de estado, mejor conocidos como banderas. Entonces, cada dato que pasa al microprocesador viene acompañado de una, para que el microprocesador sepa que hacer.

`PILA:` Guarda informacion de donde se va el programa, Por ejemplo si esta ejecutando un proceso y llega otro mas prioritario, en la pila se guarda la instruccion en la que se quedo el menos prioritario para cuando pueda reanudarlo. En la memoria esta bien marcado/segmentado de cual a cual direccion es pila, de cual a cual son datos y de cual a cual es instucciones.

![alt text](/ISC-ITM/6to/Lenguajes%20de%20interfaz/imagenes/image.png)

### desventajas del ensamblador
- repeticion constante de instrucciones
- no hay sintaxis estandarizada para variantes entre procesadores
- dificultad para encontrar errores.
### ventajas
- velocidad de ejecucion
- mayor control sobre el hardware
- realizacion de tareas tecnicas que serian imposibles en otro lenguaje
- depuracion de codigo