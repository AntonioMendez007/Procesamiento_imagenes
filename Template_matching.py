
import cv2
from matplotlib import pyplot as plt

image = cv2.imread("Imagen A.jpeg")
template = cv2.imread("cara.png")
#t = cv2.resize(template, (100,100))

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

res = cv2.matchTemplate(image_gray, template_gray, cv2.TM_SQDIFF)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
print(min_val, max_val, min_loc, max_loc)

x1, y1 = min_loc
x2, y2 = min_loc[0] + template.shape[1], min_loc[1] + template.shape[0]

cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 3)
cv2.imshow("Image", image)
cv2.imshow("Template", template)
cv2.waitKey(0)
cv2.destroyAllWindows()



