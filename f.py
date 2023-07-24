import cv2
import numpy as np
cap = cv2.VideoCapture(0)

while True:
  ret,frame = cap.read()
  #Abrir la cámara

# Convertir la imagen a escala de grises
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
  # Aplicar un filtro Gaussiano para reducir el ruido
  blur = cv2.GaussianBlur(gray, (5, 5), 0)
  #Detectar contorno
  canny = cv2.Canny(frame, 50, 150) 
    # Mostrar la imagen con los contornos dibujados
  cv2.imshow("Contornos", canny)

  # Presionar la tecla 's' para salir del bucle
  if (cv2.waitKey(1) == ord('s')):
      break
cap.release()
cv2.destroyAllWindows()