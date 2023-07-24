import cv2
from matplotlib import pyplot as plt

imagen = cv2.imread('1.jpg')
cv2.imshow('color', imagen)

R, G, B=imagen[:,:,0],imagen[:,:,1],imagen[:,:,2]
imgGray= 0.2989*R + 0.5870*G +0.1140*B
plt.imshow(imgGray,cmap='gray')
plt.show()

R,G,B=imagen[:,:,0],imagen[:,:,1],imagen[:,:,2]
imgGrayy= (R + G +B)//3
plt.imshow(imgGrayy,cmap='gray')
plt.show()

img_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gris3', img_gris)
cv2.waitKey(0)
cv2.destroyAllWindows()
