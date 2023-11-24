import cv2
import numpy as np

camera = cv2.VideoCapture(0)

while (True):
    ret, originalVideo = camera.read()
    hsv = cv2.cvtColor(originalVideo, cv2.COLOR_BGR2HSV)

    lower=np.array([155, 0, 0])
    upper=np.array([185, 255, 255])

    maske=cv2.inRange(hsv,lower,upper)
    result=cv2.bitwise_and(originalVideo, originalVideo, mask=maske)
    result=cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
    ret, result = cv2.threshold(result,5,255,cv2.THRESH_BINARY)

    cv2.imshow("Original", originalVideo)
    cv2.imshow("Result",result)

    if cv2.waitKey(50) & 0xFF == ord('x'):
        break

camera.release()
cv2.destroyAllWindows()