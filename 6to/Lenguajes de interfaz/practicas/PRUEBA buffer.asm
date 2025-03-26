org 100h
.data
martin dw 10,13,0
	
.code
mov ax,@data
mov ds,ax
	
		mov dx, offset buffer
		mov ah, 0ah
		int 21h
		jmp print
		buffer db 10,?, 10 dup(' ')
		print:
		xor bx, bx
		mov bl, buffer[1]
		mov buffer[bx+2], '$'
		mov dx, offset buffer + 2
		mov ah, 9
		int 21h    
		mov [martin+2], dx 
		mov dx, [martin+2]
		mov ah,09
		int 21h
.exit