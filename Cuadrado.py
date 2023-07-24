import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)

t=np.array([(165,120),
            (165,70),
            (100,120),
            (100,70),
            ])

#Matriz al doble
t2=np.array([(2,0),
            (0,2)
            ])
res=np.dot(t,t2)
print(res)

#Matriz a la mitad
t3=np.array([(0.5,0),
            (0,0.5)
            ])
res3=np.dot(t,t3)
res3=res3.astype('int')
print(res3)

#img = cv2.rectangle(img,(210,210),(300,300),(255,0,0),3)
img = cv2.line(img,(t[0][0],t[0][1]),(t[1][0],t[1][1]),(255,200,0),3)
img = cv2.line(img,(t[0][0],t[0][1]),(t[2][0],t[2][1]),(255,200,0),3)
img = cv2.line(img,(t[2][0],t[2][1]),(t[3][0],t[3][1]),(255,200,0),3)
img = cv2.line(img,(t[1][0],t[1][1]),(t[3][0],t[3][1]),(255,200,0),3)

#Imagen al doble
img = cv2.line(img,(res[0][0],res[0][1]),(res[1][0],res[1][1]),(255,200,0),3)
img = cv2.line(img,(res[0][0],res[0][1]),(res[2][0],res[2][1]),(255,200,0),3)
img = cv2.line(img,(res[2][0],res[2][1]),(res[3][0],res[3][1]),(255,200,0),3)
img = cv2.line(img,(res[1][0],res[1][1]),(res[3][0],res[3][1]),(255,200,0),3)

#Imagen a la mitad
img = cv2.line(img,(res3[0][0],res3[0][1]),(res3[1][0],res3[1][1]),(255,200,0),3)
img = cv2.line(img,(res3[0][0],res3[0][1]),(res3[2][0],res3[2][1]),(255,200,0),3)
img = cv2.line(img,(res3[2][0],res3[2][1]),(res3[3][0],res3[3][1]),(255,200,0),3)
img = cv2.line(img,(res3[1][0],res3[1][1]),(res3[3][0],res3[3][1]),(255,200,0),3)

cv2.imshow('Imagen',img)
cv2.waitKey()
cv2.destroyWindow()



