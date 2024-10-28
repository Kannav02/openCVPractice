import cv2 as cv
import numpy as np



def edgeStroke(image,destinationImage,blurKernelSize:int=3,edgeKernelSize:int=3):
    if blurKernelSize >= 3:
        blurredImage = cv.medianBlur(image,blurKernelSize)
        graySrc = cv.cvtColor(blurredImage,cv.CVT_BGR2GRAY)
    else:
        graySrc = cv.cvtColor(image,cv.CVT_BGR2GRAY)

    cv.Laplacian(graySrc, cv.CV_8U, graySrc, ksize = edgeKernelSize)

    normalizedAlpha = (1/255) * (255 - graySrc)

    channels=cv.split(image)
    
    for channel in channels:
        channel[:] = channel * normalizedAlpha
    
    cv.merge(channels,destinationImage)
