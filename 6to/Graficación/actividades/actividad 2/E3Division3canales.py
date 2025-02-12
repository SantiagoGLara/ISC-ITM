import cv2
import numpy as np

imagen = cv2.imread('BBWU.png')

B, G, R = cv2.split(imagen)
print(imagen.shape)# un arreglo de 3 datos, donde los primeros 2 son el tamaño y el tercero
# el numero de canales que tiene
baseNegra=np.zeros(imagen.shape[:2], dtype='uint8')
cv2.imshow('ORIGINAL', cv2.merge([B, G, R]))
cv2.imshow('ROJO',cv2.merge([baseNegra, baseNegra, R]))
cv2.imshow('Verde',cv2.merge([baseNegra, G, baseNegra]))
cv2.imshow('AZUL',cv2.merge([B, baseNegra, baseNegra]))
# imprimimos una imagen por cada canal separado
cv2.waitKey(0)