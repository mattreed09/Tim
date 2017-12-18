'''
Created on 23 Nov 2017

@author: matt reed

The facial recognition part of this code was taken from 
https://github.com/shantnu/FaceDetect
simply put this code loops over the number of cameras available, takes an image, then runs it through a facial detection
program form openCV. If  it finds faces, it updates the list IsThereAFace to True or False if there are no faces. If 
IsTheCarMoving is False we check if IsThereAFace sums to 0, and if so we start a timer to count until we reach DelayUntilMoveSeconds,
after which we return the array of lastCamera, lastFace and lastImage, so these can be passed to Movement.MoveToward to 
inform it of the direction it needs to send the vehicle.
'''
import cv2
import time


def FacialRecognition(cameraCount, IsTheCarMoving, DelayUntilMoveSeconds):

    
    cascPath = "/home/pi/Downloads/Tim-master/Tim2/lbpcascade_frontalface_improved.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)
    
    i, start, end=[cameraCount-1,0,0]
    lastCamera ,lastFace , lastImage,isTimerGoing= [[0],[0],[0],False]
    
    while True:
        print('startingLoop')
        beforeLoopTime = time.time()
        webcams = [cv2.VideoCapture(0)]
        frame = [0]
        IsThereAFace= [not IsTheCarMoving]
        for i in range(1,cameraCount):
                webcams.append(cv2.VideoCapture(i))
                frame.append(0)
                IsThereAFace.append(not IsTheCarMoving)
        now = time.time()
        while now - beforeLoopTime < 30:
            startTime = time.time()
            i = (i + 1) % cameraCount
            print("here " + str(i))
            ret0, frame[i] = webcams[i].read()
            gray = cv2.cvtColor(frame[i], cv2.COLOR_BGR2GRAY)
            cv2.imshow('frame1',gray)
            cv2.waitKey(1)        
            secondTime = time.time()
            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.25,
                minNeighbors=2,
                minSize=(40, 40)
                )
               #print("Found {0} faces!".format(len(faces)))
            thirdTime = time.time()
            if len(faces) > 0:
                IsThereAFace[i] = True
                '''for (x, y, w, h) in faces:
                    cv2.rectangle(frame[i], (x, y), (x+w, y+h), (0, 255, 0), 2)
                    cv2.imshow("Faces found", frame[i])
                    cv2.waitKey(1)'''
                isTimerGoing,lastCamera[0],lastFace[0],lastImage[0]  = [False,i,faces[0],gray]  # If there is a face, this information tells us where
            else :
                IsThereAFace[i] = False            
            if sum(IsThereAFace) == 0 and IsTheCarMoving == False and isTimerGoing == False:
                isTimerGoing = True
                start = time.time()
            if isTimerGoing:
                end = time.time()
            else :
                end = start            
            if end - start > DelayUntilMoveSeconds:
                #print('the car is moving')
                for cam in webcams:
                    cam.release()
                return [lastCamera[0],lastFace[0],lastImage[0]]
                #return 0
                    
            if sum(IsThereAFace) > 0 and IsTheCarMoving == True:
                for cam in webcams:
                    cam.release()
                #print('the car is stopping')
                return [lastCamera[0],lastFace[0],lastImage[0]]
            
            
            now = time.time()
            print(round(end - start,1))
            print(round(now - startTime,3))
        for cam in webcams:
                    cam.release()