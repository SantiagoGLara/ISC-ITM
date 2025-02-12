import cv2
import matplotlib.pyplot as plt

imagen=cv2.imread('BBWU.png')
B,G,R=cv2.split(imagen)
Y=.299*R+.587*G+.114*B
print(Y.shape) # tamaño de la imagen, pero como es B/N no sale el tercer elemento del
# ARREGLO, que deberia ser los canales (en este caso, 1)
plt.imshow(Y, cmap='gray')
plt.savefig('BBWUgris.png')
cv2.waitKey(0)