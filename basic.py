import cv2 as cv
import numpy as np


# 3x3 grayscale image
img = np.zeros((3,3),dtype=np.uint8)
height, width = img.shape
# converts it into a single array of size 3x3 which is 9
byteArray = bytearray(img)
print(img)

img = cv.cvtColor(img,cv.COLOR_GRAY2BGR)



print(img)


# converts it back to a 2D matrix of size 3x3
grayScaleImage = np.array(byteArray).reshape(height,width)

print(grayScaleImage)
