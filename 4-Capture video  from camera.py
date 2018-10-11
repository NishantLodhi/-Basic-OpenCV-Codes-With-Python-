import numpy as np
import cv2 as c

cap = c.VideoCapture(0) #used to capture videos from camera

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()     #return true if capture correctly

    # Our operations on the frame come here
    gray = c.cvtColor(frame, c.COLOR_BGR2GRAY)

    # Display the resulting frame
    c.imshow('frame',gray)
    if c.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()   #realease the frames


print( "the value ==",cap.get(3))
print( "the value ==",cap.get(4))
c.destroyAllWindows()