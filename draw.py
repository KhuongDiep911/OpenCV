import cv2 as cv
import numpy as np


blank = np.zeros((500,500), dtype='uint8')  #'uint8' is the data type of an image
cv.imshow('Blank', blank)

# # 1. Paint the image a certain color
# blank[:] = 0,255,0
# cv.imshow('Green', blank)

# 2. Draw a Rectangle
cv.rectancle(blank, (0,0), (250,250), (0,250,0), thickness=2)   # thickness=cv.FILLED or thickness=-1 will fill all the blank
cv.imshow('Rectangle', blank)

# 3. Draw a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=3)
cv.imshow('Circle', blank)

# 4. Draw a line
cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness=3)
cv.imshow('Line', blank)

# 5. Write text
cv.putText(blank, 'Hello', (225,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), thickness=2)
cv.imshow('Text', blank)

img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat', img)

cv.waitKey(0)