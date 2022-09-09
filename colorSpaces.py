import cv2 as cv


#-----Reading image----------
img = cv.imread('opencv-course/Resources/Photos/park.jpg')
cv.imshow('Park', img)

# 1. Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# 2. BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)


cv.waitKey(0)