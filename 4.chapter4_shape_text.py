from cv2 import cv2
import numpy as np 

# img = np.zeros((512,512))  #filling matrix with 512 by 512 boxes/pixels. It's a grayscale image
# print(img.shape)

img = np.zeros((512,512,3),np.uint8)  #filling matrix with 512 by 512 boxes/pixels with 3 channels, from 0 to 255

######coloring the image
# print(img)
#img[:]= 255,0,0   #coloring blue for whole image.

######Drawing line over image
# cv2.line(img,(0,0),(300,300),(0,255,0),3)  #0,0 is starting and 300,300 is ending point, color is (0,255,0), thickness is 3
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)  #0,0 is starting and shape[1] is width, shape[0] is height, color is (0,255,0), thickness is 3

######Ractangle
# cv2.rectangle(img,(0,0),(250,350),(0,0,255),cv2.FILLED)
cv2.rectangle(img,(0,0),(250,350),(0,0,255),2)


######Circle
cv2.circle(img,(400,50),30,(255,255,0),5)  #400,50 is center, 30 is radius, (255,255,0) is color & thickness is 5


######Putting text on image
cv2.putText(img," OpenCV ", (300,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),2) #origin is 300,300, fontFace is cv2's own font family, fontScale is how much big the font is, (0,150,0) is color, thickness=2


cv2.imshow("Image",img)
cv2.waitKey(0)