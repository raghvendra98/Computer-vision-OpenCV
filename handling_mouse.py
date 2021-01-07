## if i click left button of mouse that its show co-ordinate and after clicking right button it shows BGR color of that point
import cv2

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x ,',' , y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ', '+ str(y)
        cv2.putText(img, strXY, (x,y), font, .5, (255, 0, 0), 1)
        cv2.imshow('image',img)
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 0]
        font = cv2.FONT_HERSHEY_SIMPLEX
        strBGR = str(blue) + ', ' + str(green) + ', ' + str(red)
        cv2.putText(img, strBGR, (x, y), font, .5, (0,0, 255), 1)
        cv2.imshow('image', img)

img = cv2.imread('trex.png')

cv2.imshow('image', img)

cv2.setMouseCallback('image',click_event)
cv2.waitKey(0)
