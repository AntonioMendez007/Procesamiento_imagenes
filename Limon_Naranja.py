import cv2
import numpy as np
from matplotlib import pyplot as plt

imagen = cv2.imread('limon.jpg')
#imagen_chica=cv2.resize(imagen,(450,460),interpolation=cv2.INTER_CUBIC)
cv2.imshow('color limon', imagen)
cv2.waitKey(0)

imagen2 = cv2.imread('nara.jpg')
#imagen_chica=cv2.resize(imagen,(450,460),interpolation=cv2.INTER_CUBIC)
#cv2.imshow('color naranja', imagen2)

#-----------------------------------------------------------------------------------
#Segmentación por color a RGB
# Separamos la imagen en los canales de color que la componen.
channels = cv2.split(imagen)
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

# Convertir la imagen de BGR a HSV
hsv_img = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

# Definir los rangos de color para la segmentación
min_color = (0, 0, 0)   # mínimo color a buscar en la imagen
max_color = (255, 255, 255)  # máximo color a buscar en la imagen

# Segmentar la imagen utilizando los rangos de color
mask = cv2.inRange(hsv_img, min_color, max_color)

# Aplicar la máscara a la imagen original para obtener la imagen segmentada
segmented_img = cv2.bitwise_and(imagen, imagen, mask=mask)

# Mostrar la imagen segmentada
cv2.imshow('Imagen Segmentada', segmented_img)


# Cerramos las ventanas creadas por el programa.
plt.close()
cv2.waitKey(0)
cv2.destroyAllWindows()

