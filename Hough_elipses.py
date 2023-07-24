'''
import cv2
import numpy as np

def detect_ellipses(image):
    # Convertir la imagen a escala de grises
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Aplicar un umbral adaptativo para segmentar la imagen
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    
    # Aplicar la Transformada de Hough para detectar elipses
    ellipses = cv2.HoughCircles(
        thresh, cv2.HOUGH_GRADIENT, dp=2, minDist=30, param1=50, param2=40, 
        minRadius=1, maxRadius=30)
    
    # Dibujar las elipses detectadas en la imagen original
    if ellipses is not None:
        ellipses = np.uint16(np.around(ellipses))
        for ellipse in ellipses[0, :]:
            center = (ellipse[0], ellipse[1])
            axes = (ellipse[1], ellipse[2])
            angle = ellipse[2]
            cv2.ellipse(image, center, axes, angle, 0, 360, (255, 0, 0), 4)
    
    # Mostrar la imagen con las elipses detectadas
    cv2.imshow('Ellipses', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Cargar la imagen
image = cv2.imread('tasa.jpg')
img=cv2.resize(image,(750,680),interpolation=cv2.INTER_CUBIC)
# Llamar a la función para detectar las elipses
detect_ellipses(img)
'''
import cv2

def detectar_elipses(imagen):
    # Convertir la imagen a escala de grises
    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    # Aplicar un desenfoque gaussiano para reducir el ruido
    gris = cv2.GaussianBlur(gris, (5, 5), 0)

    # Aplicar la detección de bordes mediante el operador de Canny
    bordes = cv2.Canny(gris, 50, 150)

    # Encontrar contornos en los bordes
    contornos, _ = cv2.findContours(bordes, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Detectar y dibujar elipses
    for contorno in contornos:
        if len(contorno) >= 5:
            elipse = cv2.fitEllipse(contorno)
            cv2.ellipse(imagen, elipse, (0, 255, 0), 2)

    # Mostrar la imagen con las elipses detectadas
    cv2.imshow("Elipses detectadas", imagen)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Cargar la imagen
imagen = cv2.imread("tasa.jpg")

# Detectar elipses en la imagen
detectar_elipses(imagen)


