import cv2
import numpy as np


baseImg = cv2.imread('liquid.jpg')
gray = cv2.cvtColor(baseImg, cv2.COLOR_BGR2GRAY)

def drawCircle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(baseImg, (x, y), 100, (0, 255, 255), 2)

cv2.namedWindow("Working Window")

cv2.setMouseCallback("Working Window", drawCircle)

while True:
    cv2.imshow("Working Window", gray)

    if cv2.waitKey(0):
        break

cv2.destroyAllWindows()
