'''
Created on 21 Nov 2017

@author: matt
'''
import time
class Movement:
    
    
    def __init__(self):
        self = self
    
    @staticmethod
    def MoveThread(q):
        q.put([42,None, 'hello'])
    
    
    
    @staticmethod
    def MoveTowards(image1,image2,image3):
        angle = Movement.MeasureAngle( image1)
        distance = Movement.MeasureDistance( image1)
        
        '''
        create a smart way here of directing a car toward the point of interest.
        '''
        while True:
            print('moooving')
            time.sleep(1)
        
    
    @staticmethod
    def MeasureAngle( image):
        return 0
        
    @staticmethod
    def MeasureDistance(image):
        return 0
    
    @staticmethod
    def Stop(image):
        while True:
            print('stooopping')
            time.sleep(1)
        
    