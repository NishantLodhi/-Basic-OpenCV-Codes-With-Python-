import numpy as np
import cv2

img = np.zeros((512,512,3), np.uint8) #create window of an black screen

#lines
img = cv2.line(img,(384,0),(400,400),(255,255,0),20)# line in gren
img = cv2.line(img,(10,10),(400,400),(255,0,0),5)#Draw a diagonal blue line with thicknessof 5 

#rectangle
img = cv2.rectangle(img,(384,0),(510,128),(0,255,0),8) #draw rectangle
img = cv2.rectangle(img,(0,0),(100,150),(255,255,0),25) #rectangle
img = cv2.rectangle(img,(250,250),(100,128),(0,0,128),16)

#circle
img = cv2.circle(img,(447,63), 63, (0,255,255), 3)#need centre cordinate and radius and color,thckness
img = cv2.circle(img,(460,70), 45, (255,0,255), 5) #circle
img = cv2.circle(img,(300,305), 50, (128,0,128), 5) #cicle
cv2.imshow('hello',img)
cv2.waitKey(0)


