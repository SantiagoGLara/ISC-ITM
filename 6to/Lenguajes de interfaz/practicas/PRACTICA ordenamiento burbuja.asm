.stack 1000

.model small

.data

numeros db '3','2','5','4','7','$';23457   

aux db 0 
orden db 0

.code
inicio:
cmp orden, 1     ;por default, orden tiene un 1, si el codigo entra a la seccion de ordenar quiere decir que se ordeno minimo
                 ;una vez, osease que puede que se requiera dar otra vuelta para poder ordenar totalmente el arreglo
                 ;si orden nunca deja de ser 1, quiere decir que nunca requirió ordenar datos, por lo tanto está ordenado todo
                
mov orden,1      ;un mov que no altera las banderas, por lo tanto no altera la 
je salida 

mov si, 0           
mov ax,@data
mov ds,ax 
 

mov bx, offset numeros 


seguir:
mov al,[bx+si] 
inc si
mov ah,[bx+si] 

cmp ah,'$'       ; Compara si AH contiene el carácter '$'
je  inicio 

cmp ah,al
ja seguir 
jb ordenar



ordenar:
mov orden, 0
mov aux, al
mov al, ah
mov ah, aux
  
mov [bx+si],ah
dec si
mov [bx+si],al
inc si
jmp seguir




salida:
mov dx, offset numeros
mov ah, 09
int 21h

.exit
