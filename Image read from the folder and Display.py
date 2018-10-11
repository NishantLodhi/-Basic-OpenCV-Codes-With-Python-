import numpy as np
import cv2
#lading of image
#Loads a color image. Any transparency of image will be neglected. It is the default flag.
img = cv2.imread('H:\\test.jpg',1)  #this function is used to read the image from location
print("Give image with color==",img)
#cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode
im = cv2.imread('H:\\test2.jpg',0)
print("Image in gray scale==",im)
#cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel
i = cv2.imread('H:\\oprn.jpg',-1)
print("image in alphachanel",i)




#dispaly of an images
cv2.imshow('H:\\oprn.jpg',i)  #here display an image
cv2.imshow('H:\\test.jpg',img)
cv2.imshow('H:\\test2.jpg',im)  
cv2.waitKey(0)                  #now this key is used to close or destroy all windows
cv2.destroyAllWindows()




