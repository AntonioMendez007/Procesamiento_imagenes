
import cv2
import numpy as np
from matplotlib import pyplot as plt

capture = cv2.VideoCapture(0)

while (capture.isOpened()):
    #Abrir la cámara
    ret, frame = capture.read()

    #Convertir a escala de grises y eliminar ruido
    src = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    src = cv2.medianBlur(src, 5)
    
    
    circles = cv2.HoughCircles(src, cv2.HOUGH_GRADIENT, 1, 30,
                            param1=60, param2=30, minRadius=1, maxRadius=28)#radio del círculo face2 maxradius=28 param1=52, param2=30
                                                                                    #ojos_mujer minradius=7,maxradius=22 param1=52, param2=30
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            # Dibujar el círculo y el centro
            cv2.circle(frame, (i[0], i[1]), i[2], (0, 255, 0), 2)
            cv2.circle(frame, (i[0], i[1]), 2, (0, 0, 255), 3)
    

    # Aplicar la detección de bordes mediante el operador de Canny
    '''
    bordes = cv2.Canny(src, 50, 200)

    # Encontrar contornos en los bordes
    contornos, _ = cv2.findContours(bordes, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Detectar y dibujar elipses
    for contorno in contornos:
        if len(contorno) >= 5:
            elipse = cv2.fitEllipse(contorno)
            cv2.ellipse(frame, elipse, (0, 255, 0), 2)
    '''
    #cv2.imshow('webCam',src)
    cv2.imshow('iris',frame)

    if (cv2.waitKey(1) == ord('s')):
        break

capture.release()

cv2.destroyAllWindows()