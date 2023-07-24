import cv2
import numpy as np
 
img = cv2.imread('placa00.png')
#img=cv2.resize(im,(550,360),interpolation=cv2.INTER_CUBIC)

#img = cv2.imread('linea.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,880,apertureSize = 3)
#cv2.imshow('ss',edges)
cv2.waitKey(0)

lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength=100,maxLineGap=10)
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1,y1), (x2,y2), (0,255,0), 2, cv2.LINE_AA)

cv2.imshow('Probabilistica',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
print("-------------------------------------------------------------------------------------------------")
img = cv2.imread('Placa01.jpg')
#img=cv2.resize(im,(550,360),interpolation=cv2.INTER_CUBIC)

#img = cv2.imread('linea.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,90,780,apertureSize = 3)
#cv2.imshow('ss',edges)
cv2.waitKey(0)

lines = cv2.HoughLinesP(edges,1,np.pi/180,22,minLineLength=100,maxLineGap=10)
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1,y1), (x2,y2), (0,255,0), 2, cv2.LINE_AA)

cv2.imshow('Probabilistica',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
print("-------------------------------------------------------------------------------------------------")
img = cv2.imread('Placas02.jpg')
#img=cv2.resize(im,(550,360),interpolation=cv2.INTER_CUBIC)

#img = cv2.imread('linea.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,100,600,apertureSize = 3)
cv2.imshow('ss',edges)
cv2.waitKey(0)

lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength=100,maxLineGap=10)
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1,y1), (x2,y2), (0,255,0), 2, cv2.LINE_AA)

cv2.imshow('Probabilistica',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
