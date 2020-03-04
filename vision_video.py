
import cv2
import time
import numpy as np

video_write = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter('ABHINAV.mp4', video_write, 20.0, (640, 480))

# captures video
cap = cv2.VideoCapture(0)

# setting time to 'n' seconds after which video starts capturing
time.sleep(3)

# captures video for the backgroud
for i in range(10):
    ret, background = cap.read()
t0 = time.time()

# while the camera is opened, it keeps capturing video foreground
while(cap.isOpened()):
    
    ret, foreground = cap.read()
    
    foreground = cv2.bitwise_and(foreground, foreground)
    background = cv2.bitwise_and(background, background)
    
    # adding static frame and dynamic frames
    
    full = cv2.add(foreground, background)
    
    # writing output and showing the same
    output.write(full)
    cv2.imshow('ABHINAV', full)
    
    # waitkey to manually stop capturing video
    if cv2.waitKey(1) & 0xFF == ord('a'):
        break
    
    # time to automatically stop capturing video after pre-defined time in seconds
    t1 = time.time() 
    num_seconds = t1 - t0 
    if num_seconds > 10:  
        break
        

# closing all the camera windows
cap.release()
output.release()
cv2.destroyAllWindows()

