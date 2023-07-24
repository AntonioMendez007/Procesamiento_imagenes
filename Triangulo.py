import cv2 
import numpy as np


img= np.zeros((512,512,3),np.uint8)

t = np.array([(200,230,260),(250,160,250)])

#Matriz de traslacion
tras = np.array([(50,50,50)])

#Matriz resultante
res= t + tras
print("\nMatriz trasladada")
print(res)

#Triangulo original
cv2.line(img, (t[0][0],t[1][0]),(t[0][1],t[1][1]),(253,250,0),3)
cv2.line(img, (t[0][1],t[1][1]),(t[0][2],t[1][2]),(253,250,0),3)
cv2.line(img, (t[0][0],t[1][0]),(t[0][2],t[1][2]),(253,250,0),3)

#Triangulo trasladado
cv2.line(img, (res[0][0],res[1][0]),(res[0][1],res[1][1]),(0,0,255),3)
cv2.line(img, (res[0][1],res[1][1]),(res[0][2],res[1][2]),(0,0,255),3)
cv2.line(img, (res[0][0],res[1][0]),(res[0][2],res[1][2]),(0,0,255),3)

cv2.imshow('Triangulo',img)

cv2.waitKey()
cv2.destroyWindow('Triangulo')