import cv2
import numpy as np
 

im = cv2.imread('crucigrama.png')
img=cv2.resize(im,(350,360),interpolation=cv2.INTER_CUBIC)
#cv2.imshow('color naranja', imagen2)
#img = cv2.imread('linea.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3)
cv2.imshow('ss',edges)
cv2.waitKey(0)
minLineLength = 100
maxLineGap = 10
lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1,y1), (x2,y2), (0,255,0), 1, cv2.LINE_AA)

cv2.imshow('Probabilistica',img)

im2 = cv2.imread('crucigrama.png')
img2=cv2.resize(im,(350,360),interpolation=cv2.INTER_CUBIC)
gray2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
edges2 = cv2.Canny(gray2,50,150,apertureSize = 3)
 
lines2 = cv2.HoughLines(edges2,1,np.pi/180,100)
for rho,theta in lines2[0]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))
 
    cv2.line(img2,(x1,y1),(x2,y2),(0,0,255),2)

cv2.imshow('Normal',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()