name "Practica 5 Calculadora"
.model tiny
ORG 100h
;---------------------
;Segmento de datos
.data 
    ;Menu que se imprimira en la pantalla
    menuOpc db '-----------MENU-----------',13,10
            db '1. Suma',13,10
            db '2. Resta',13,10
            db '3. Division',13,10
            db '4. Multiplicacion',13,10 
            db '5. Salir',13,10,13,10
			db 'Opcion seleccionada: $',13,10
	
	sumaMsg db 10,13,10,13, 'Suma','$'
	restaMsg db 10,13,10,13, 'Resta','$'
	diviMsg db 10,13,10,13, 'Division','$'
	multiMsg db 10,13,10,13, 'Multiplicacion','$'
	 
	 
	menos db "-","$"
    ingresa db 10,13,'Ingresa un digito: ', 	'$'  
			
    res db 10,13,10,13,'Resultado= ',	'$' 
    
    Error db 10,13,10,13, "Error: opcion no valida", "$"
    div0 db 10,13,10,13, "Error: Division entre 0"
    
    num1 dw ?                         ;Primer numero
	num2 dw ?                         ;Segundo numero
	
	A1 dw ?                                  
    B1 dw ?                                  
    A2 dw ?                                  
    B2 dw ?
    aux db ?                                  
    
    result dw ?                                 
    
;---------------------
;Segmento de codigo
.code
Inicio:
	;Carga el segmento de datos en ds
    MOV AX, @data
	MOV DS,AX
Menu:
    MOV AH,00h  
	MOV AL,03h
 	INT 10h  
 	
	MOV CX,02h ;LIMPIA PANTALLA AL INICIAR EL MENU
    
    ;Imprime el menu
	mov ah, 09h 
	lea dx, menuOpc  ;Imprime mensaje 
	int 21h
	
	MOV AH,01h       ;Entrada de caracter
	INT 21h  
	
	XOR AH,AH        ;Limpia AH
	SUB AL,30h       ;Convertir caracter decimal
	
	                 ;Salto a la opcion que haya en AL
	CMP AL,1         ;
	JE Suma
	CMP AL,2
	JE Resta
	CMP AL,3
	JE Division
	CMP AL,4
	JE Multiplicacion
	CMP AL,5
	JE Salir
	JMP Menu ;Si no es ninguna opcion salta de nuevo al menu

Salir:

	MOV AX,4C00h
	INT 21h

;--------------------SUMA------------------------
	
Suma:
	mov ah, 09h 
	lea dx, sumaMsg   
	int 21h
	                 ;Pide los dos numeros
	call LEER_NUM
    ADD AL, BL
    MOV b.result, AL
    call IMPRIMIR_RES

	;Salta a Menu
	JMP Menu 
	
;--------------------RESTA------------------------

Resta:
	
	mov ah, 09h 
	lea dx, restaMsg   
	int 21h
	call LEER_NUM
	CMP BL, AL
    JE resNor 
    JB resNor
    JA resNeg  
  JMP menu 
	
    
;--------------------DIVISION------------------------

Division: 
	mov ah, 09h 
	lea dx, diviMsg  ;Imprime mensaje 
	int 21h
	
	 
    call LEER_NUM
    CMP BL, 0
    JE divCero
    JA divNor
    
    ;Salta a menu
JMP Menu 

;--------------------MULTIPLICACION------------------------
    
Multiplicacion:
	mov ah, 09h 
	lea dx, multiMsg  ;Imprime mensaje 
	int 21h  
	
    call LEER_NUM
    MUL BL
    MOV b.result, AX
    call IMPRIMIR_RES
	
    ;Salta a menu
    JMP Menu 
    
;--------------------PEDIR NUM------------------------
    
LEER_NUM:
    
    MOV A1, 0
    MOV B1, 0
    MOV A2, 0
    MOV B2, 0
    
    MOV num1, 0
    MOV num2, 0
    
    MOV result, 0   
    
    
    MOV AH, 09H                                 
    LEA DX, ingresa
    INT 21H
    
    call guardarDigito
                                     
    MOV b.A1, AL                             
    
    call guardarDigito
    
    MOV b.B1, AL
    
    MOV AX, a1                               
    
    MOV BX, 10                                  
    MUL BX                                      
    
    ADD num1, AX                             
    
    MOV AX, B1                               
    
    ADD num1, AX 
    
    
    MOV AH, 09H                                 
    LEA DX, ingresa
    INT 21H
    
    call guardarDigito
                                     
    MOV b.a2, AL                             
    
    call guardarDigito
                                     
    MOV b.B2, AL                             
    
    MOV AX, a2                               
    
    MOV BX, 10                                  
    MUL BX                                      
    
    ADD num2, AX                             
    
    MOV AX, b2                               
    
    MOV BX, 1                           
    MUL BX
    
    ADD num2, AX 
    
    
    MOV AL, b.num1
    MOV BL, b.num2
ret

guardarDigito:
   MOV AH, 01H                                 
   INT 21H
    
   SUB AL, 30H
   
   CMP AL, 0
   JL msgError
    
   CMP AL, 9
   JG msgError
ret 


;impresiones

IMPRIMIR_RES:
    MOV AH, 09H
    LEA DX, res
    INT 21H

    MOV AX, result    
    MOV CX, 0         
    MOV BX, 10  

CONVER:
    XOR DX, DX        
    DIV BX            
    PUSH DX           
    INC CX            
    CMP AX, 0         
    JNE CONVER

IMPRIMIR:
    POP DX            
    ADD DL, '0'       
    MOV AH, 02H       
    INT 21H           
    LOOP imprimir     
ret 
 
IMPRIMIR_RESN:
    MOV AH, 09H
    LEA DX, res
    INT 21H 
    
    MOV AH, 09H
    LEA DX, menos
    INT 21H

    MOV AX, result    
    MOV CX, 0         
    MOV BX, 10
    JMP CONVER             
ret



ResNeg:  
    MOV aux, BL
    MOV BL, AL
    MOV AL, aux

    SUB AL, BL
    MOV b.result, AL
    call IMPRIMIR_RESN:
JMP menu

ResNor: 
    SUB AL, BL
    MOV b.result, AL
    call IMPRIMIR_RES
JMP menu

divCero: 
    MOV AH, 09H                                     
    LEA DX, div0                                 
    INT 21H
JMP menu 

divNor:
    DIV BL
    MOV b.result, AX
    call IMPRIMIR_RES
JMP menu  

msgError:
    MOV AH, 09H                                     
    LEA DX, Error                                 
    INT 21H
JMP menu


end Inicio