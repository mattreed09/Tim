'''
Created on 21 Nov 2017

@author: matt

Purpose of the code is to move a vehicle depending on whether a set of cameras can see a face. The FacialRecognition function
runs to check if any faces are present.If they are, it prompts the Movement method 'Stop' to run in a separate thread, which
will be terminated if there are no faces detected after a period of time. If this happens, the code will run the 'MoveToward'
method and terminate the stop method.
'''

from multiprocessing import Process
import FacialRecognition as fr
from Movement import Movement as m

if __name__ == '__main__':
    
    numberOfCameras = int(input('Please enter number of cameras: '))
    moving = False
    p1=None
    
    while True:
        result=fr.FacialRecognition(numberOfCameras,moving,3) # Runs the facial recognition and returns when there is a change in faces being present.
        # inputs are the number of cameras, is the car moving (bool) and the number of seconds to wait without a face to begin moving.
        print('MOVING OR STOPPING THE CAR ' + str(moving))
        
        
        if p1 is None:
            d=1
        else:
            p1.terminate()
        if not moving:
            p1=Process(target = m.MoveTowards, args=(result[0],result[1],result[2],))# start a separate thread moving the car
        else:
            p1=Process(target = m.Stop, args=(result[0],))# start a separate thread stopping the car
        p1.start()                
        moving = not moving
    
    p1.terminate()
