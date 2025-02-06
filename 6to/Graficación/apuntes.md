# Graficación
## Algoritmo Breseham
- utiliza solo aritmetica de enteros
- eficiente
- no requiere redondeo
- ideal para implementar en hardware
### funcionamiento basico

**investigar e implementar el algoritmo de Breseham**
## Algoritmo DDA
- basado en calculo de incrementos de punto flotante
- simple de entender e incrementar

### funcionamiento basico
**investigar e implementar el algoritmo de Breseham**
| Breseham  |   DDA     |
|-----------|-----------|
| Fila 1    | Dato 1    |
| Fila 2    | Dato 2    |
| Fila 3    | Dato 3    |
|           |           |

## Algoritmo Scan-Line
- metodo para rellenar poligonos en grafico
- procesa el poligono linea por linea horizontalmente
- Determina los puntos interiores del polígono
### aplicaciones
- renderizado 2d
- procesamiento de imagenes
### elementos clave
- linea de escaneo(scan-line): linea horizontal que atraviesa el poligono
- puntos de interseccion: donde la linea cruza con bordes
- Aristas activas: bordes que intersectan la linea de escaneo actual
- lista de bordes: almacena informacion de las aristas

**investigar e implementar scan-line**

## procesamiento de imagenes
para procesar una imagen usaremos python image y python pillow, una imagen es un arreglo de arreglos y cuenta con su propio formato

### formatos de imagen
- png(portable Network Grafics): cuenta con transparencia, no pierde calidad al ser comprimido
- jpeg(): para imagenes con muchos colores, pero si pierde calidad y no tiene transparencia
- gif(graphics interchange format): animaciones 
### rgb
| R  | G | B  | COLOR  | 
|----|----|----|----|
| 0 | 0  | 0  | NEGRO  |
| 0 | 0  | 255  | AZUL | 
| 0| 255 | 0 | VERDE | 
| 255 | 0 | 0 | ROJO |
En el caso de imagenes rgb, la imagen es un arreglo de arreglos(cada celda tiene 3 valores, de la cantidad de R-G-B que tiene cada pixel), tambien se puede hacer en hexadecimal, pero es mas usado en diseño como web, que en programación.
### escala de grises
el arreglo de la imagen es unicamente de 0-255, pero unicamente un valor por pixel
### para cambiar fondo de una imagen
conociendo que una imagen es una matriz de arreglos
primero: leemos la imagen


