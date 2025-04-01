;en este caso, lo que inicia con . son las directivas del programa
.model small
.data  ;segmento de datos


cuenta db 30h,'$',0Ah;en cuenta, reserva un DataByte(8 bits) con el valor 30 en hexadecimal, por eso 30h y otros 8 bits para el signo de pesos
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