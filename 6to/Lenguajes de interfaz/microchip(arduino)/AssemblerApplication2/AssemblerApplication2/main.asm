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
