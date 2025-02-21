import matplotlib.pyplot as plt
import numpy as np
import math  # Importar el módulo math para usar math.factorial


def bezier_curve(points, num_points=100):
    n = len(points) - 1
    t = np.linspace(0, 1, num_points)
    curve = np.zeros((num_points, 2))

    for i in range(n + 1):
        curve += np.outer(bernstein_poly(n, i, t), points[i])

    return curve


def bernstein_poly(n, i, t):
    return comb(n, i) * (t ** i) * (1 - t) ** (n - i)


def comb(n, k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))  # Usar math.factorial


def plot_bezier_curve(points):
    curve = bezier_curve(points)

    plt.figure()
    plt.plot(curve[:, 0], curve[:, 1], 'b-', label='Curva de Bézier')
    plt.plot([p[0] for p in points], [p[1] for p in points], 'ro-', label='Puntos de Control')
    plt.legend()
    plt.title('Curva de Bézier')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.show()


# Ejemplo de uso
points = np.array([[0, 0], [1, 3], [4, 4], [5, 0]])
plot_bezier_curve(points)