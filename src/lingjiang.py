import pyautogui
import pydirectinput
import random
import time
import sys
import os
import argparse
from util import *
import pygetwindow as gw

window = gw.getWindowsAt(650,350)[0]
print(window.size)
window.moveTo(0,0)
window.resizeTo(1350, 790)

while True:
    clickWhenSee('../general/lingqu.png')
    clickWhenSee('../general/lingqu2.png')
    clickWhenSee('../general/shouxia.png')
    clickWhenSee('../general/wancheng.png')
    #time.sleep(0.5)