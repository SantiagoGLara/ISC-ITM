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