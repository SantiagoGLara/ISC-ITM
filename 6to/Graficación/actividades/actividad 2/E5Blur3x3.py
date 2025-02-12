import numpy as np
import cv2

def filtroBlur(image):
    if image is None:
        print("Error: No se pudo cargar la imagen. Verifica la ruta del archivo.")
        return None
    kernel = np.ones((3, 3), np.float32) / 9
    blureada = cv2.filter2D(image, -1, kernel)
    return blureada
image = cv2.imread('Metamorfosis.jpg')
blured= filtroBlur(image)


if blured is not None:
    cv2.imwrite("kafkaBlured.jpg", blured)
    cv2.imshow('kkkkk', blured)
    cv2.waitKey(0)