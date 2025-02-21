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
## estructura de un microporcesador
![estructura](/6to/Lenguajes%20de%20interfaz/imagenes/image002.gif)
`RELOJ:`sincroniza las operaciones internas del microprocesador con los demas componentes del sistema a su ritmo
`UC:`asasasa
`bus:`Serie de cables que conectan al mc para pasar info

- bus de datos: Puede ser bidireccional y permite la transferencia de datos entre la CPU y el resto de unidades del ordenador.
- bus de control: Sincroniza las actividades entre la CPU y los periféricos mediante señales como lectura/escritura.
- bus de direcciones: te da la informaicon donde se almacena un dato
## registros
un flip flop es un dispositivo de almacenar 2 niveles de volaje, uno bajo de .5v y otro alto de 5v. El nivel bajo es interpretado como 0 y el alto como 1, cada flip flop es capaz de almacenar 1 bit, el conjunto de varios flip flops es lo que llamamos `registro`. Los registros son ubicaciones de almacenamiento de alta velocidad que se encuentran directamente dentro del microprocesador, estan diseñados para un acceso mayor a la velociadad convenciona.

a un grupo de 16 bits se le conoce como palabra `dw`(Data Word), esta palabra dividida a la mitad son 8 bits y estos 8 a la mitad son nibbles. Regularmente al trabajar con 1 caracter ocupa estos 4 bits.

### registros de proposito general
- Registro AX: acumulador principal, se usa para la mayoria de aritmetica y E/S
- Registro BX: registro base, para el indexado/funciona como apuntador
- Registro CX: registro contador ya que puede contener un valor para controlar el numero de veces que se repite una cierta operaciones
- Registro DX Se reconoce como registro de datos. Algunas E/S requieren su uso, y las operaciones como multiplicacion y division con cifras grandes requieren que ax y dx trabajen juntos
#### registros de indice
los registros de indice se utilizan fundamentalmente en operaciones con cadenas y para direccionamiento indexado
- registro SI(Indice Fuente): requeridos en algunas operaciones con cadenas de caracteres. Este registro está asociado con Ds
- Registro DI(indice destino) requerido tambien en determinadas operaciones con cadenas de caracteres. Asociado con DS o ES

Los registros tambien se pueden usar como registros de datos para sumas,movimiento de datos,etc. Pero unicamente cuando no los vayamos a utilizar

#### Registros apuntadores (SP y BP)
están asociados al registro de segmento de pila(SS) y permiten acceder a los datos almacenados en l pila. Representan un desplazamiento respecto de la direcion indicada en SS
**COMPLETAR**

#### Registro Apuntador de Instrucciones(IP)
se trata de un registro de 16 bits que contiene el desplazamiento de la dirección de la siguiente instrucción **completar**

#### Registro de banderas (FL)
Registro de 16 bits (solo se usan 9 de ellos) sirven para indicar el estado actual de la maquina y el resultado del procesamiento. La mayor parte de las instrucciones de comparacion y aritmeticas
## segmentos
un segmento es un area especial en un programa que inicia el limite de un parrafo, esto es en una localidad regularmente dividida en 16 o 10 hex. Puede estar dividido.
- segmento de codigo(CS): espacio de memoria asignado a las instrucciones:
- segmento de datos(DS): contiene datos, constantes y areas de trabajo definidas por el programa
- segmento de pila(SS): contiene datos y direcciones que se necesitan guardar temporalmente
- registros de segmento: son registros de 16 bits que guardan los limites de los segmentos, las direcciones de cada segmento vaya. 