import cv2
import numpy as np
from matplotlib import pyplot as plt

# Cargar la imagen y convertirla a escala de grises
img = cv2.imread('limo.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
lab_img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#cv2.imshow('Segmentacion del limon hsv', hsv_img)

#--------------Histograma---------------------
# Separamos la imagen en los canales de color que la componen.
channels = cv2.split(img)
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

#-----------------Segmentacion---------------------------------------
# Aplicar umbralización para separar el fondo de los objetos
_, thresh = cv2.threshold(gray_img, 0, 150, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

# Eliminar ruido mediante apertura morfológica
kernel = np.ones((3,3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

# Identificar los contornos de los objetos
contours, hierarchy = cv2.findContours(opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Crear una máscara para el fondo
mask = np.zeros(img.shape[:2], np.uint8)
for c in contours:
    cv2.drawContours(mask, [c], 0, 255, -1)

# Aplicar la máscara a la imagen original para quitar el fondo
result = cv2.bitwise_and(img, img, mask=mask)

# Mostrar la imagen resultante
cv2.imshow('Segmentacion del limon', result)

#----------Segmentacion  LAB---------------------------------------------
# Separar los canales de color LAB
l_channel, a_channel, b_channel = cv2.split(lab_img)

# Aplicar umbralización al canal A para separar el fondo de los objetos
_, a_thresh = cv2.threshold(a_channel, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

# Eliminar ruido mediante apertura morfológica
kernel = np.ones((3,3), np.uint8)
opening = cv2.morphologyEx(a_thresh, cv2.MORPH_OPEN, kernel, iterations=2)

# Identificar los contornos de los objetos
contours, hierarchy = cv2.findContours(opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Crear una máscara para el fondo
mask = np.zeros(lab_img.shape[:2], np.uint8)
for c in contours:
    cv2.drawContours(mask, [c], 0, 255, -1)

# Aplicar la máscara a la imagen original para quitar el fondo
result = cv2.bitwise_and(lab_img, lab_img, mask=mask)

# Mostrar la imagen resultante
cv2.imshow('Segmentacion del limon LAB', result)

#----------------Segmentacion HSV--------------------------------------------
# Definir el rango de colores del fondo en HSV
lower_bound = np.array([20, 50, 50], dtype=np.uint8) # valor mínimo para H, S y V
upper_bound = np.array([120, 255, 255], dtype=np.uint8) # valor máximo para H, S y V

# Aplicar umbralización para separar el fondo de los objetos
mask = cv2.inRange(hsv_img, lower_bound, upper_bound)

# Eliminar ruido mediante apertura morfológica
kernel = np.ones((3,3), np.uint8)
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=2)

# Identificar los contornos de los objetos
contours, hierarchy = cv2.findContours(opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Crear una máscara para el fondo
mask = np.zeros(hsv_img.shape[:2], np.uint8)
for c in contours:
    cv2.drawContours(mask, [c], 0, 255, -1)

# Aplicar la máscara a la imagen ori99898999999999999999999999999999999999999998ginal para quitar el fondo
result = cv2.bitwise_and(hsv_img, hsv_img, mask=mask)

# Mostrar la imagen resultante
cv2.imshow('Segmentacion del limon HSV', result)


plt.close()
cv2.waitKey(0)
cv2.destroyAllWindows()
