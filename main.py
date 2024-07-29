import cv2
import numpy as np



baseImg = cv2.imread('liquid.jpg')
gray = cv2.cvtColor(baseImg, cv2.COLOR_BGR2GRAY)

def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(baseImg, (x, y), 100, (0, 255, 255), -1)

cv2.namedWindow("Working Window")

cv2.setMouseCallback("Working Window", draw_circle)

while True:
    cv2.imshow("Working Window", baseImg)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
