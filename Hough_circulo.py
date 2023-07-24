import cv2
import numpy as np


#im = cv2.imread('face2.jpeg')
#img=cv2.resize(im,(650,800),interpolation=cv2.INTER_CUBIC)
im = cv2.imread('face4.jpeg')
img=cv2.resize(im,(650,800),interpolation=cv2.INTER_CUBIC)

img = cv2.imread('ojos_mujer.jpg')
src = cv2.medianBlur(img, 5)
src = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
#edges = cv2.Canny(src,50,150,apertureSize = 3)


circles = cv2.HoughCircles(src, cv2.HOUGH_GRADIENT, 1, 30,
                            param1=40, param2=30, minRadius=7, maxRadius=22)#radio del círculo face2 maxradius=28 param1=52, param2=30
                                                                                    #ojos_mujer minradius=7,maxradius=22 param1=52, param2=30

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # dibujar circulo 
    cv2.circle(img, (i[0], i[1]), i[2], (0,255,0), 2)
    # dibujar centro
    cv2.circle(img, (i[0], i[1]), 2, (0,0,255), 3)
#cv2.imshow('s', edges)
cv2.imshow('detected circles', img)
cv2.waitKey(0)
cv2.destroyAllWindows()