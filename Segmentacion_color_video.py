import cv2
import numpy as np
from matplotlib import pyplot as plt

#Definir los valores del color rojo
#lower_red = np.array([-1,50,50])
#upper_red = np.array([3,255,255])

# Definir los valores del color azul
lower_blue = np.array([91, 50, 50])
upper_blue = np.array([130, 255, 255])


capture = cv2.VideoCapture(0)
capture.set(3, 640)
capture.set(4, 480)

# Medidas de la fecha
arrow_length = 100  
arrow_head_width = 20  

while (capture.isOpened()):
    #Abrir la cámara
    ret, frame = capture.read()
    ret, frame2 = capture.read()

    #Convertir a escala de grises
    gray= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray2= cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)
    
    #-----------------Segmentacion--------------------------------------   
    # Convertir el frame de video a formato HSV tanto para el frame y el frame 2
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hsv2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2HSV)

    # Aplicar una máscara para obtener solo los píxeles que están dentro del rango de colores especificado
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    mask2 = cv2.inRange(hsv2, lower_blue, upper_blue)

    # Aplicar la máscara al frame original para obtener solo los píxeles del color deseado para poder separar el color del fondo
    res = cv2.bitwise_and(frame, frame, mask= mask)
    res2 = cv2.bitwise_and(frame2, frame2, mask= mask2)

    #Eliminar ruido de la segemtación realizada para que se vea un poco más suavizada
    ruido=cv2.medianBlur(res,7)
    ruido2=cv2.medianBlur(res2,7)

    #Se obtiene la diferencia de T - (T-1)
    diferencia=ruido2-ruido
    
    # Orientación del objeto
    gray3 = cv2.cvtColor(diferencia, cv2.COLOR_BGR2GRAY)
    # Obtener el umbral de la conversión a escala de grises de la diferencia
    _, threshold = cv2.threshold(gray3, 20, 255, cv2.THRESH_BINARY)
    # Identificar el contorno del objeto a partir del umbral
    contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        # Se obtiene el valor maximo que hay en el contorno del objeto
        contour = max(contours, key=cv2.contourArea)
        (x, y, w, h) = cv2.boundingRect(contour)
        # Se define el centro en la posición (x,y) de donde va a partir la flecha
        centro_x = x + w // 2
        centro_y = y + h // 2

        #Se define el punto inicial de la flecha
        start_point = (int(frame2.shape[1] // 2), int(frame2.shape[0] // 2))
        # Punto final de la flecha en el frame
        end_point = (centro_x, centro_y)

        #Se genera otra "ventana" duplicada de la segmentación del objeto para mostrar la flecha"
        result = ruido.copy()
        # Se genera la flecha en la ventana segmentada con el punto inicial, final, el color y el grosor
        cv2.arrowedLine(result, start_point, end_point, (0, 0, 255), 2)

        cv2.imshow('Orientacion del objeto segmentado', result)

    # Mostrar el color segmentado sin la flecha
    #cv2.imshow('frame',ruido)

    #Diferencia T - (T-1)   
    cv2.imshow('frame diferencia',diferencia)
        
    # Presionar la tecla 's' para salir del bucle
    if (cv2.waitKey(1) == ord('s')):
        break

capture.release()

cv2.destroyAllWindows()