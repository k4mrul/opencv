from cv2 import cv2



#####Resize image
##In opencv, width comes first

img = cv2.imread("Resources/maru.jpg")
print(img.shape)  #you should see (400, 400, 3). Where first 400 is the height, second 400 is width, 3 is the channel BGR). In opencv, width comes first

imgResize = cv2.resize(img,(300,200))  #width is 300, height is 200. In opencv, width comes first
print(imgResize.shape)


#####Cropping image
imgCropped = img[0:200,200:500]   #here, height comes first, width comes later. Only opencv, width comes first then height


cv2.imshow("Image", img)
cv2.imshow("Image Resized", imgResize)
cv2.imshow("Image Cropped", imgCropped)

cv2.waitKey(0)