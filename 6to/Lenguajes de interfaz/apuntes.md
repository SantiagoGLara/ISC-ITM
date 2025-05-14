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
## Memoria Principal(RAM)
Memoria volatil, es donde la computadora guarda temporalmente los datos de los progroamas que el procesador está procesando o va a procesar. Cuando el procesador va a ejecutar un programa primero carga a memoria y despues ejecuta
### tipos de memoria RAM
- SRAM
- DRAM: donde se guardan programas y datos cuando hay un programa en ejecucion. Economica pero debe actualizarse en lapsos no mayor a 1 ms o se pierde el contenido
- VRAM: almacena datos de video, tiene doble puerto y permite actualizar constantemente la pantalla
- RAM de CMOS: en la tarjeta madre almacena informacion del sistema.
- caché: muy costosa, se caracteriza por ser la mas rapida de todas. Se conforma de circuitos integrados o chips capaces de memorizar información digital, es decir, valores binarios.
## interrupciones
estado en el cual el microprocesador detiene la ejecución, por una peticion y le tiene que dar prioridad a esta. Fueron creadas para facilitar al programador el acceso a los diferentes dispositivos de la computadora. Hay diferentes tipos:
- hardware: generadas por el teclado, el mouse, botón de volumen,etc.
    - internas: cuando realizamos una operacion que genera banderas de estado 
    - externas: cuando conectamos el cargador, audifonos, impresora, etc.
- software: provocadas por el sistema, como una alarma que pongamos
    - interrupciones DOS:
    - interrupciones BIOS: Basic Input Output System

La instrucción INT es como nos referimos a la subrutina del sistema conocida como MANEJADOR DE INTERRUPCIONES. En el manejador de interrupciones se encuentran todas las interrupciones; cuando mandamos a llamar una interrupcion se manda una dirección de donde se encuentra la función que queremos usar y el manejador de interrupciones ejecuta ese segmento

### interrupciones comunes
- INT 10h: servicios de video, procedimientos que muestean rutinas que controlan la posicion del cursor, textoa  color, desplazan pantalla y muestran graficos
- 16h
- 1Ah
### llamadas a servicios del sistema
llamadas que ejecutan los programas de aplicacion para pedir algun servicio al SO. Existen 2 tipos de llamadas al sistema, bloqueantes y no bloqueantes
- bloqueantes: 
- no bloqueantes
## modos de direccionamiento
son las maneras que enviamos la info. Indican la manera de obtener los operandos.
- `Direccionamiento de registro:` cuando en un mnemonico se opera con 2 registros
- `Direccionamiento inmediato:` cuando se opera y queremos mandar un numero de memoria
- `Direccionamiento directo:`
- `Direccionamiento indirecto:`
- `Direccionamiento extentido:`
- `Direccionamiento indirecto mediante registro: `
- `Direccionamiento por registro base: `
- `Direccionamiento indexado: `
- `Direccionamiento respecto a una base: `

## Proceso de ensamblado y ligado
un programa escrito ensamblador no puede ejecutarse directamente en la computadora, debe interpretarse/ensamblarse en ejecutable. El ensamblador, similar a lo que hace un compilador, produce un archivo que contiene lenguaje maquina al cual se le conoce archivo de codigo objeto

Este archivo no está aun listo para ejecutarse, debe pasar a otro programa llamado `Enlazador`, que hace enlace con los recursos que necesita el codigo para ahora si, poder ejecutarse.
flujo:
![ensam-liga](/6to/Lenguajes%20de%20interfaz/imagenes/Proceso%20ensamblado%20ligado.png)
## Despleagado de mensajes en el monitor

El adaptador de video controla la visualización de texto y gráﬁcos. Tiene dos componentes: el controlador de video y la memoria de visualización de video. Todos los gráficos y el texto que se muestran en el monitor se escriben en la RAM de visualización de video, para después enviarlos al monitor mediante el controlador de video. ​

El controlador de video es en sí un microprocesador de propósito especial, que libera a la CPU principal del trabajo de controlar el hardware de video.​

Para hacer esto se pueden utilizar varios de los servicios con los que cuenta el lenguaje ensamblador.​

Para detener la pantalla y permitir al usuario ver lo que se ha desplegado en la misma se utiliza el servicio 00 de la interrupción 16h.​

```asm
;en este caso, lo que inicia con . son las directivas del programa
.model small
.data  ;segmento de datos


cuenta db 30h,'$';en cuenta, reserva un DataByte(8 bits) con el valor 30 en hexadecimal, por eso 30h y otros 8 bits para el signo de pesos
                 ;tambien pudimos referenciar el signo de pesos con su ascii en hexadecimal (24) o decimal (36)

.code      ;segmento de codigo
mov ax, @data ;aqui @data manda a llamar la direccion del segmento de datos y la guarda en ax, puesto que aunque pusimos antes el segmento, el codigo por si solo
              ;no sabe donde esta ese segmento
mov ds,ax
mov cx,0
ciclo:     ;etiqueta/identificador, para "marcar" una seccion del codigo
mov dx,offset cuenta   ;offset hace el desplazamiento hasta donde estan los datos cuenta
mov ah,09      

int 21h     
add cuenta,1
inc cx

cmp cx, 10        ;COMPARA 10 y CX
jne ciclo         ;toda las instrucciones que inician con j son de bifurcacion de salto, JNE es JUMP IF NOT EQUALS, si no son iguales salta a la linea del ciclo
je salir          ;si son iguales, salta a salir 



salir:

.exit    ;fin del codigo

```

practica 1: imprimir 3 nombres con su no. de control, numero, correo y edad
```asm
.model small
.data
usuario1 db 'Cristian Cambron',0Dh,0Ah,'CC@GMAIL.COM',0Dh,0Ah,'21120701',0Dh,0Ah,'443121212',0Dh,0Ah,'21','$',
usuario2 db 0Ah,0Dh,'Santiago Lara',0Dh,0Ah,'SL@GMAIL.COM',0Dh,0Ah,'22121360',0Dh,0Ah,'4341147110',0Dh,0Ah,'20','$'
usuario3 db 0Ah,0Dh,'Mayavi Sosa',0Dh,0Ah,'MS@GMAIL.COM',0Dh,0Ah,'217777771',0Dh,0Ah,'4431041502',0Dh,0Ah,'21','$',0Dh,0Ah


.code
mov ax, @data
mov ds, ax

mov dx, offset usuario1
mov ah,09
int 21h

mov dx, offset usuario2
int 21h

mov dx, offset usuario3
int 21h

.exit
```


### constantes
- tipo caracter
- tipo cadena (secuencias de caracteres)
### palabras reservadas
tienen un significado especial, y solo pueden usarse dentro de su contexto correcto. Hay varias palabras reservadas
### identificadores
### instrucciones
es un enunciado que se vuelve ejecutable

## Ciclos numericos
en ocaciones es necesario hacer que el programa no siga una secuencia lineal, si no que repita varias veces una sentencia o bloque de instrucciones antes de continuar con el ciclo del programa. Por ejemplo LOOP, LOOPE, LOOPNE, LOOPZ, LOOPNZ

### caotyra vasuca de cadenas:
- MOVSB
- MOVSW


## arduino
PINB

DDRB: 8 bits, registra en cada bit, cada puerto si va a fungir como entrada o salida (1 salida, 0 entrada)

PORTB: 8 bits, registra si el puerto está encendido o apagado. en caso de tener el DDRB marcado un bit como entrada, ese mismo Bit lo marcaremos como un 1, para usar la resistencia de pullUp, que permite diferenciar cuando la entrada haga el cambio de voltaje

pinB: muestra si tenemos algo conectado. si la resistencia de puppUp está activada(es decir, dado bit marcado como entrada), esperaremos ver en PinB un 1 si no tenemos conectados nada, osea que la entrada no está pasando, el boton sin presionar. Si el boton `se presiona`, osea que ya manda voltaje, en pinB se verá un 0    

primero vemos en ddrb si es entrada o salida, despues en portb, si es entrada vemos si tiene la resistencia de pullup está encendida o apagada, y si es salida si le mandamos o no voltaje

```ASM
.include "m328pbdef.inc"

config: LDI R16,0B00011100;
	   OUT DDRB,R16 ;CONFIGURA CUALES BITS SON IN Y CUALES OUT (1 IN, 2 OUT)
	   SBI PORTB,0 ;BOTON0 1, set bit in out. Pone un 1 en el bit 0 del puerto B
	   SBI PORTB,1 ;BOTON0 2, pone un 1 en el bit 1 del puertoB. osea que marcamos del puerto b los bits 
				   ;de entrada

BOTON1: LDI R21,0b00000001
		NOP ;retardillo		
		NOP
		IN R20,PINB ;in port, lo que está en el puerto lo cargamos al registro
		AND R21,R20  ;00000001, me indica si el boton está presionado o no, en este caso el bit 0 si.
		CPI R21, 0X01 ;compara el registro 21 con un 1. 0x= hexa
		BRNE LED_ON ;branch if not equals, osea si la comparacion no es igual. que sea distinto de 1
					;quiere decir que no está presionado
BOTON2: LDI R21, 0b00000010  ;0b00000010
		 IN R20, PINB ;0B00000011
		 AND R21, R20 ;0b00000010
		 CPI R21,0b00000010  
		 BREQ BOTON1
		 BRNE LED_OFF
LED_ON: SBI PORTB,3
	   SBI PORTB,4
	   SBI PORTB,2
	   JMP BOTON1

LED_OFF: CBI PORTB,3
		 CBI PORTB,4
		 CBI PORTB,2
		 JMP BOTON1
start:
    inc r16
    rjmp start

```