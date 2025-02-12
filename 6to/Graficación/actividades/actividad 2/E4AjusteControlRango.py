import cv2
import numpy as np

imagen=cv2.imread('Metamorfosis.jpg')
brightness=100 # valores entre 0 y 255
brillosa=cv2.add(imagen, np.array([brightness],dtype=np.uint8))
cv2.imshow('imagen',brillosa)
cv2.imwrite('kafkaBrillosa.jpg',brillosa)
cv2.waitKey(0)
