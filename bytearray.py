import cv2 as cv
import numpy as np
import os


byteArray = bytearray(os.urandom(120000))
numpyArray = np.array(byteArray)

grayscaleImage = numpyArray.reshape((300,400))
cv.imwrite("randomImage.jpg",grayscaleImage)

bgrImage = numpyArray.reshape(100,400,3)
cv.imwrite("randomImage2.jpg",bgrImage)
