.stack 1000

.data

;----TEXTOS
menuOpc db 13,10,'-----------MENU-----------',13,10
        db '1. Consultar',13,10
        db '2. Agregar',13,10
        db '3. Borrar',13,10
        db '4. Salir',13,10,13,10
        db 'Opcion seleccionada:',13,10,'$'

menuPers db 13,10,'----------SELECCIONE PERSONA----------',13,10
         db 'Persona1',13,10
         db 'Persona2',13,10
         db 'Persona3',13,10
         db 'Persona4',13,10
         db 'Persona Seleccionado: $',13,10,'$'
ingNombre db 13,10,'Ingrese su nombre: ',13,10,'$'
ingNControl db 13,10,'Ingrese su Numero de Control: ',13,10,'$'
ingTel db 13,10,'Ingrese su telefono: ',13,10,'$'
ingCorreo db 13,10,'Ingrese su Correo: ',13,10,'$'
ingPeso db 13,10,'Ingrese su Peso: ',13,10,'$'
ingEstatura db 13,10,'Ingrese su Altura: ',13,10,'$'
punto db '.','$'
saltolinea db 13,10,'$'
msgNombre db 'nombre: ','$'
msgNControl db 'Numero de control: ','$'
msgTel db 'Telefono: ','$'
msgCorreo db 'Correo: ','$'
msgPeso db 'Peso: ', '$'
msgEstatura db 'Estatura: ','$'
msgImc db 'IMC: ','$'

;----DATOS PERSONAS
nombres dw '$',0,'$', 0,'$', 0,'$', 0 '$'
numeroscon dw '$',0,'$',0,'$',0,'$',0,'$'
telefonos dw '$',0,'$',0,'$',0,'$',0,'$'
correos dw '$',0,'$',0,'$',0,'$',0,'$'
pesos dw '$',0,0,0,'$',0,0,0,'$',0,0,0,'$',0,0,0,'$'
estaturas dw '$',0,0,0,'$',0,0,0,'$',0,0,0,'$',0,0,0,'$'
imcd1 db '$',0,'$',0,'$',0,'$',0,'$'
imcd2 db '$',0,'$',0,'$',0,'$',0,'$'
imcd3 db '$',0,'$',0,'$',0,'$',0,'$'
imcd4 db '$',0,'$',0,'$',0,'$',0,'$'

;----VARIABLES AUXILIARES
nombrebuff1 db 80,?,80 dup('$')
ncontrolbuff1 db 10,?,10 dup('$')
telefonobuff1 db 11,?,11 dup('$')
correobuff1 db 100,?,100 dup('$')    
nombrebuff2 db 80,?,80 dup('$')
ncontrolbuff2 db 10,?,10 dup('$')
telefonobuff2 db 11,?,11 dup('$')
correobuff2 db 100,?,100 dup('$')  
nombrebuff3 db 80,?,80 dup('$')
ncontrolbuff3 db 10,?,10 dup('$')
telefonobuff3 db 11,?,11 dup('$')
correobuff3 db 100,?,100 dup('$')  
nombrebuff4 db 80,?,80 dup('$')
ncontrolbuff4 db 10,?,10 dup('$')
telefonobuff4 db 11,?,11 dup('$')
correobuff4 db 100,?,100 dup('$')  
centena db 100
decena db 10
pesoD1 db ?
pesoD2 db ?
pesoD3 db ? 
sumpes db 0 
alturaD1 db ?
alturaD2 db ?
alturaD3 db ? 
sumalt db 0  
d1 db 0
d2 db 0
d3 db 0
d4 db 0

opcion db ?
opcionPers db ?
flagP1 db 0
flagP2 db 0
flagP3 db 0
flagP4 db 0     

flagbuff1 db 0
flagbfuf2 db 0
flagbuff3 db 0
flagbuff4 db 0

;-----VARIABLES CALCULO IMC

pesoG dd 0   
alturaG dw 0
decdmill dw 2710h
cocdecimal dw 0
resdecimal dw 0

.code
mov ax,@data
mov ds,ax

inicio:   
mov dx, offset nombres

mov dx, offset menuOpc
mov ah, 09
int 21h
mov ah,01
int 21h
mov opcion, al
sub opcion, 30h

cmp opcion,4
je salida

mov dx, offset menuPers
mov ah,09
int 21h
mov ah,01
int 21h
sub al, 30h
mov opcionPers, al

cmp opcion,1
je consultaPersonas
cmp opcion,2
je ingresaPersonas
cmp opcion,3
je borrarPersona

;-----SETTERS
ingresaPersonas:
;comienzo cortado

cmp opcionPers,1
je setPersona1
cmp opcionPers,2
je setPersona2
cmp opcionPers,3
je setPersona3
cmp opcionPers,4
je setPersona4
jmp inicio

setPersona1:
;---lo unico que te pido dios 
mov dx, offset saltolinea
mov ah,09
int 21h
mov dx, offset ingNombre
int 21h
mov dx, offset nombrebuff1
mov ah,0ah
int 21h  

xor bx, bx
mov bl, nombrebuff1[1]
mov nombrebuff1[bx+2],'$'    ;he aqui la posible optim
                            ;la clave es buff[1]
mov dx, offset ingNControl
mov ah,09
int 21h  
mov dx, offset ncontrolbuff1
mov ah,0ah
int 21h

xor bx,bx
mov bl, ncontrolbuff1[1]
mov ncontrolbuff1[bx+2],'$'

mov dx, offset ingTel
mov ah,09
int 21h 
mov dx, offset telefonobuff1
mov ah,0ah
int 21h      

xor bx,bx   
mov bl, telefonobuff1[1]
mov telefonobuff1[bx+2],'$'  
mov dx, offset ingCorreo
mov ah,09
int 21h 
mov dx, offset correobuff1
mov ah, 0ah
int 21h
xor bx,bx
mov bl, correobuff1[1]
mov correobuff1[bx+2],'$' 
 
mov dx, offset ingPeso
mov ah,09
int 21h
;-------LECTURA DIGITOS
mov ah, 01
int 21h     
mov pesoD1, al
sub pesoD1,30h  
mov al, pesoD1
mul centena         ;resultado se queda en ax
add sumpes, al
   
mov ah, 01
int 21h
mov pesoD2, al
sub pesoD2,30h
mov al, pesoD2
mul decena 
add sumpes, al     
mov ah, 01
int 21h
mov pesoD3, al 
sub pesoD3, 30h 
mov al, pesoD3        ;POR EL TIPO DE DIRECCIONAMIENTO
add sumpes, al 
add pesoD1,30h
add pesoD2,30H
add pesoD3, 30h
;----TERMINA CONVERSION DIGITOS  
mov dx, offset saltolinea
mov ah,09
int 21h
mov dx, offset msgEstatura
mov ah,09
int 21h
;----EMPIEZA CONVERSION DIGITOS  
mov ah,01
int 21h  
mov alturaD1,al 
sub alturaD1,30h 
mov al, alturaD1
mul centena 
add sumalt,al
  
mov ah,01
int 21h
mov alturaD2,al  
sub alturaD2,30h 
mov al, alturaD2
mul decena 
add sumalt, al  
mov ah,01
int 21h
mov alturaD3,al
sub alturaD3,30H 
mov al, alturaD3 
add sumalt, al 
mov al, sumalt   
add alturaD1,30h
add alturaD2,30h
add alturaD3,30h
mov al, sumpes
mov ah,0
mul decdmill
MOV WORD PTR pesoG,AX
MOV WORD PTR pesoG+2,dx
mov al, sumalt
mul sumalt
mov alturaG,ax
xor ax,ax
xor dx,dx
mov ax, WORD PTR pesoG
mov dx, WORD PTR pesoG+2
div alturaG
mov cocdecimal,ax
mov resdecimal,dx
mov bl, 0ah
div bl   
mov [imcd1+1],al
add [imcd1+1],30h
mov al,[imcd1+1] 
mov [imcd2+1],ah
add [imcd2+1],30h
mov al,[imcd2+1]   
mov ax, resdecimal
mov bx,64h
mul bx
mov bx, alturaG
div bx
mov bl,10
div bl
mov [imcd3+1],al
add [imcd3+1],30h
mov al,[imcd3+1]
mov [imcd4+1],ah
add [imcd4+1],30h
mov dx, offset saltolinea
mov ah, 09
int 21h
;----TERMINA CONVERSION DIGITOS

  


mov dx, offset nombrebuff1+2
mov [nombres+1],dx
mov dx, offset ncontrolbuff1+2
mov [numeroscon+1],dx 
mov dx, offset telefonobuff1+2
mov [telefonos+1],dx
mov dx, offset correobuff1+2
mov [correos+1],dx 

xor dx,dx 
mov dl, pesoD1
mov [pesos+1],dx 
mov dl, pesoD2
mov [pesos+2],dx
mov dl,pesoD3
mov [pesos+3],dx   
mov dl, alturaD1
mov [estaturas+1],dx 
mov dl,alturaD2
mov [estaturas+2],dx
mov dl,alturaD3
mov [estaturas+3],dx   
mov [estaturas+4],'$'  
mov [pesos+4],'$' 




mov dx, offset saltolinea
mov ah,09
int 21h 

mov flagP1,1
jmp inicio

setPersona2:  
mov pesoG,0
mov alturaG,0   
mov sumpes,0
mov sumalt,0
   
;---lo unico que te pido dios 
mov dx, offset saltolinea
mov ah,09
int 21h
mov dx, offset ingNombre
int 21h
mov dx, offset nombrebuff2
mov ah,0ah
int 21h  

xor bx, bx
mov bl, nombrebuff2[1]
mov nombrebuff2[bx+2],'$'    ;he aqui la posible optim
                            ;la clave es buff[1]
mov dx, offset ingNControl
mov ah,09
int 21h  
mov dx, offset ncontrolbuff2
mov ah,0ah
int 21h

xor bx,bx
mov bl, ncontrolbuff2[1]
mov ncontrolbuff2[bx+2],'$'

mov dx, offset ingTel
mov ah,09
int 21h 
mov dx, offset telefonobuff2
mov ah,0ah
int 21h      

xor bx,bx   
mov bl, telefonobuff2[1]
mov telefonobuff2[bx+2],'$'  
mov dx, offset ingCorreo
mov ah,09
int 21h 
mov dx, offset correobuff2
mov ah, 0ah
int 21h
xor bx,bx
mov bl, correobuff2[1]
mov correobuff2[bx+2],'$' 
 
mov dx, offset ingPeso
mov ah,09
int 21h
;-------LECTURA DIGITOS
mov ah, 01
int 21h     
mov pesoD1, al
sub pesoD1,30h  
mov al, pesoD1
mul centena         ;resultado se queda en ax
add sumpes, al
   
mov ah, 01
int 21h
mov pesoD2, al
sub pesoD2,30h
mov al, pesoD2
mul decena 
add sumpes, al     
mov ah, 01
int 21h
mov pesoD3, al 
sub pesoD3, 30h 
mov al, pesoD3        ;POR EL TIPO DE DIRECCIONAMIENTO
add sumpes, al 
add pesoD1,30h
add pesoD2,30H
add pesoD3, 30h
;----TERMINA CONVERSION DIGITOS  
mov dx, offset saltolinea
mov ah,09
int 21h
mov dx, offset msgEstatura
mov ah,09
int 21h
;----EMPIEZA CONVERSION DIGITOS  
mov ah,01
int 21h  
mov alturaD1,al 
sub alturaD1,30h 
mov al, alturaD1
mul centena 
add sumalt,al
  
mov ah,01
int 21h
mov alturaD2,al  
sub alturaD2,30h 
mov al, alturaD2
mul decena 
add sumalt, al  
mov ah,01
int 21h
mov alturaD3,al
sub alturaD3,30H 
mov al, alturaD3 
add sumalt, al 
mov al, sumalt   
add alturaD1,30h
add alturaD2,30h
add alturaD3,30h
mov al, sumpes
mov ah,0
mul decdmill
MOV WORD PTR pesoG,AX
MOV WORD PTR pesoG+2,dx
mov al, sumalt
mul sumalt
mov alturaG,ax
xor ax,ax
xor dx,dx
mov ax, WORD PTR pesoG
mov dx, WORD PTR pesoG+2
div alturaG
mov cocdecimal,ax
mov resdecimal,dx
mov bl, 0ah
div bl   
mov [imcd1+3],al
add [imcd1+3],30h
mov al,[imcd1+3] 
mov [imcd2+3],ah
add [imcd2+3],30h
mov al,[imcd2+3]   
mov ax, resdecimal
mov bx,64h
mul bx
mov bx, alturaG
div bx
mov bl,10
div bl
mov [imcd3+3],al
add [imcd3+3],30h
mov al,[imcd3+3]
mov [imcd4+3],ah
add [imcd4+3],30h
mov dx, offset saltolinea
mov ah, 09
int 21h
;----TERMINA CONVERSION DIGITOS
   
   
   
mov dx, offset nombrebuff2+2
mov [nombres+3],dx
mov dx, offset ncontrolbuff2+2
mov [numeroscon+3],dx 
mov dx, offset telefonobuff2+2
mov [telefonos+3],dx
mov dx, offset correobuff2+2
mov [correos+3],dx 

xor dx,dx 
mov dl, pesoD1
mov [pesos+5],dx 
mov dl, pesoD2
mov [pesos+6],dx
mov dl,pesoD3
mov [pesos+7],dx   
mov dl, alturaD1
mov [estaturas+5],dx 
mov dl,alturaD2
mov [estaturas+6],dx
mov dl,alturaD3
mov [estaturas+7],dx 
mov [estaturas+8],'$'  
mov [pesos+8],'$'

mov dx, offset saltolinea
mov ah,09
int 21h 
mov flagP2,1
jmp inicio
    
    
    
setPersona3:  
mov pesoG,0
mov alturaG,0   
mov sumpes,0
mov sumalt,0

;---lo unico que te pido dios 
mov dx, offset saltolinea
mov ah,09
int 21h
mov dx, offset ingNombre
int 21h
mov dx, offset nombrebuff3
mov ah,0ah
int 21h  

xor bx, bx
mov bl, nombrebuff3[1]
mov nombrebuff3[bx+2],'$'    ;he aqui la posible optim
                            ;la clave es buff[1]
mov dx, offset ingNControl
mov ah,09
int 21h  
mov dx, offset ncontrolbuff3
mov ah,0ah
int 21h

xor bx,bx
mov bl, ncontrolbuff3[1]
mov ncontrolbuff3[bx+2],'$'

mov dx, offset ingTel
mov ah,09
int 21h 
mov dx, offset telefonobuff3
mov ah,0ah
int 21h      

xor bx,bx   
mov bl, telefonobuff3[1]
mov telefonobuff3[bx+2],'$'  
mov dx, offset ingCorreo
mov ah,09
int 21h 
mov dx, offset correobuff3
mov ah, 0ah
int 21h
xor bx,bx
mov bl, correobuff3[1]
mov correobuff3[bx+2],'$' 
 
mov dx, offset ingPeso
mov ah,09
int 21h
;-------LECTURA DIGITOS
mov ah, 01
int 21h     
mov pesoD1, al
sub pesoD1,30h  
mov al, pesoD1
mul centena         ;resultado se queda en ax
add sumpes, al
   
mov ah, 01
int 21h
mov pesoD2, al
sub pesoD2,30h
mov al, pesoD2
mul decena 
add sumpes, al     
mov ah, 01
int 21h
mov pesoD3, al 
sub pesoD3, 30h 
mov al, pesoD3        ;POR EL TIPO DE DIRECCIONAMIENTO
add sumpes, al 
add pesoD1,30h
add pesoD2,30H
add pesoD3, 30h
;----TERMINA CONVERSION DIGITOS  
mov dx, offset saltolinea
mov ah,09
int 21h
mov dx, offset msgEstatura
mov ah,09
int 21h
;----EMPIEZA CONVERSION DIGITOS  
mov ah,01
int 21h  
mov alturaD1,al 
sub alturaD1,30h 
mov al, alturaD1
mul centena 
add sumalt,al
  
mov ah,01
int 21h
mov alturaD2,al  
sub alturaD2,30h 
mov al, alturaD2
mul decena 
add sumalt, al  
mov ah,01
int 21h
mov alturaD3,al
sub alturaD3,30H 
mov al, alturaD3 
add sumalt, al 
mov al, sumalt   
add alturaD1,30h
add alturaD2,30h
add alturaD3,30h
mov al, sumpes
mov ah,0
mul decdmill
MOV WORD PTR pesoG,AX
MOV WORD PTR pesoG+2,dx
mov al, sumalt
mul sumalt
mov alturaG,ax
xor ax,ax
xor dx,dx
mov ax, WORD PTR pesoG
mov dx, WORD PTR pesoG+2
div alturaG
mov cocdecimal,ax
mov resdecimal,dx
mov bl, 0ah
div bl   
mov [imcd1+5],al
add [imcd1+5],30h
mov al,[imcd1+5] 
mov [imcd2+5],ah
add [imcd2+5],30h
mov al,[imcd2+5]   
mov ax, resdecimal
mov bx,64h
mul bx
mov bx, alturaG
div bx
mov bl,10
div bl
mov [imcd3+5],al
add [imcd3+5],30h
mov al,[imcd3+5]
mov [imcd4+5],ah
add [imcd4+5],30h
mov dx, offset saltolinea
mov ah, 09
int 21h
;----TERMINA CONVERSION DIGITOS


mov dx, offset nombrebuff3+2
mov [nombres+5],dx
mov dx, offset ncontrolbuff3+2
mov [numeroscon+5],dx 
mov dx, offset telefonobuff3+2
mov [telefonos+5],dx
mov dx, offset correobuff3+2
mov [correos+5],dx 

xor dx,dx 
mov dl, pesoD1
mov [pesos+9],dx 
mov dl, pesoD2
mov [pesos+10],dx
mov dl,pesoD3
mov [pesos+11],dx   
mov dl, alturaD1
mov [estaturas+9],dx 
mov dl,alturaD2
mov [estaturas+10],dx
mov dl,alturaD3
mov [estaturas+11],dx 
mov [estaturas+12],'$'  
mov [pesos+12],'$'
 
mov flagP3,1
jmp inicio

setpersona4:
mov pesoG,0
mov alturaG,0   
mov sumpes,0
mov sumalt,0 

;---lo unico que te pido dios 
mov dx, offset saltolinea
mov ah,09
int 21h
mov dx, offset ingNombre
int 21h
mov dx, offset nombrebuff4
mov ah,0ah
int 21h  

xor bx, bx
mov bl, nombrebuff4[1]
mov nombrebuff4[bx+2],'$'    ;he aqui la posible optim
                            ;la clave es buff[1]
mov dx, offset ingNControl
mov ah,09
int 21h  
mov dx, offset ncontrolbuff4
mov ah,0ah
int 21h

xor bx,bx
mov bl, ncontrolbuff4[1]
mov ncontrolbuff4[bx+2],'$'

mov dx, offset ingTel
mov ah,09
int 21h 
mov dx, offset telefonobuff4
mov ah,0ah
int 21h      

xor bx,bx   
mov bl, telefonobuff4[1]
mov telefonobuff4[bx+2],'$'  
mov dx, offset ingCorreo
mov ah,09
int 21h 
mov dx, offset correobuff4
mov ah, 0ah
int 21h
xor bx,bx
mov bl, correobuff4[1]
mov correobuff4[bx+2],'$' 
 
mov dx, offset ingPeso
mov ah,09
int 21h
;-------LECTURA DIGITOS
mov ah, 01
int 21h     
mov pesoD1, al
sub pesoD1,30h  
mov al, pesoD1
mul centena         ;resultado se queda en ax
add sumpes, al
   
mov ah, 01
int 21h
mov pesoD2, al
sub pesoD2,30h
mov al, pesoD2
mul decena 
add sumpes, al     
mov ah, 01
int 21h
mov pesoD3, al 
sub pesoD3, 30h 
mov al, pesoD3        ;POR EL TIPO DE DIRECCIONAMIENTO
add sumpes, al 
add pesoD1,30h
add pesoD2,30H
add pesoD3, 30h
;----TERMINA CONVERSION DIGITOS  
mov dx, offset saltolinea
mov ah,09
int 21h
mov dx, offset msgEstatura
mov ah,09
int 21h
;----EMPIEZA CONVERSION DIGITOS  
mov ah,01
int 21h  
mov alturaD1,al 
sub alturaD1,30h 
mov al, alturaD1
mul centena 
add sumalt,al
  
mov ah,01
int 21h
mov alturaD2,al  
sub alturaD2,30h 
mov al, alturaD2
mul decena 
add sumalt, al  
mov ah,01
int 21h
mov alturaD3,al
sub alturaD3,30H 
mov al, alturaD3 
add sumalt, al 
mov al, sumalt   
add alturaD1,30h
add alturaD2,30h
add alturaD3,30h
mov al, sumpes
mov ah,0
mul decdmill
MOV WORD PTR pesoG,AX
MOV WORD PTR pesoG+2,dx
mov al, sumalt
mul sumalt
mov alturaG,ax
xor ax,ax
xor dx,dx
mov ax, WORD PTR pesoG
mov dx, WORD PTR pesoG+2
div alturaG
mov cocdecimal,ax
mov resdecimal,dx
mov bl, 0ah
div bl   
mov [imcd1+7],al
add [imcd1+7],30h
mov al,[imcd1+7] 
mov [imcd2+7],ah
add [imcd2+7],30h
mov al,[imcd2+7]   
mov ax, resdecimal
mov bx,64h
mul bx
mov bx, alturaG
div bx
mov bl,10
div bl
mov [imcd3+7],al
add [imcd3+7],30h
mov al,[imcd3+7]
mov [imcd4+7],ah
add [imcd4+7],30h
mov dx, offset saltolinea
mov ah, 09
int 21h
;----TERMINA CONVERSION DIGITOS


mov dx, offset nombrebuff4+2
mov [nombres+7],dx
mov dx, offset ncontrolbuff4+2
mov [numeroscon+7],dx 
mov dx, offset telefonobuff4+2
mov [telefonos+7],dx
mov dx, offset correobuff4+2
mov [correos+7],dx 

xor dx,dx 
mov dl, pesoD1
mov [pesos+13],dx 
mov dl, pesoD2
mov [pesos+14],dx
mov dl,pesoD3
mov [pesos+15],dx   
mov dl, alturaD1
mov [estaturas+13],dx 
mov dl,alturaD2
mov [estaturas+14],dx
mov dl,alturaD3
mov [estaturas+15],dx
mov [estaturas+16],'$'  
mov [pesos+16],'$' 
 
mov flagP4,1
jmp inicio

;------GETTERS
consultaPersonas:
cmp opcionPers,1
je checkP1
cmp opcionPers,2
je checkP2
cmp opcionPers,3
je checkP3
cmp opcionPers,4
je checkP4
jmp inicio 

checkP1:  
cmp flagP1,0
je getPersona1Vacia
jne getPersona1  

checkP2:
cmp flagP2,0
je getPersona2Vacia
jne getPersona2

checkP3:
cmp flagP3,0
je getPersona3Vacia
jne getPersona3

checkP4:
cmp flagP4,0
je getPersona4Vacia
jne getPersona4 

getPersona1Vacia:
mov dx,offset saltolinea
mov ah,09
int 21h
mov dx, offset msgNombre
int 21h
mov dx,offset [nombres+1]
int 21h
mov dx,offset saltolinea
int 21h
mov dx, offset msgNControl
int 21h
mov dx,offset [numeroscon+1]
int 21h
mov dx,offset saltolinea
int 21h
mov dx, offset msgTel
int 21h
mov dx,offset [telefonos+1]
int 21h
mov dx,offset saltolinea
int 21h
mov dx, offset msgCorreo
int 21h
mov dx,offset [correos+1]
int 21h
mov dx,offset saltolinea
int 21h
mov dx, offset msgPeso
int 21h
mov dx, offset [pesos+1]
int 21h
mov dx,offset saltolinea
int 21h
mov dx, offset msgEstatura
int 21h
mov dx, offset[estaturas+1] ;idoneamente serian los 3 digitos de estaturas y de pesos, pero por estetica y pq no afecta,
int 21h               ;solo tomaré 1 cuando está vacio
mov dx,offset saltolinea
int 21h
mov dx,offset offset msgImc
int 21h
mov dx, offset [imcd1+1]
int 21h
mov dx, offset [imcd2+1]
int 21h
mov dx, offset [punto]
int 21h
mov dx, offset [imcd3+1]
int 21h
mov dx, offset [imcd4+1]
int 21h
mov dx,offset saltolinea
int 21h
jmp inicio

getPersona1:
mov dx,offset saltolinea
mov ah,09
int 21h
mov dx, offset msgNombre
int 21h
mov dx, [nombres+1]
int 21h
mov dx,offset saltolinea
int 21h
mov dx, offset msgNControl
int 21h
mov dx, [numeroscon+1]
int 21h
mov dx,offset saltolinea
int 21h
mov dx, offset msgTel
int 21h
mov dx, [telefonos+1]
int 21h
mov dx,offset saltolinea
int 21h
mov dx, offset msgCorreo
int 21h
mov dx, [correos+1]
int 21h
mov dx,offset saltolinea
int 21h
mov dx, offset msgPeso
int 21h
mov dx, offset [pesos+1]
int 21h
mov dx,offset saltolinea
int 21h
mov dx, offset msgEstatura
int 21h
mov dx, offset [estaturas+1]
int 21h 
mov dx,offset saltolinea
int 21h
mov dx, offset msgImc
int 21h
mov dx, offset [imcd1+1]
int 21h
mov dx, offset [imcd2+1]
int 21h
mov dx, offset [punto]
int 21h
mov dx, offset [imcd3+1]
int 21h
mov dx, offset [imcd4+1]
int 21h
mov dx,offset saltolinea
int 21h
jmp inicio

getPersona2Vacia:
mov dx,offset saltolinea
mov ah,09
int 21h
mov dx, offset msgNombre
int 21h
mov dx,offset [nombres+3]
int 21h
mov dx,offset saltolinea
int 21h
mov dx, offset msgNControl
int 21h
mov dx,offset [numeroscon+3]
int 21h
mov dx,offset saltolinea
int 21h
mov dx, offset msgTel
int 21h
mov dx,offset [telefonos+3]
int 21h
mov dx,offset saltolinea
int 21h
mov dx, offset msgCorreo
int 21h
mov dx,offset [correos+3]
int 21h
mov dx,offset saltolinea
int 21h
mov dx, offset msgPeso
int 21h
xor dx,dx
mov dx,offset  [pesos+3]
int 21h  
xor dx,dx
mov dx,offset saltolinea
int 21h
mov dx, offset msgEstatura
int 21h
mov dx,offset [estaturas+3]
int 21h
mov dx,offset saltolinea
int 21h
mov dx, offset msgImc
int 21h
mov dx, offset [imcd1+3]
int 21h
mov dx, offset [imcd2+3]
int 21h
mov dx, offset [punto]
int 21h
mov dx, offset [imcd3+3]
int 21h
mov dx, offset [imcd4+3]
int 21h
mov dx,offset saltolinea
int 21h
jmp inicio   

getPersona2:
mov dx,offset saltolinea
mov ah,09
int 21h
mov dx, offset msgNombre
int 21h
mov dx, [nombres+3]
int 21h
mov dx,offset saltolinea
int 21h
mov dx, offset msgNControl
int 21h
mov dx, [numeroscon+3]
int 21h
mov dx,offset saltolinea
int 21h
mov dx, offset msgTel
int 21h
mov dx, [telefonos+3]
int 21h
mov dx,offset saltolinea
int 21h
mov dx, offset msgCorreo
int 21h
mov dx, [correos+3]
int 21h
mov dx,offset saltolinea
int 21h
mov dx, offset msgPeso
int 21h
mov dx, offset[pesos+5]
int 21h
mov dx,offset saltolinea
int 21h
mov dx, offset msgEstatura
int 21h
mov dx, offset[estaturas+5]
int 21h
mov dx,offset saltolinea
int 21h
mov dx, offset msgImc
int 21h
mov dx, offset [imcd1+3]
int 21h
mov dx, offset [imcd2+3]
int 21h
mov dx, offset [punto]
int 21h
mov dx, offset [imcd3+3]
int 21h
mov dx, offset [imcd4+3]
int 21h
mov dx,offset saltolinea
int 21h 


jmp inicio


getPersona3Vacia:
mov dx,offset saltolinea
mov ah,09
int 21h
mov dx, offset msgNombre
int 21h
mov dx, offset [nombres+5]
int 21h
mov dx,offset saltolinea
int 21h
mov dx, offset msgNControl
int 21h
mov dx, offset [numeroscon+5]
int 21h
mov dx,offset saltolinea
int 21h
mov dx, offset msgTel
int 21h
mov dx, offset [telefonos+5]
int 21h
mov dx,offset saltolinea
int 21h
mov dx, offset msgCorreo
int 21h
mov dx, offset [correos+5]
int 21h
mov dx,offset saltolinea
int 21h
mov dx, offset msgPeso
int 21h
mov dx, offset [pesos+5]
int 21h
mov dx,offset saltolinea
int 21h
mov dx, offset msgEstatura
int 21h
mov dx, offset [estaturas+5]
int 21h
mov dx,offset saltolinea
int 21h
mov dx, offset msgImc
int 21h
mov dx, offset [imcd1+5]
int 21h
mov dx, offset [imcd2+5]
int 21h
mov dx, offset [punto]
int 21h
mov dx, offset [imcd3+5]
int 21h
mov dx, offset [imcd4+5]
int 21h
mov dx,offset saltolinea
int 21h
jmp inicio



getPersona3:
mov dx,offset saltolinea
mov ah,09
int 21h
mov dx, offset msgNombre
int 21h
mov dx, [nombres+5]
int 21h
mov dx,offset saltolinea
int 21h
mov dx, offset msgNControl
int 21h
mov dx, [numeroscon+5]
int 21h
mov dx,offset saltolinea
int 21h
mov dx, offset msgTel
int 21h
mov dx, [telefonos+5]
int 21h
mov dx,offset saltolinea
int 21h
mov dx, offset msgCorreo
int 21h
mov dx, [correos+5]
int 21h
mov dx,offset saltolinea
int 21h
mov dx, offset msgPeso
int 21h
mov dx, offset[pesos+9]
int 21h
mov dx,offset saltolinea
int 21h
mov dx, offset msgEstatura
int 21h
mov dx, offset[estaturas+9]
int 21h
mov dx,offset saltolinea
int 21h
mov dx, offset msgImc
int 21h
mov dx, offset [imcd1+5]
int 21h
mov dx, offset [imcd2+5]
int 21h
mov dx, offset [punto]
int 21h
mov dx, offset [imcd3+5]
int 21h
mov dx, offset [imcd4+5]
int 21h
mov dx,offset saltolinea
jmp inicio

getPersona4Vacia:
mov dx,offset saltolinea
mov ah,09
int 21h
mov dx, offset msgNombre
int 21h
mov dx, offset [nombres+3]
int 21h
mov dx,offset saltolinea
int 21h
mov dx, offset msgNControl
int 21h
mov dx, offset [numeroscon+3]
int 21h
mov dx,offset saltolinea
int 21h
mov dx, offset msgTel
int 21h
mov dx, offset [telefonos+3]
int 21h
mov dx,offset saltolinea
int 21h
mov dx, offset msgCorreo
int 21h
mov dx, offset [correos+3]
int 21h
mov dx,offset saltolinea
int 21h
mov dx, offset msgPeso
int 21h
mov dx, offset[pesos+13]
int 21h
mov dx,offset saltolinea
int 21h
mov dx, offset msgEstatura
int 21h
mov dx, offset[estaturas+13]
int 21h
mov dx,offset saltolinea
int 21h
mov dx, offset msgImc
int 21h
mov dx, offset [imcd1+3]
int 21h
mov dx, offset [imcd2+3]
int 21h
mov dx, offset [punto]
int 21h
mov dx, offset [imcd3+3]
int 21h
mov dx, offset [imcd4+3]
int 21h
mov dx,offset saltolinea
int 21h
jmp inicio  

getPersona4:
mov dx,offset saltolinea
mov ah,09
int 21h
mov dx, offset msgNombre
int 21h
mov dx, [nombres+7]
int 21h
mov dx,offset saltolinea
int 21h
mov dx, offset msgNControl
int 21h
mov dx, [numeroscon+7]
int 21h
mov dx,offset saltolinea
int 21h
mov dx, offset msgTel
int 21h
mov dx, [telefonos+7]
int 21h
mov dx,offset saltolinea
int 21h
mov dx, offset msgCorreo
int 21h
mov dx, [correos+7]
int 21h
mov dx,offset saltolinea
int 21h
mov dx, offset msgPeso
int 21h
mov dx, offset [pesos+13]
int 21h
mov dx, offset saltolinea
int 21h
mov dx, offset msgEstatura
int 21h                                     
mov dx, offset[estaturas+13]
int 21h
mov dx,offset saltolinea
int 21h
mov dx, offset msgImc
int 21h
mov dx, offset [imcd1+7]
int 21h
mov dx, offset [imcd2+7]
int 21h
mov dx, offset [punto]
int 21h
mov dx, offset [imcd3+7]
int 21h
mov dx, offset [imcd4+7]
int 21h
mov dx,offset saltolinea
int 21h
jmp inicio


;--------BORRAR 
borrarPersona:
cmp opcionPers,1
je borrarPersona1
cmp opcionPers,2
je borrarPersona2
cmp opcionPers,3
je borrarPersona3
cmp opcionPers,4
je borrarPersona4
jmp inicio  

borrarPersona1: 

mov [nombres+1],0
mov [numeroscon+1],0
mov [telefonos+1],0
mov [correos+1],0
mov [pesos+1],0    
mov [pesos+2],0
mov [pesos+3],0   
mov [estaturas+1],0    
mov [estaturas+2],0
mov [estaturas+3],0  
mov [imcd1+1],0
mov [imcd2+1],0
mov [imcd3+1],0    
mov [imcd4+1],0
mov flagP1,0  
jmp inicio


borrarPersona2: 
mov [nombres+3],0
mov [numeroscon+3],0
mov [telefonos+3],0
mov [correos+3],0
mov [pesos+5],0    
mov [pesos+6],0
mov [pesos+7],0   
mov [estaturas+5],0    
mov [estaturas+6],0
mov [estaturas+7],0  
mov [imcd1+3],0
mov [imcd2+3],0
mov [imcd3+3],0
mov [imcd4+3],0  
mov flagP2,0
jmp inicio

borrarPersona3: 
mov [nombres+5],0
mov [numeroscon+5],0
mov [telefonos+5],0
mov [correos+5],0
mov [pesos+9],0    
mov [pesos+10],0
mov [pesos+11],0   
mov [estaturas+9],0    
mov [estaturas+10],0
mov [estaturas+11],0  
mov [imcd1+5],0
mov [imcd2+5],0
mov [imcd3+5],0
mov [imcd4+5],0  
mov flagP3,0
jmp inicio

borrarPersona4:
mov [nombres+7],0
mov [numeroscon+7],0
mov [telefonos+7],0
mov [correos+7],0
mov [pesos+13],0    
mov [pesos+14],0
mov [pesos+15],0   
mov [estaturas+13],0    
mov [estaturas+14],0
mov [estaturas+15],0  
mov [imcd1+7],0
mov [imcd2+7],0
mov [imcd3+7],0 
mov [imcd4+7],0 
mov flagP4,0
jmp inicio

salida:

.exit
