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