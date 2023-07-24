import cv2
import numpy as np
from matplotlib import pyplot as plt

lower_red = np.array([-1,50,50])
upper_red = np.array([3,255,255])

capture = cv2.VideoCapture(0)
capture.set(3, 640)
capture.set(4, 480)

while (capture.isOpened()):
    #Abrir la cámara
    ret, frame = capture.read()
    
    #Convertir a escala de grises
    gray= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    '''
    #--------------Histograma---------------------
    # Separamos la imagen en los canales de color que la componen.
    channels = cv2.split(frame)
    # Inicializamos el lienzo donde dibujaremos el histograma.
    plt.figure()
    plt.title("Histograma de Color ")
    plt.xlabel('Bins')
    plt.ylabel('# de pixeles')
    plt.xlim((0, 256))

    # Iteramos sobre cada canal de color...
    colors = ('b', 'g', 'r')
    for (channel, color) in zip(channels, colors):
        # Calculamos el histograma del canal actual.
        histogram = cv2.calcHist([channel], [0], None, [256], [0, 256])

        # Lo añadimos al gráfico.
        plt.plot(histogram, color=color)
    # Mostramos el gráfico.
    plt.show()
    '''
    #-----------------Segmentacion--------------------------------------   
    # Convertir el frame de video a formato HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
    # Aplicar una máscara para obtener solo los píxeles que están dentro del rango de colores especificado
    mask = cv2.inRange(hsv, lower_red, upper_red)
        
    # Aplicar la máscara al frame original para obtener solo los píxeles del color deseado
    res = cv2.bitwise_and(frame, frame, mask= mask)
    
    #Eliminar ruido a la diferencia a escala de grises para segmentar
    ruido=cv2.medianBlur(res,7)
    # Aplicar un filtro Gaussiano para reducir el ruido para detectar contorno
    #blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Mostrar el color segmentado
    cv2.imshow('Segmentacion',ruido)

    #Detectar contorno
    canny = cv2.Canny(ruido, 100, 150) 
    # Mostrar la imagen con los contornos dibujados
    cv2.imshow("Contornos", canny)
        
    # Presionar la tecla 's' para salir del bucle
    if (cv2.waitKey(1) == ord('s')):
        break

capture.release()

cv2.destroyAllWindows()