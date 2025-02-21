import numpy as np
import matplotlib.pyplot as plt
fig, axs = plt.subplots(2, 3, figsize=(15, 15))

# Círculo
theta = np.linspace(0, 2 * np.pi, 100)
x_circle = np.cos(theta)
y_circle = np.sin(theta)
axs[0, 0].plot(x_circle, y_circle, label="x² + y² = 1")
axs[0, 0].set_title("Círculo")
axs[0, 0].axis("equal")
axs[0, 0].legend()
axs[0, 0].grid()

# Elipse
a, b = 2, 1
x_ellipse = a * np.cos(theta)
y_ellipse = b * np.sin(theta)
axs[0, 1].plot(x_ellipse, y_ellipse, label="(x/a)² + (y/b)² = 1")
axs[0, 1].set_title("Elipse")
axs[0, 1].axis("equal")
axs[0, 1].legend()
axs[0, 1].grid()

# Parábola
y = np.linspace(-10, 10, 100)
x_parabola = y**2 / 4
axs[0, 2].plot(x_parabola, y, label="y² = 4x")
axs[0, 2].set_title("Parábola")
axs[0, 2].legend()
axs[0, 2].grid()

# Hipérbola
x = np.linspace(-5, 5, 100)
y_hyperbola_pos = np.sqrt((x**2 / 4) - 1)
y_hyperbola_neg = -y_hyperbola_pos
axs[1, 2].plot(x, y_hyperbola_pos, label="x²/4 - y²/1 = 1")
axs[1, 2].plot(x, y_hyperbola_neg)
axs[1, 2].set_title("Hipérbola")
axs[1, 2].legend()
axs[1, 2].grid()


# Senoidal
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)
axs[1, 1].plot(x, y, label="y = sin(x)")
axs[1, 1].set_title("Senoidal")
axs[1, 1].legend()
axs[1, 1].grid()

# Desactivar los gráficos restantes
axs[1,0].axis("off")
axs[1, 2].axis("off")

plt.tight_layout()
plt.show()
