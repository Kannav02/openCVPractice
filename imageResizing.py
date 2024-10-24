import cv2 as cv
import numpy as np

firstImage = cv.imread("randomImage.jpg")


# resizing 

height,width,c = firstImage.shape
# shape returns in the format height and width, but in normal functions it is used as width. height

size = (width,height)


# here it uses the format of width and height
# then different interpolation properties can be described here
resized_image1 = cv.resize(firstImage,(200,400),interpolation=cv.INTER_LINEAR)

cv.imshow("resized",resized_image1)
cv.waitKey(0)
cv.destroyAllWindows()

