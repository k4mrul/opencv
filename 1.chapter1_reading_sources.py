#######Read images, videos and webcam


######Code source###############
# https://github.com/murtazahassan/Learn-OpenCV-in-3-hours


from cv2 import cv2

#Image is the array of pixels

###Reading image
#img = cv2.imread("Resources/maru.jpg")  #reading image

#cv2.imshow("Output", img)  #showing image 
#cv2.waitKey(0)   #don't close right after showing image. wait infinite times. 0 means infinite. You can specify seconds 5s = 5000

###Reading video
# cap = cv2.VideoCapture("Resources/cat.mp4")

###Reading webcam
cap = cv2.VideoCapture(0)  # Here 0 is the default webcam value. If you have multiple webcam, value will be different
cap.set(3, 640)   # 3 is the id of width
cap.set(4, 480)   # 4 is the id of height
cap.set(4, 100)   # 10 is the id of brightness

# Info about the properties/values/id: https://docs.opencv.org/3.4/d4/d15/group__videoio__flags__base.html


while True:   #since video is a sequence of images, we need a loop to go through the images
    success, img = cap.read()   #while success, put the read image to img variable
    cv2.imshow("Video", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):     #if q pressed, break the loop
        break