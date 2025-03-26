.stack 1000
.model small

.data
;----TEXTOS
menuOpc db 13, 10, '-----------MENU-----------', 13, 10
        db '1. Consultar', 13, 10
        db '2. Agregar', 13, 10
        db '3. Borrar', 13, 10
        db '4. Salir', 13, 10, 13, 10
        db 'Opcion seleccionada:', 13, 10, '<span class="math-inline">'
menuPers db 13, 10, '\-\-\-\-\-\-\-\-\-\-SELECCSELECCIONAR PERSONA\-\-\-\-\-\-\-\-\-\-', 13, 10
db 'Persona1', 13, 10
db 'Persona2', 13, 10
db 'Persona3', 13, 10
db 'Persona4', 13, 10
db 'Persona Seleccionada\: ', '</span>'

ingNombre db 13, 10, 'Ingrese su nombre: ', 13, 10, '<span class="math-inline">'
ingNControl db 13, 10, 'Ingrese su Numero de Control\: ', 13, 10, '</span>'
ingTel db 13, 10, 'Ingrese su telefono: ', 13, 10, '<span class="math-inline">'
ingCorreo db 13, 10, 'Ingrese su Correo\: ', 13, 10, '</span>'
ingPeso db 13, 10, 'Ingrese su Peso: ', 13, 10, '<span class="math-inline">'
ingEstatura db 13, 10, 'Ingrese su Altura\: ', 13, 10, '</span>'
punto db '.', '<span class="math-inline">'
saltolinea db 13, 10, '</span>'
msgNombre db 'nombre: ', '<span class="math-inline">'
msgNControl db 'Numero de control\: ', '</span>'
msgTel db 'Telefono: ', '<span class="math-inline">'
msgCorreo db 'Correo\: ', '</span>'
msgPeso db 'Peso: ', '<span class="math-inline">'
msgEstatura db 'Estatura\: ', '</span>'
msgImc db 'IMC: ', '<span class="math-inline">'
flagP1 db 0
flagP2 db 0
flagP3 db 0
flagP4 db 0
;\-\-\-\-DATOS PERSONAS \(Redefinidos como cadenas ASCII\)
nombres db 80 dup\('</span>')
numeroscon db 10 dup('<span class="math-inline">'\)
telefonos db 12 dup\('</span>')
correos db 100 dup('<span class="math-inline">'\)
pesos db 6 dup\('</span>')
estaturas db 6 dup('<span class="math-inline">'\)
imcd1 db 6 dup\('</span>')
imcd2 db 6 dup('<span class="math-inline">'\)
imcd3 db 6 dup\('</span>')
imcd4 db 6 dup('<span class="math-inline">'\)
;\-\-\-\-VARIABLES AUXILIARES
nombrebuff db 80, ?, 80 dup\(' '\), '</span>'
ncontrolbuff db 9, 0, 9 dup('<span class="math-inline">'\)
telefonobuff db 11, 0, 11 dup\('</span>')
correobuff db 100, 0, 100 dup('<span class="math-inline">'\)
pesoD1 db ?
pesoD2 db ?
pesoD3 db ?
alturaD1 db ?
alturaD2 db ?
alturaD3 db ?
opcion db ?
opcionPers db ?
\.code
mov ax, @data
mov ds, ax
inicio\:
mov dx, offset menuOpc
mov ah, 09h
int 21h
mov ah, 01h
int 21h
mov opcion, al
sub opcion, 30h
cmp opcion, 4
je salida
mov dx, offset menuPers
mov ah, 09h
int 21h
mov ah, 01h
int 21h
sub al, 30h
mov opcionPers, al
cmp opcion, 1
je consultaPersonas
cmp opcion, 2
je ingresaPersonas
cmp opcion, 3
;je
;\-\-\-\-\-SETTERS
ingresaPersonas\:
mov dx, offset saltolinea
mov ah, 09h
int 21h
mov dx, offset ingNombre
mov ah, 09h
int 21h
mov dx, offset nombrebuff
mov ah, 0ah
int 21h
xor bx, bx
mov bl, nombrebuff\[1\]
mov nombrebuff\[bx \+ 2\], '</span>'
    mov dx, offset nombrebuff + 2

    cmp opcionPers, 1
    je setPersona1
    cmp opcionPers, 2
    je setPersona2
    cmp opcionPers, 3
    je setPersona3
    cmp opcionPers, 4
    je setPersona4
    jmp inicio

setPersona1:
    mov di, offset nombres ; Copia el nombre al buffer de nombres
    mov si, offset nombrebuff + 2
copiarNombre1:
    mov al, [si]
    mov [di], al
    inc di
    inc si
    cmp al, '<span class="math-inline">'
jne copiarNombre1
jmp inicio
setPersona2\:
mov di, offset nombres \+ 80 ; Copia el nombre al buffer de nombres
mov si, offset nombrebuff \+ 2
copiarNombre2\:
mov al, \[si\]
mov \[di\], al
inc di
inc si
cmp al, '</span>'
    jne copiarNombre2
    jmp inicio

setPersona3:
    mov di, offset nombres + 160 ; Copia el nombre al buffer de nombres
    mov si, offset nombrebuff + 2
copiarNombre3:
    mov al, [si]
    mov [di], al
    inc di
    inc si
    cmp al, '<span class="math-inline">'
jne copiarNombre3
jmp inicio
setPersona4\:
mov di, offset nombres \+ 240 ; Copia el nombre al buffer de nombres
mov si, offset nombrebuff \+ 2
copiarNombre4\:
mov al, \[si\]
mov \[di\], al
inc di
inc si
cmp al, '</span>'
    jne copiarNombre4
    jmp inicio

;------GETTERS
consultaPersonas:
    cmp opcionPers, 1
    je getPersona1
    cmp opcionPers, 2
    je getPersona2
    cmp opcionPers, 3
    je getPersona3
    cmp opcionPers, 4
    je getPersona4
    jmp inicio

;------GETTERS CUANDO YA SE HA INGRESADO EL USUARIO
getPersona1:
    mov dx, offset saltolinea
    mov ah, 09h
    int 21h
    mov dx, offset msgNombre
    mov ah, 09h
    int 21h
    mov dx, offset nombres ; Imprime el nombre
    mov ah, 09h
    int 21h
    mov dx, offset saltolinea
    mov ah, 09h
    int 21h
    mov dx, offset msgNControl
    mov ah, 09h
    int 21h
    mov dx, offset numeroscon ; Imprime el numero de control
    mov ah, 09h
    int 21h
    mov dx, offset saltolinea
    mov ah, 09h
    int 21h
    mov dx, offset msgTel
    mov ah, 09h
    int 21h
    mov dx, offset telefonos ; Imprime el telefono
    mov ah, 09h
    int 21h
    mov dx, offset saltolinea
    mov ah, 09h
    int 21h
    mov dx, offset msgCorreo
    mov ah, 09h
    int 21h
    mov dx, offset correos ; Imprime el correo
    mov ah, 09h
    int 21h
    mov dx, offset saltolinea
    mov ah, 09h
    int 21h
    mov dx, offset msgPeso
    mov ah, 09h
    int 21h
    mov dx, offset pesos ; Imprime el peso
    mov ah, 09
    