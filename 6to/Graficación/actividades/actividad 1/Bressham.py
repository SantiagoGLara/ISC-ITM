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

# Ejemplo de uso
dibujar_linea(10, 10, 50, 30)