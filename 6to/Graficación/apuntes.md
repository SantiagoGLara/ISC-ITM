# Graficación
## Algoritmo Breseham
- utiliza solo aritmetica de enteros
- eficiente
- no requiere redondeo
- ideal para implementar en hardware
```python
import matplotlib.pyplot as plt

def bresenham(x1, y1, x2, y2):
    puntos = []
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1 #ayudan a definir hacia donde es el incremento en x y y
    sy = 1 if y1 < y2 else -1
    error = dx - dy

    while True:
        puntos.append((x1, y1))
        if x1 == x2 and y1 == y2:
            break
        dobleError = 2 * error
        if dobleError > -dy:
            error -= dy
            x1 += sx
        if dobleError < dx: # va añadiendo los puntos a la lista, que van a ser los puntos que se van a dibujar
                            # es decir, va dibujando uno a uno hasta llegar al punto final (x2, y2)
            error += dx
            y1 += sy

    return puntos

def dibujar_linea(x1, y1, x2, y2):
    puntos = bresenham(x1, y1, x2, y2)
    x_coords, y_coords = zip(*puntos)
    plt.plot(x_coords, y_coords, marker='o')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Algoritmo de Línea de Bresenham')
    plt.grid(True)
    plt.show()

```
# Ejemplo de uso
dibujar_linea(10, 10, 50, 30)
`
### funcionamiento basico

**investigar e implementar el algoritmo de Breseham**
## Algoritmo DDA
- basado en calculo de incrementos de punto flotante
- simple de entender e incrementar
```PYTHON
import matplotlib.pyplot as plt

def linea_dda(x_inicio, y_inicio, x_fin, y_fin):
    # Calcula las diferencias entre las coordenadas iniciales y finales
    diferencia_x = x_fin - x_inicio
    diferencia_y = y_fin - y_inicio
    
    # Determina el número de pasos necesarios
    pasos = max(abs(diferencia_x), abs(diferencia_y))
    
    # Calcula los incrementos en x e y para cada paso
    incremento_x = diferencia_x / pasos
    incremento_y = diferencia_y / pasos
    
    # Inicializa las coordenadas actuales
    x_actual = x_inicio
    y_actual = y_inicio
    
    # Listas para almacenar los puntos de la línea
    puntos_x = []
    puntos_y = []
    
    # Genera los puntos de la línea
    for _ in range(pasos + 1):
        puntos_x.append(round(x_actual))
        puntos_y.append(round(y_actual))
        x_actual += incremento_x
        y_actual += incremento_y
    
    return puntos_x, puntos_y

# Definir los puntos inicial y final de la línea
x_inicio, y_inicio = 2, 3
x_fin, y_fin = 9, 8

# Generar los puntos de la línea usando el algoritmo DDA
puntos_x, puntos_y = linea_dda(x_inicio, y_inicio, x_fin, y_fin)

# Graficar la línea
plt.plot(puntos_x, puntos_y, marker='o', linestyle='-', color='b')
plt.title('Línea generada con el algoritmo DDA')
plt.xlabel('Coordenada X')
plt.ylabel('Coordenada Y')
plt.grid(True)
plt.show()
```

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
```PYTHON
import matplotlib.pyplot as plt

def rellenar_poligono_scanline(vertices):
    # Encontrar los valores mínimo y máximo en el eje Y
    y_min = int(min(v[1] for v in vertices))
    y_max = int(max(v[1] for v in vertices))

    # Lista para almacenar los puntos que se van a rellenar
    puntos_relleno = []

    # Iterar sobre cada línea horizontal (scan-line)
    for y_actual in range(y_min, y_max + 1):
        intersecciones = []

        # Calcular las intersecciones de la línea actual con los bordes del polígono
        for i in range(len(vertices)):
            x1, y1 = vertices[i]
            x2, y2 = vertices[(i + 1) % len(vertices)]  # Conectar el último vértice con el primero

            # Verificar si la línea horizontal intersecta con este borde
            if min(y1, y2) <= y_actual <= max(y1, y2):
                if y1 != y2:  # Evitar divisiones por cero en bordes horizontales
                    # Calcular la coordenada X de la intersección
                    x_interseccion = (y_actual - y1) * (x2 - x1) / (y2 - y1) + x1
                    intersecciones.append(x_interseccion)

        # Ordenar las intersecciones de menor a mayor
        intersecciones.sort()

        # Rellenar los puntos entre pares de intersecciones
        for i in range(0, len(intersecciones), 2):
            x_inicio = int(intersecciones[i])
            x_fin = int(intersecciones[i + 1]) if i + 1 < len(intersecciones) else x_inicio
            for x in range(x_inicio, x_fin + 1):
                puntos_relleno.append((x, y_actual))

    return puntos_relleno

# Definir los vértices del polígono
vertices_poligono = [(50, 50), (200, 100), (150, 200), (100, 150)]

# Aplicar el algoritmo de relleno Scan-Line
puntos_relleno = rellenar_poligono_scanline(vertices_poligono)

# Extraer las coordenadas X e Y de los puntos rellenos
x_relleno = [p[0] for p in puntos_relleno]
y_relleno = [p[1] for p in puntos_relleno]

# Configurar la gráfica
fig, ax = plt.subplots()
ax.set_aspect('equal')  # Mantener la proporción de los ejes

# Dibujar el polígono
vertices_poligono.append(vertices_poligono[0])  # Cerrar el polígono
x_poligono = [v[0] for v in vertices_poligono]
y_poligono = [v[1] for v in vertices_poligono]
ax.plot(x_poligono, y_poligono, 'black', label="Contorno del polígono")

# Dibujar los puntos rellenos
ax.scatter(x_relleno, y_relleno, color='violet', s=1, label="Puntos rellenos")

ax.legend()
ax.set_title("Relleno de un polígono usando el algoritmo Scan-Line")
plt.show()
```

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

### BYTWISE NOT, INVERSION DE COLORES

COMMIT para no dejar abandonado este repo, pero lo odio