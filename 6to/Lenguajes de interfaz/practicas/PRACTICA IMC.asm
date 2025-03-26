.stack 1000
.data  

pesoD1 db 0 ;kilos 
pesoD2 db 0
pesoD3 db 0
alturaD1 db 0
alturaD2 db 0
alturaD3 db 0
mensajePeso db 13,10,'ingrese peso: $'
mensajeAltura db ,13,10,'ingrese altura: $'  
decdmill dw 2710h
centena dw 100
decena dw 0Ah
alt db 0
pes db 0   
pesoG dd 0  
alturaG dw 0   
imc db 0, '$'
imcmod db 0 ,'$'
punto db 2Eh ,'$'     
cocdecimal dw 0
resdecimal dw 0   
d1 db 0,0,'$'
d2 db 0,0,'$'
d3 db 0,0,'$'
d4 db 0,0,'$'      
newline db 0ah,0dh,'$' 
centenaword dw 0ah               

.code     
mov AX,@data
mov DS, AX 

mov dx, offset mensajePeso
mov ah, 09
int 21h

mov ah, 01
int 21h
mov pesoD1, al
sub pesoD1,30h  
mov al, pesoD1
mul centena         ;resultado se queda en ax
add pes, al

   
mov ah, 01
int 21h
mov pesoD2, al
sub pesoD2,30h
mov al, pesoD2
mul decena
add pes, al    


mov ah, 01
int 21h
mov pesoD3, al 
sub pesoD3, 30h 
mov al, pesoD3        ;POR EL TIPO DE DIRECCIONAMIENTO
add pes, al 

mov al, pes   
mov ah,0
mul decdmill  

MOV WORD PTR pesoG, AX  ; Parte baja en resultado[0:15]
MOV WORD PTR pesoG+2, DX ; Parte alta en resultado[16:31]

mov dx, offset newline
mov ah,09
int 21h

mov dx, offset mensajeAltura
mov ah,09
int 21h

mov ah,01
int 21h  
mov alturaD1,al 
sub alturaD1,30h 
mov al, alturaD1
mul centena
add alt,al
  
mov ah,01
int 21h
mov alturaD2,al  
sub alturaD2,30h 
mov al, alturaD2
mul decena
add alt, al  


mov ah,01
int 21h
mov alturaD3,al
sub alturaD3,30H 
mov al, alturaD3  
add alt, al 
mov al, alt 

mul alt
MOV alturaG, ax  
mov ax, 0
mov dx,0

MOV ax, WORD PTR pesoG      ; Parte baja del dividendo en DX 
mov dx, WORD PTR pesoG+2   ; Parte alta del dividendo en AX

div alturaG

mov cocdecimal, ax
mov resdecimal, dx   

mov bl, 0Ah   
div bl 
mov d1,al 
add d1,30h  
mov al, d1
mov [d1+1],'$' 

mov d2,ah  
add d2,30h
mov [d2+1],'$'
mov al,d2
           
mov ax, resdecimal 
mov bx, 64h  ;ra
mul bx ;recien agregado 
mov bx, alturaG   
div bx   

mov bl,10
div bl

mov d3, al
add d3, 30h
mov [d3+1],'$'
mov al, d3 

mov d4, ah
add d4,30h
mov [d4+1],'$'  

mov al,d4
      
mov dx, offset newline
mov ah,09
int 21h 

             
mov dx, offset d1             
mov ah, 09
int 21h
                   
mov dx, offset d2
int 21h

mov dx, offset punto
int 21h  

mov dx, offset d3
int 21h

mov dx, offset d4
int 21h


.exit