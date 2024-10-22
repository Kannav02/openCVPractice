import numpy as np
import cv2 as cv


numpyArray = np.random.randint(0,256,120000).reshape(100,400,3)


# to get a value from a certain index we use the following 

# this will return the pixel value at 50th row and 200th column for the blue channel, blue =0, 1= green , 2=red
print(numpyArray.item((50,200,0)))

# this would set the pixel value as a certain color again for the same position 
numpyArray.itemset((50,200,0),120)

# Reverse all channels
img = numpyArray[::-1, ::-1, :]  # Flips image completely

# Reverse the entire green channel
img[:, ::-1, 1] = img[:, :, 1]  # Flips horizontally
img[::-1, :, 1] = img[:, :, 1]  # Flips vertically


# numpy array has 3 properties

print(numpyArray.shape) # is a tuple containing the height and the width or the channels if BGR
print(numpyArray.size) # contains the number of elements in the array, for grayscale it is number of pixels, for BGR it is thrice the number of pixels
print(numpyArray.dtype)
