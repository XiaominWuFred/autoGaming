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

def general(w,h):
    if clickWhenSeeRegionS(['../simple/fabaozhu.png',
                     '../simple/fabao2.png'],0,0,w,h):
        pass
    
    if hasImgsRegion(['../simple/zhandou.png','../simple/zhandou2.png'],0,0,w,h):
        print('sleep...zzz')
        time.sleep(1)
        return 

    clickWhenSeeRegion('../simple/shouyao.png',0,0,w,h)
    if clickWhenSeeRegion('../simple/jixu.png',0,0,w,h):
        tc = 10
        while not hasImgsRegion(['../simple/danren.png','../simple/yaopo.png','../simple/kaishixiulian.png','../simple/tiaozhan.png'],0,0,w,h) and tc > 0:
            clickWhenSeeRegion('../simple/jixu.png',0,0,w,h)
            print('jixu count down: '+str(tc))
            tc-=1
    
    if clickWhenSeeRegionS(['../simple/qingyi.png',
                     '../simple/qingyi4.png',
                     '../simple/qingyi2.png',
                     '../simple/qingyi3.png'],0,0,w,h):
        time.sleep(0.1)
        pydirectinput.click()

    clickWhenSeeRegion('../simple/zhidaole.png',0,0,w,h)
    clickWhenSeeRegion('../simple/queren2.png',0,0,w,h)
    clickWhenSeeRegion('../simple/qianwangtiaozhan.png',0,0,w,h)
    clickWhenSeeRegion('../simple/kaishizhandou.png',0,0,w,h)
    
    if hasImgsRegion(['../simple/zhuzhan.png'],0,0,w,h):
        pass
    else:
        time.sleep(0.2)
        if hasImgsRegion(['../simple/zhuzhan.png'],0,0,w,h):
            pass
        else:
            time.sleep(0.2)
            clickWhenSeeRegion('../simple/querenchuzhan.png',0,0,w,h)
    
    time.sleep(0.5)
    
    

                


if __name__ == '__main__':
    w,h = pyautogui.size()
    window = gw.getWindowsAt(650,350)[0]
    print(window.size)
    window.moveTo(0,0)
    window.resizeTo(w, h//2)
    #window.resizeTo(w//2, h)

    while True:
        clickWhenSeeRegion('../simple/queding.png',0,0,w,h)
        general(w,h//2)