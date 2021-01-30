import pyautogui
import pydirectinput
import random
import time
import sys
import os
import argparse
from util import *
import pygetwindow as gw

def clk11():
    randomClickWithinRegion(384,411,567,597)
    time.sleep(0)
    
def clk12():
    randomClickWithinRegion(486,506,575,600)
    time.sleep(0)
        
def clk13():
    randomClickWithinRegion(575,598,575,600)
    time.sleep(0)
        
def clk21():
    randomClickWithinRegion(688,718,575,600)
    time.sleep(0)
        
def clk22():
    randomClickWithinRegion(785,816,575,600)
    time.sleep(0)
        
def clk23():
    randomClickWithinRegion(881,908,575,600)
    time.sleep(0)
    
def fish1():
    randomClickWithinRegion(284,324,199,242)
    time.sleep(0)
    
def fish2():
    randomClickWithinRegion(418,459,198,245)
    time.sleep(0)
    
def fish3():
    randomClickWithinRegion(555,603,202,248)
    time.sleep(0)
    
def fish4():
    randomClickWithinRegion(691,732,201,249)
    time.sleep(0)
        
def fish5():
    randomClickWithinRegion(824,866,194,246)
    time.sleep(0)
    
def fish6():
    randomClickWithinRegion(964,1008,196,246)
    time.sleep(0)
    
def fish7():
    randomClickWithinRegion(1097,1144,199,246)
    time.sleep(0)
    
def yuce():
    randomClickWithinRegion(1051,1146,567,591)
    time.sleep(0)

def queren():
    clickWhenSee('../caiyu/caiyu.png')
    time.sleep(0.35)    
    
def suiji():
    randomClickWithinRegion(537,628,669,688)
    time.sleep(0)
    
def clkFish(each):
    if each == '1':
        fish1()
    if each == '2':
        fish2()
    if each == '3':
        fish3()
    if each == '4':
        fish4()
    if each == '5':
        fish5()
    if each == '6':
        fish6()
    if each == '7':
        fish7()     

pyautogui.FAILSAFE = False
window = gw.getWindowsAt(650,350)[0]
print(window.size)
window.moveTo(0,0)
window.resizeTo(1350, 790)
#window.resizeTo(2560, 790)
print(window.size)

#python caiyu.py 2671 2345 1 

In1 = sys.argv[1]
stringIn1 = []
for char in In1:
    stringIn1.append(char)
print('original candidates:')
print(stringIn1)

In2 = sys.argv[2]
stringIn2 = []
for char in In2:
    stringIn2.append(char)
print(stringIn2)

qian = int(sys.argv[3])

if In1 == In2 == '0':
    while qian>0:
        qian-=1
        suiji()
        yuce()
        queren()
else:
    while qian>0:
        print(str(qian)+'qian remained, good luck')
        qian-=1
        random.shuffle(stringIn1)
        print('shuffled candidates:')
        print(stringIn1)
        random.shuffle(stringIn2)
        print(stringIn2)
        round1 = stringIn1[:3]
        round2 = stringIn2[:3]
        
        for i,each in enumerate(round1):
            if i == 0:
                clk11()
                clkFish(each)
            if i == 1:
                clk12()
                clkFish(each)
            if i == 2:
                clk13()
                clkFish(each)
                
        for i,each in enumerate(round2):
            if i == 0:
                clk21()
                clkFish(each)
            if i == 1:
                clk22()
                clkFish(each)
            if i == 2:
                clk23()
                clkFish(each)  

        yuce()
        queren()
            
            
            















