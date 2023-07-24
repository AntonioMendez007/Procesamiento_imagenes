import cv2
from matplotlib import pyplot as plt
import numpy as np

imagen = cv2.imread('pollo.jpg')
img=cv2.resize(imagen,(250,140),interpolation=cv2.INTER_CUBIC)
cv2.imshow('color', img)


hist = cv2.calcHist([img], [2], None, [256], [0, 256])
plt.plot(hist, color='red')
plt.xlabel('intensidad-iluminacion')
plt.ylabel('cantidad-pixeles')
plt.show()

hist = cv2.calcHist([img], [1], None, [256], [0, 256])
plt.plot(hist, color='green')
plt.xlabel('intensidad-iluminacion')
plt.ylabel('cantidad-pixeles')
plt.show()

hist = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.plot(hist, color='blue')
plt.xlabel('intensidad-iluminacion')
plt.ylabel('cantidad-pixeles')
plt.show()

#Gris
img_gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gris', img_gris)
hist = cv2.calcHist([img_gris], [0], None, [256], [0, 256])
plt.plot(hist,color='gray')
plt.xlabel('intensidad-iluminacion')
plt.ylabel('cantidad-pixeles')
plt.show()