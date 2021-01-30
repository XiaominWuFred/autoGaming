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

if __name__ == '__main__':
    window = gw.getWindowsAt(650,350)[0]
    print(window.size)
    window.moveTo(0,0)
    window.resizeTo(1350, 790)

    while True:
        randomClickWithinRegion(925,935,260,270)
        time.sleep(0.3)
        randomClickWithinRegion(1035,1145,680,690)
        time.sleep(0.3)
            
