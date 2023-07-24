import cv2
import numpy as np

cap = cv2.VideoCapture(0)

ret, frame1 = cap.read()

hsv = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)

lower_blue = np.array([90, 50, 50])
upper_blue = np.array([130, 255, 255])

arrow_length = 100  
arrow_head_width = 20  

prev_gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)

while True:
    ret, frame2 = cap.read()

    hsv2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv2, lower_blue, upper_blue)
    segmented = cv2.bitwise_and(frame2, frame2, mask=mask)

    diff = cv2.absdiff(frame2, frame1)

    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    _, threshold = cv2.threshold(gray, 20, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        contour = max(contours, key=cv2.contourArea)
        (x, y, w, h) = cv2.boundingRect(contour)
        center_x = x + w // 2
        center_y = y + h // 2

        start_point = (int(frame2.shape[1] // 2), int(frame2.shape[0] // 2))
        end_point = (center_x, center_y)

        result = segmented.copy()
        cv2.arrowedLine(result, start_point, end_point, (0, 0, 255), 2)

        cv2.imshow('Segmentación del objeto azul con flecha', result)

    cv2.imshow('Diferencia de imágenes (t - t-1)', diff)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    frame1 = frame2

cap.release()
cv2.destroyAllWindows()