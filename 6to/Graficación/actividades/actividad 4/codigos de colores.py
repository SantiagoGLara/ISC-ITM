from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import colorsys

# Función para convertir de RGB a CMY
def rgb_to_cmy(image_array):
    return 1 - image_array / 255.0

# Función para convertir de RGB a HSV
def rgb_to_hsv(image_array):
    hsv_image = np.empty_like(image_array, dtype=float)
    for i in range(image_array.shape[0]):
        for j in range(image_array.shape[1]):
            r, g, b = image_array[i, j] / 255.0
            h, s, v = colorsys.rgb_to_hsv(r, g, b)
            hsv_image[i, j] = [h, s, v]
    return hsv_image

# Función para convertir de RGB a HSL
def rgb_to_hsl(image_array):
    hsl_image = np.empty_like(image_array, dtype=float)
    for i in range(image_array.shape[0]):
        for j in range(image_array.shape[1]):
            r, g, b = image_array[i, j] / 255.0
            h, l, s = colorsys.rgb_to_hls(r, g, b)  # Nota: HLS en colorsys es equivalente a HSL
            hsl_image[i, j] = [h, s, l]
    return hsl_image

# Función para mostrar una imagen junto con sus modelos de color
def display_color_models(image_path):
    # Cargar la imagen
    image = Image.open(image_path).convert("RGB")
    image_array = np.array(image)

    # Convertir la imagen a los modelos de color
    cmy_image = rgb_to_cmy(image_array)
    hsv_image = rgb_to_hsv(image_array)
    hsl_image = rgb_to_hsl(image_array)

    # Crear un gráfico para mostrar las imágenes
    fig, axs = plt.subplots(1, 4, figsize=(20, 5))

    # Mostrar la imagen original (RGB)
    axs[0].imshow(image)
    axs[0].set_title("RGB")
    axs[0].axis("off")

    # Mostrar la imagen en CMY
    axs[1].imshow(1 - cmy_image)  # Volver a CMY para mostrar correctamente
    axs[1].set_title("CMY")
    axs[1].axis("off")

    # Mostrar la imagen en HSV (usando el canal V para visualización)
    axs[2].imshow(hsv_image[:, :, 2], cmap="gray")
    axs[2].set_title("HSV (Canal V)")
    axs[2].axis("off")

    # Mostrar la imagen en HSL (usando el canal L para visualización)
    axs[3].imshow(hsl_image[:, :, 2], cmap="gray")
    axs[3].set_title("HSL (Canal L)")
    axs[3].axis("off")

    plt.tight_layout()
    plt.show()

# Lista de rutas de las imágenes
image_paths = [
    "3agent.jpg",
    "1984.jpg",
    "godot.jpeg",
    "ILOVEBB.jpg",
    "sova.jpg"
]

# Aplicar la conversión a cada imagen
for path in image_paths:
    display_color_models(path)
