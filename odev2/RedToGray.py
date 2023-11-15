import cv2
import numpy as np

camera = cv2.VideoCapture(0)

while (True):
    ret, originalVideo = camera.read()
    hsv = cv2.cvtColor(originalVideo, cv2.COLOR_BGR2HSV)

    lower=np.array([0, 100, 20])
    upper=np.array([10, 255, 255])

    maske=cv2.inRange(hsv,lower,upper)
    result=cv2.bitwise_and(originalVideo, originalVideo, mask=maske)
    result=cv2.cvtColor(result, cv2.COLOR_BGR2HSV)
    result[:, :, 0] = 0
    result[:, :, 1] = 0
    ret, result = cv2.threshold(result,0,255,cv2.THRESH_BINARY)

    cv2.imshow("Original", originalVideo)
    cv2.imshow("Result",result)

    if cv2.waitKey(50) & 0xFF == ord('x'):
        break

camera.release()
cv2.destroyAllWindows()