import cv2 as cv
import numpy as np



image = cv.imread("randomImage.jpg")

heightImage, widthImage,_ = image.shape

yMovement = 76
xMovement = 104

for y in range (0,heightImage,yMovement):
    for x in range(0,widthImage,xMovement):

        y1 = y+yMovement
        x1 = x+xMovement

        if x1 > widthImage and y1 > heightImage:
            x1 = widthImage-1
            y1 = heightImage-1

        elif x1 > widthImage:
            x1 = widthImage-1

        elif y1 > widthImage:
            y1 = heightImage-1
        
        cv.rectangle(image,(x,y),(x1,y1),(0,0,255),1)


cv.imwrite("newImage.jpg",image)
        

            

        