import cv2
import matplotlib.pyplot as plt

imagen=cv2.imread('Metamorfosis.jpg')

invertida= cv2.bitwise_not(imagen)
cv2.imshow('imagen',invertida)
cv2.imwrite('kafkainvertido.png',invertida)
cv2.waitKey(0)