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