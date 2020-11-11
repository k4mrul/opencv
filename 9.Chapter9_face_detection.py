#we will use opencv's library to detect the faces. If you want to detect the custom object or you want to build something custom, use this tutorial: https://www.youtube.com/watch?v=dZ4itBvIjVY


from cv2 import cv2

faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")

img = cv2.imread('Resources/khabib.jpg')
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#find the faces of image using face cascade
faces = faceCascade.detectMultiScale(imgGray,1.1,4)

#bounding box around faces 
for (x,y,w,h) in faces: 
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow("Result", img)
cv2.waitKey(0)