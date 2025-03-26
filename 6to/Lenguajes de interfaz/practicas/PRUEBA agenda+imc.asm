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
msgPeso db 'Peso', '$'
msgEstatura db 'Estatura: ','$'
msgImc db 'IMC: ','$'

;----DATOS PERSONAS

nombres dw '$',30h,'$', 0,'$', 0,'$', 0 '$'
numeroscon dw '$',30h,'$',0,'$',0,'$',0,'$'
telefonos dw '$',30h,'$',0,'$',0,'$',0,'$'
correos dw '$',30h,'$',0,'$',0,'$',0,'$'
pesos dw '$',30h,'$',0,'$',0,'$',0,'$'
estaturas dw '$',30h,'$',0,'$',0,'$',0,'$'   
imcd1 db '$',30h,'$',0,'$',0,'$',0,'$'
imcd2 db '$',30h,'$',0,'$',0,'$',0,'$'
imcd3 db '$',30h,'$',0,'$',0,'$',0,'$'
imcd4 db '$',30h,'$',0,'$',0,'$',0,'$'  

;----VARIABLES AUXILIARES 

nombrebuff db 80,?,80 dup('$')   
ncontrolbuff db 9,?,9 dup('$')
telefonobuff db 11,?,11 dup('$') 
correobuff db 100,?,100 dup('$')  
pesoD1 db ?
pesoD2 db ?
pesoD3 db ?
alturaD1 db ?
alturaD2 db ?
alturaD3 db ?

opcion db ?
opcionPers db ?    

.code 
mov ax,@data
mov ds,ax

inicio:

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
;je

;-----SETTERS

ingresaPersonas:
mov dx, offset saltolinea
mov ah,09
int 21h
mov dx, offset ingNombre
int 21h
mov dx, offset nombrebuff
mov ah,0ah
int 21h  

xor bx, bx
mov bl, nombrebuff[1]
mov nombrebuff[bx+2],'$' 
mov dx, offset nombrebuff+2

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


setPersona2: 
mov [nombres+3],dx  
;mov al, [nombrebuff+2 ]
;mov [nombres+3], ax
mov dx, offset saltolinea
mov ah,09
int 21h
jmp inicio

setPersona3:

setpersona4:


;------GETTERS

consultaPersonas: 
cmp opcionPers,1
je getPersona1
cmp opcionPers,2
je getPersona2
cmp opcionPers,3
je getPersona3
cmp opcionPers,4
je getPersona4   
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
mov dx,  [correos+1]
int 21h
mov dx,offset saltolinea   
int 21h
mov dx, offset msgPeso
int 21h
mov dx, [pesos+1]
int 21h
mov dx,offset saltolinea   
int 21h 
mov dx, offset msgEstatura  
int 21h
mov dx, [estaturas+1]
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
mov dx, [pesos+3]
int 21h
mov dx,offset saltolinea   
int 21h 
mov dx, offset msgEstatura  
int 21h
mov dx, [estaturas+3]
int 21h       
mov dx,offset saltolinea   
int 21h  
mov dx, offset msgImc  
int 21h
mov dx, offset [imcd1+3]   ;pendiente ve ruq epedo con el offset        
int 21h                    ;pero seguramente igual se vaya  

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



getPersona3:

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



getPersona4:  

mov dx,offset saltolinea

mov ah,09    

int 21h  

mov dx, offset msgNombre

int 21h

mov dx, offset [nombres+7]

int 21h 

mov dx,offset saltolinea   

int 21h

mov dx, offset msgNControl

int 21h        

mov dx, offset [numeroscon+7]

int 21h   

mov dx,offset saltolinea   

int 21h

mov dx, offset msgTel 

int 21h

mov dx, offset [telefonos+7]

int 21h 

mov dx,offset saltolinea   

int 21h    

mov dx, offset msgCorreo

int 21h

mov dx, offset [correos+7]

int 21h

mov dx,offset saltolinea   

int 21h

mov dx, offset msgPeso

int 21h

mov dx, offset [pesos+7]

int 21h

mov dx,offset saltolinea   

int 21h 

mov dx, offset msgEstatura  

int 21h

mov dx, offset [estaturas+7]

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





salida: 



.exit
