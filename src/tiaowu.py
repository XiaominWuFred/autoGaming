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

path = 'jiayuan'

if __name__ == '__main__':
    window = gw.getWindowsAt(650,350)[0]
    print(window.size)
    window.moveTo(0,0)
    window.resizeTo(1350, 790)
    
    
    while True:
        
        if hasImgs(['../'+path+'/tuichu.png','../tiaowu/yan.png']):
            randomClickWithinRegion(1282,1307,253,272)
            time.sleep(0.5)
            if not hasImgs(['../'+path+'/tuichu.png']):
                time.sleep(0.3)
                randomClickWithinRegion(1179,1258,127,174)
                time.sleep(0.3)
                randomClickWithinRegion(1089,1132,105,125)
                time.sleep(0.3)
                dis = random.randint(200, 230)
                randomDragUpWithinRegion(841,1158,353,554,-dis) 
                time.sleep(1)
                randomDragUpWithinRegion(841,1158,353,554,-dis)
                time.sleep(1)
                tc = 5
                while not clickWhenSeeRegion('../'+path+'/tiaowu.png',729,119,1275-729,735-119) and tc > 0:
                    tc =- 1
                    print('finding : '+str(tc))
                    time.sleep(0.2)
                    
                time.sleep(2)
                randomClickWithinRegion(634,717,274,372)
                time.sleep(1)
                randomClickWithinRegion(654,687,585,616)
            
        
        clickWhenSeeRegionS(['../tiaowu/queding.png','../tiaowu/jixu.png','../tiaowu/cross.png','../tiaowu/kanban.png','../tiaowu/jiandan.png','../tiaowu/xianchan.png','../tiaowu/run.png'],33,48,1332-33,775-48)
        
        while hasImgsRegion(['../tiaowu/zanting.png'],20,33,207-20,109-33):
            tc =- 1
            clickWhenSeeRegionS(['../tiaowu/p1.png',
                                 '../tiaowu/p2.png',
                                 '../tiaowu/p3.png',
                                 '../tiaowu/p4.png',
                                 '../tiaowu/p5.png'],33,48,1332-33,775-48)
            if hasImgsRegion(['../'+path+'/tuichu.png'],x =1152 ,y=668,w = 1322-1152,h = 773-668 ):
                break
                