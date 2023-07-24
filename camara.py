
import cv2
import numpy as np
from matplotlib import pyplot as plt

capture = cv2.VideoCapture(0)

while (capture.isOpened()):
    #Abrir la cámara
    ret, frame = capture.read()
    ret, frame2 = capture.read()

    #Convertir a escala de grises
    gray= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray2= cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)
    #Convertir a blanco y negro a partir de la escala de grises
    (thresh, im_bw) = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    (thresh, im_bw2) = cv2.threshold(gray2, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    #Diferencia 1
    img_resta=gray2-gray
    cv2.imshow('webCam_gris diferencia',img_resta)
    #cv2.imshow('webCam',frame)
    #cv2.imshow('webCam_gris',gray)
    

    #Hacer segmentación a la escala de grises
    '''
    ret, thresh = cv2.threshold(gray,0,80,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    cv2.imshow('Segmentacion', thresh)
    hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
    plt.plot(hist, color='gray')
    plt.xlabel('intensidad de iluminacion')
    plt.ylabel('cantidad de pixeles')
    plt.show()
    '''
    #Eliminar ruido a la diferencia a escala de grises
    ruido=cv2.fastNlMeansDenoising(img_resta,None,10,7,21)
    plt.subplot(122),plt.imshow(ruido)
    plt.show()
    
    #Mostrar la imagen a blanco y negro
    #img_resta2=im_bw2-im_bw
    #cv2.imshow('webCam_blanco y negro',im_bw)
    #cv2.imshow('webCam_blanco y negro resta',img_resta2)
    
    if (cv2.waitKey(1) == ord('s')):
        break

capture.release()

cv2.destroyAllWindows()