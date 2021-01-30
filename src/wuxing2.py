import pyautogui
import pydirectinput
import random
import time
import sys
from util import *


pyautogui.FAILSAFE = False
#Sw,Sh = pyautogui.size()

piao = '../pics/5jie.png' #'../pics/piaotuzi.png'#
piaoType = 'liandu' #'name' #
fabao = '../pics/fabaozhu.png'

count = 0
Goal = int(sys.argv[1])

imgs = ['../pics/zhandou.png',
        '../pics/jixu.png',
        piao,
        '../pics/queren.png',
        '../pics/queren2.png',
        '../pics/shihe.png',
        '../pics/cross.png',
        '../pics/kaishixiulian.png',
        '../pics/shuaxin.png',
        '../pics/kaishifuben.png',
        fabao,
        '../pics/qingyi.png',
        '../pics/qingyi2.png']

crossFlag = False
noMana = False
shiheCount = 0
while count < Goal:
    if noMana:
        break
    
    for img in imgs:
        #left conner
        loca = pyautogui.locateOnScreen(img, region = (0,0,1400,800), confidence =.8)
        if loca != None:
            if img == '../pics/zhandou.png':
                print(img+' Has been Found, sleep')
                time.sleep(1)
                
            else:
                print(img+' Has been Found')
                R = random.randint(2, 8)
                C = random.randint(2,7)
                if img == piao:
                    if piaoType == 'name':
                        pyautogui.moveTo(loca[0]+loca[2]//R,loca[1]+loca[3]//C+150,duration = 0.1)
                    elif piaoType == 'liandu':
                        pyautogui.moveTo(loca[0]+loca[2]//R,loca[1]+loca[3]//C-150,duration = 0.1)
                elif img == '../pics/shihe.png':
                    pyautogui.moveTo(loca[0]+loca[2]-R+600,loca[1]+loca[3]-C,duration = 0.1)
                    crossFlag = True
                    shiheCount+=1
                    print('shihe count : '+str(shiheCount))
                    if shiheCount > 1:
                        isTrue = hasImgs(['../pics/meitili.png'])
                        print('check meitili')
                        if isTrue:
                            print('meitili hit')
                            noMana = True
                            
                            
                else:
                    pyautogui.moveTo(loca[0]+loca[2]//R,loca[1]+loca[3]//C,duration = 0.1)
                #pydirectinput.moveTo(loca[0]+loca[2]//R,loca[1]+loca[3]//C)
                if img == '../pics/cross.png':
                    if crossFlag:
                        time.sleep(0.2)
                        pydirectinput.click()
                        print('cross click')
                        crossFlag = False
                elif img == '../pics/queren.png':
                    pydirectinput.click()
                    pyautogui.dragRel(0, -200, duration=0.2)
                    break
                elif img == '../pics/jixu.png':
                    pydirectinput.click()
                    break
                elif img == '../pics/kaishifuben.png':
                    pydirectinput.click()
                    time.sleep(1)
                    count+=1
                    print('Finished times: '+str(count))
                elif img == '../pics/qingyi.png' or img == '../pics/qingyi2.png':
                    pydirectinput.click()
                    time.sleep(0.3)
                    pydirectinput.click()
                    break
                else:
                    pydirectinput.click()
                    
        clickWhenSee('../pics/zhidaole.png')

time.sleep(0.5)
clickWhenSee('../pics/cross.png')   
time.sleep(0.5)             
clickWhenSee('../pics/back.png')
time.sleep(0.5)
clickWhenSee('../pics/backhuodong.png')
time.sleep(0.5)
clickWhenSee('../pics/huodongcross.png')

print('Finished Times: '+str(count)+' Program Closed')
    
