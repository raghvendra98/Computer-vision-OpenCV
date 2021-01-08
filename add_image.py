import numpy as np
import cv2

img1 = cv2.imread("beach.png")
img2 = cv2.imread('trex.png')

print(img1.shape)
print(img1.size)
print(img1.dtype)
b,g,r =cv2.split(img1)
img = cv2.merge((b,g,r))

ball = img[280:340, 330:390]


img1 = cv2.resize(img1, (512,512))
img2 = cv2.resize(img2, (512,512))

imgg = cv2.addWeighted(img1, .4, img2, .6, 0);
cv2.imshow('image', imgg)
cv2.waitKey(0)
cv2.destroyAllWindows()


