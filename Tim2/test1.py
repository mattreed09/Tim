

import cv2
import time

if __name__ == '__main__':
    startTime = time.time()
    now = time.time()
    webcams = [cv2.VideoCapture(2),cv2.VideoCapture(1)]#,cv2.VideoCapture(0)]#,cv2.VideoCapture(3)]
    frame = [0,0]
    while now - startTime  < 10:
        now = time.time()
        for i in range(0,len(webcams)):
            ret0, frame[i] = webcams[i].read()
            gray = cv2.cvtColor(frame[i], cv2.COLOR_BGR2GRAY)
            cv2.imshow('frame1',gray)
            cv2.waitKey(1)
    
    
    
    
    
    
    
    
    
    
    