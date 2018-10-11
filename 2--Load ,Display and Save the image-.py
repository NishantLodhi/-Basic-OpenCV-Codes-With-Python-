#program to load the image in grey and then save if want and exit

import numpy as np
import cv2 as c

img = c.imread('H:\\test.jpg',1)     #load image in gray
c.imshow('H:\\test.jpg',img)
k = c.waitKey(0)
if k == 27:         # wait for ESC key to exit
    c.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
   
    c.imwrite('H:\\test1.png',img) #write the image
    c.destroyAllWindows()
     