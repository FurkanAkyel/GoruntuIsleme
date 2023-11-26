import cv2 as cv
import numpy as np

rice = cv.imread("rice.jpg", cv.IMREAD_GRAYSCALE)

thresh, output_bintresh = cv.threshold (rice, 200,255, cv.THRESH_BINARY)
cv.imshow("Esikleme", output_bintresh)
print("Eşikleme tamamlandi", thresh)

thresh, output_otsuthresh = cv.threshold(rice, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
cv.imshow("Otsu Esikleme", output_otsuthresh)
print("Otsu Esikleme", thresh)

kernel = np.ones((5,5),np.uint8)
output_erosion = cv.erode(output_otsuthresh, kernel)
cv.imshow("Puruz Azaltma", output_erosion)

contours, hierarchy = cv.findContours(output_erosion, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

print("Pirinc sayisi:", len(contours))

cv.waitKey(0)
