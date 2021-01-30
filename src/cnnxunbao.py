import pyautogui
import pydirectinput
import random
import time
import sys
import os
import argparse
from util import *

import pygetwindow as gw

import tensorflow as tf
from tensorflow import keras
import numpy as np
from PIL import Image

pyautogui.FAILSAFE = False

class xunbao():
    def __init__(self):
        self.walkTime = [0.5,0.6,0.7,0.8]
        self.RandomWalkTime = [1,1.1,1.2,1.3,1.4]
        self.path = '../xunbao/'

  
        self.motions = [[0,-100],
                   [0,100],
                   [-100,0],
                   [100,0],
                   [-100,-100],
                   [100,-100],
                   [-100,100],
                   [100,100]]
        
        self.dirctRagion = [962,1190,240,423]
        self.moveRagion = [165,211,603,643]  
        
        self.scs = 0
        self.scx = 0
        self.scz = 0
        self.scy = 0
        
        # Load the TFLite model and allocate tensors.
        self.interpreter = tf.lite.Interpreter(model_path='../models/shendu2.tflite')
        self.interpreter.allocate_tensors()
        # Get input and output tensors.
        self.input_details = self.interpreter.get_input_details()
        self.output_details = self.interpreter.get_output_details()
    
    
    def walk(self):
        while True:     
            if clickWhenSeeRegion(self.path+'wa.png',self.dirctRagion[0],self.dirctRagion[2],
                          self.dirctRagion[1]-self.dirctRagion[0],
                          self.dirctRagion[3]-self.dirctRagion[2]):
                time.sleep(5)
        
            path = '../runtime/direction.png'
            image = pyautogui.screenshot(region = (1045,299,1105-1045,366-299))  #(1007,270,1141-1007,397-270)
            #im.save(path)
            
            #image = Image.open('../train/zuo/'+str(i)+'.png')
            npImg = np.array(image)
            input_image = npImg / 255
            input_image = np.array(input_image, dtype=np.float32)
            input_image = np.array(input_image)
            input_image = input_image.reshape((1,67,60,3))
            
            self.interpreter.set_tensor(self.input_details[0]["index"], input_image)
            self.interpreter.invoke()
            output_data = self.interpreter.get_tensor(self.output_details[0]['index'])
            result = np.argmax(output_data[0])
            
            if result == 2:   
                print('predict zuo')
                self.scz += 1
                self.scs = 0
                self.scx = 0
                self.scy = 0
                
                randomDragWithinRegion(*self.moveRagion,*self.motions[random.choice([2,4,6])],random.choice(self.walkTime))
                  
            if result == 3:
                print('predict you')
                self.scz = 0
                self.scs = 0
                self.scx = 0
                self.scy += 1
                
                randomDragWithinRegion(*self.moveRagion,*self.motions[random.choice([3,5,7])],random.choice(self.walkTime))
                
            
            if result == 0:        
                print('predict shang')
                self.scz = 0
                self.scs += 1
                self.scx = 0
                self.scy = 0
                
                randomDragWithinRegion(*self.moveRagion,*self.motions[random.choice([0,4,5])],random.choice(self.walkTime))     
                
            if result == 1:           
                print('predict xia')
                self.scz = 0
                self.scs = 0
                self.scx += 1
                self.scy = 0
                
                randomDragWithinRegion(*self.moveRagion,*self.motions[random.choice([1,6,7])],random.choice(self.walkTime))    

            limit = 5
            if max([self.scs,self.scx,self.scz,self.scy]) == limit:
                if self.scz == limit:
                    print('random walk you')
                    randomDragWithinRegion(*self.moveRagion,*self.motions[random.choice([3,5,7])],random.choice(self.RandomWalkTime))
                
                if self.scy == limit:
                    print('random walk zuo')
                    randomDragWithinRegion(*self.moveRagion,*self.motions[random.choice([2,4,6])],random.choice(self.RandomWalkTime))  
                
                if self.scs == limit:
                    print('random walk xia')
                    randomDragWithinRegion(*self.moveRagion,*self.motions[random.choice([1,6,7])],random.choice(self.RandomWalkTime)) 
                
                if self.scx == limit:
                    print('random walk shang')
                    randomDragWithinRegion(*self.moveRagion,*self.motions[random.choice([0,4,5])],random.choice(self.RandomWalkTime)) 
                
                self.scz = 0
                self.scs = 0
                self.scx = 0
                self.scy = 0            
            
            #time.sleep(0.5)
                
            clickWhenSeeRegion(self.path+'shouxia.png',895,629,1133-895,740-629)
            clickWhenSeeRegion(self.path+'queding.png',829,443,1039-829,535-443)   
            clickWhenSeeRegion(self.path+'cross.png',1044,139,1150-1044,219-139)
            clkPos = random.choice([[362,447,484,508],[924,984,495,525]])
            randomClickWithinRegion(*clkPos)
            #time.sleep(1)
        
        #randomDragWithinRegion(x1,x2,y1,y2,disX,disY,holdTime)


if __name__ == '__main__':
    w,h = pyautogui.size()
    window = gw.getWindowsAt(650,350)[0]
    print(window.size)
    window.moveTo(0,0)
    window.resizeTo(1350, 790)
    
    xb = xunbao()
    xb.walk()