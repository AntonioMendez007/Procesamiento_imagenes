import cv2
import numpy as np
from matplotlib import pyplot as plt

imagen = cv2.imread('2.jpeg')
imagen_chica=cv2.resize(imagen,(450,460),interpolation=cv2.INTER_CUBIC)
#cv2.imshow('color', imagen_chica)
#Gris
img_gris = cv2.cvtColor(imagen_chica, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gris', img_gris)
'''
ret, thresh = cv2.threshold(img_gris,10,80,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
cv2.imshow('Segmentacion', thresh)


hist = cv2.calcHist([img_gris], [0], None, [256], [0, 256])
plt.plot(hist, color='gray' )

plt.xlabel('intensidad de iluminacion')
plt.ylabel('cantidad de pixeles')
plt.show()
'''
ruido=cv2.fastNlMeansDenoising(img_gris,None,10,7,21)
#f=cv2.fastNlMeansDenoisingColored(imagen_chica,None,10,10,7,21)
plt.subplot(122),plt.imshow(ruido)
#plt.subplot(122),plt.imshow(imagen_chica)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()