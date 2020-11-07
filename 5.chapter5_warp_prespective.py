from cv2 import cv2
import numpy as np

##Code source: https://github.com/murtazahassan/Learn-OpenCV-in-3-hours

img = cv2.imread("Resources/cards.jpg")

width,height = 250,350  #output image size

pts1 = np.float32([[111,219],[287,188],[154,482],[352,440]])   #setting up image points. upper left, upper right, lower left, lower right
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])  #defining the points that where pts1 are actually located in the image

matrix = cv2.getPerspectiveTransform(pts1,pts2)  #making matrix of the prespective out of image

imgOutput = cv2.warpPerspective(img, matrix, (width,height))   #warping the prespective 

cv2.imshow("Image", img)
cv2.imshow("Output", imgOutput)

cv2.waitKey(0)