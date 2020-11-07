from cv2 import cv2
import numpy as np

img = cv2.imread("Resources/maru.jpg")
kernel = np.ones((5,5),np.uint8)  #here, we are setting one matrix of 5 by 5. uint8 means unsigned integer (0 to 255)

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #Converting image to gray.Conventionally, we use RGB. But in opencv, we use BGR. Remember that!!!
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)   #ksize must be odd value which is 7. 

#Finding edges of the image
imgCanny = cv2.Canny(img,150,200)  #threshold is 100. You can go higher or lower. Exam, set to 150,200 for lower edges

#Setting thickness of the edges
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)  #iterations=1 means how much thickness we need

#Setting thinner of edges
imgEroded = cv2.erode(imgDialation,kernel,iterations=1)


cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny) 
cv2.imshow("Dialation Image", imgDialation) 
cv2.imshow("Eroded Image", imgEroded) 
cv2.waitKey(0) 