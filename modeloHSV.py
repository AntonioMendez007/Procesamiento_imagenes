import cv2
from matplotlib import pyplot as plt

imagen = cv2.imread('pollo.jpg')
imagen_chica=cv2.resize(imagen,(350,240),interpolation=cv2.INTER_CUBIC)
cv2.imshow('color', imagen_chica)

#HSV
img_gris = cv2.cvtColor(imagen_chica,cv2.COLOR_BGR2HSV)
cv2.imshow('HSV', img_gris)

#Gris
img_gris = cv2.cvtColor(imagen_chica, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gris', img_gris)

#YUV 
img_yuv = cv2.cvtColor(imagen_chica,cv2.COLOR_BGR2YUV)
cv2.imshow('YUV', img_yuv)
cv2.waitKey(0)
cv2.destroyAllWindows()