import numpy as np
import cv2

cap = cv2.VideoCapture(0)   #define function to capture video frame

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('H:\\output.mp4',fourcc, 20.0, (640,480)) #record video and save

while(cap.isOpened()):
    ret, frame = cap.read()   #here read the frame
    if ret==True:
        frame = cv2.flip(frame,0) #here flip is used to lip the video at recording time

        # write the flipped frame
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('x'):   #pree s to exit
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()