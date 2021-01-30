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

w,h = pyautogui.size()
window = gw.getWindowsAt(650,350)[0]
print(window.size)
window.moveTo(0,0)
window.resizeTo(w, h//2)
