import pyautogui
import pydirectinput
import random
import time
import sys
import os
import argparse
from util import *

import pygetwindow as gw

pyautogui.FAILSAFE = False

class xunbao():
    def __init__(self):
        self.walkTime = [0.5,1,1.5]
        self.RandomWalkTime = [2,3,4]
        self.path = '../xunbao/'
        self.directions = [self.path+'shang.png',
                      self.path+'xia.png',
                      self.path+'zuo.png',
                      self.path+'you.png',
                      self.path+'zuoshang.png',
                      self.path+'youshang.png',
                      self.path+'zuoxia.png',
                      self.path+'youxia.png']
        
        self.zuos = [self.path+'zuo.png',self.path+'zuoshang.png',
                    self.path+'zuoxia.png',self.path+'zuo2.png',
                    self.path+'zuo3.png',self.path+'zuo4.png',
                    self.path+'zuo5.png',self.path+'zuo6.png',
                    self.path+'zuo7.png',self.path+'zuo8.png',
                    self.path+'zuo9.png',self.path+'zuo10.png',
                    self.path+'zuo11.png',self.path+'zuo12.png',
                    self.path+'zuo13.png',self.path+'zuo14.png',
                    self.path+'zuo15.png'
                    
                    
                    ]
                    
        self.yous = [self.path+'you.png',self.path+'youshang.png',
                     self.path+'youxia.png',self.path+'you2.png',
                     self.path+'you3.png',self.path+'you4.png',
                     self.path+'you5.png',self.path+'you6.png',
                     self.path+'you7.png',self.path+'you8.png',
                     self.path+'you9.png']
                     
        self.shangs = [self.path+'shang.png',
                       self.path+'shang2.png',
                       self.path+'shang3.png',
                       self.path+'shang4.png',
                       self.path+'shang5.png',
                       self.path+'shang6.png',
                       self.path+'shang7.png',
                       self.path+'shang8.png',
                       self.path+'shang9.png',
                       self.path+'shang10.png',
                       self.path+'shang11.png',
                       self.path+'shang12.png',
                       
                       ]
        
        self.xias = [self.path+'xia.png',
                     self.path+'xia2.png',
                     self.path+'xia3.png',
                     self.path+'xia4.png',
                     self.path+'xia5.png',
                     self.path+'xia6.png',
                     self.path+'xia7.png',
                     self.path+'xia8.png',
                     self.path+'xia9.png',
                     self.path+'xia10.png',
                     self.path+'xia11.png',
                     self.path+'xia12.png',
                     self.path+'xia13.png',
                     self.path+'xia14.png',
                     self.path+'xia15.png',
                     
                     
                     
                     
                     ]
        
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
        
        self.stackCount = 0
    
    def walk(self):
        while True:
            isFound = False 
            random.shuffle(self.zuos)
            if hasImgsRegion(self.zuos,self.dirctRagion[0],self.dirctRagion[2],
                                      self.dirctRagion[1]-self.dirctRagion[0],
                                      self.dirctRagion[3]-self.dirctRagion[2]):
                                      
                randomDragWithinRegion(*self.moveRagion,*self.motions[random.choice([2,4,6])],random.choice(self.walkTime))
                isFound = True

            random.shuffle(self.yous)    
            if hasImgsRegion(self.yous,self.dirctRagion[0],self.dirctRagion[2],
                                      self.dirctRagion[1]-self.dirctRagion[0],
                                      self.dirctRagion[3]-self.dirctRagion[2]):
                                      
                randomDragWithinRegion(*self.moveRagion,*self.motions[random.choice([3,5,7])],random.choice(self.walkTime))
                isFound = True
            
            random.shuffle(self.shangs)            
            if hasImgsRegion(self.shangs,self.dirctRagion[0],self.dirctRagion[2],
                                      self.dirctRagion[1]-self.dirctRagion[0],
                                      self.dirctRagion[3]-self.dirctRagion[2]):
                                      
                randomDragWithinRegion(*self.moveRagion,*self.motions[random.choice([0,4,5])],random.choice(self.walkTime))     
                isFound = True
                
            random.shuffle(self.xias)
            if hasImgsRegion(self.xias,self.dirctRagion[0],self.dirctRagion[2],
                                      self.dirctRagion[1]-self.dirctRagion[0],
                                      self.dirctRagion[3]-self.dirctRagion[2]):
                                      
                randomDragWithinRegion(*self.moveRagion,*self.motions[random.choice([1,6,7])],random.choice(self.walkTime))    
                isFound = True
            
            if not isFound:
                if clickWhenSeeRegion(self.path+'wa.png',self.dirctRagion[0],self.dirctRagion[2],
                                      self.dirctRagion[1]-self.dirctRagion[0],
                                      self.dirctRagion[3]-self.dirctRagion[2]):
                    
                    self.stackCount = 0
                    time.sleep(2)
                    clickWhenSeeRegion(self.path+'shouxia.png',895,629,1133-895,740-629)
                    
                else:
                    #break
                    print('random walk')
                    randomMotion = random.choice(self.motions)
                    randomDragWithinRegion(*self.moveRagion,*randomMotion,random.choice(self.RandomWalkTime))
            
            self.stackCount+=1
            print('stackCount: '+str(self.stackCount))
            if self.stackCount == 5:
                self.stackCount = 0
                print('random walk')
                randomMotion = random.choice(self.motions)
                randomDragWithinRegion(*self.moveRagion,*randomMotion,random.choice(self.RandomWalkTime))
            clickWhenSeeRegion(self.path+'shouxia.png',895,629,1133-895,740-629)
            clickWhenSeeRegion(self.path+'queding.png',829,443,1039-829,535-443)    
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

