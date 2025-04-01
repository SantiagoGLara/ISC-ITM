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