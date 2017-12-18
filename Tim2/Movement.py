'''
Created on 21 Nov 2017

@author: matt
'''
import time
import RPi.GPIO as GPIO
import numpy


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)


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
            x = numpy.random.randint(2,size=1)[0]
            print ('x is ' + str(x))
            GPIO.output(17, x)
            GPIO.output(18, 1 - x)
            GPIO.output(22, False)
            GPIO.output(23, True)
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
            GPIO.output(17, False)
            GPIO.output(18, False)
            GPIO.output(22, False)
            GPIO.output(23, False)
            print('stooopping')
            time.sleep(1)
        return 0
    