import cv2 
import numpy as np

'''
ventana = 255*np.ones((450,300,3),dtype=np.uint8)

cv2.line(ventana,(150,5),(200,5),(255,100,0),2)

cv2.imshow('Vectores',ventana)

cv2.waitKey()
cv2.destroyWindow('Vectores')
'''
'''
ventana2 = 255*np.ones((450,300,3),dtype=np.uint8)

cv2.line(ventana2,(165,170),(165,70),(0,0,255),10)
cv2.line(ventana2,(185,185),(185,85),(0,255,0),10)
cv2.line(ventana2,(200,195),(200,95),(255,0,0),10)
cv2.imshow('Vectoress',ventana2)

cv2.waitKey()
cv2.destroyWindow('Vectoress')
'''
#Matriz
t=np.array([(165,170),(165,70)])
m=np.array([(185,185),(185,85)])
n=np.array([(200,195),(200,95)])

ventana2 = 255*np.ones((450,300,3),dtype=np.uint8)

cv2.line(ventana2,(t[0][0],t[0][1]),(t[1][0],t[1][1]),(0,0,255),10)
cv2.line(ventana2,(m[0][0],m[0][1]),(m[1][0],m[1][1]),(0,255,0),10)
cv2.line(ventana2,(n[0][0],n[0][1]),(n[1][0],n[1][1]),(255,0,0),10)
cv2.imshow('Vectoress',ventana2)

cv2.waitKey()
cv2.destroyWindow('Vectoress')

#Crea un imagen en negro (fondo)
img = np.zeros((512,512,3),np.uint8)

#Matriz
v=np.array([(100,255),(411,255)])

#Dibuja la linea horizontal
#         punto inicial punto final color  grosor
cv2.line(img,(v[0][0],v[0][1]),(v[1][0],v[1][1]),(0,255,0),4)
cv2.imshow('Imagen',img)
cv2.waitKey()
cv2.destroyWindow()






