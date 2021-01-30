import pyautogui
import pydirectinput
import random
import time
import sys

pyautogui.FAILSAFE = False
#Sw,Sh = pyautogui.size()

piao = '../pics/5jie.png'#'../pics/piaotuzi.png'
piaoType =  'liandu'#'name'
fabao = '../pics/fabaozhu.png'

count = 0
Goal = int(sys.argv[1])
     
imgs = ['../pics/zhandou.png',
        '../pics/jixu.png',
        '../pics/shouyao.png',
        piao,
        '../pics/queren.png',
        '../pics/queren2.png',
        '../pics/shihe.png',
        '../pics/cross.png',
        '../pics/danren.png',
        '../pics/shuaxin.png',
        '../pics/kaishifuben.png',
        fabao,
        '../pics/qingyi.png',
        '../pics/qingyi2.png']

crossFlag = False

while count < Goal:
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
                else:
                    pyautogui.moveTo(loca[0]+loca[2]//R,loca[1]+loca[3]//C,duration = 0.1)
                #pydirectinput.moveTo(loca[0]+loca[2]//R,loca[1]+loca[3]//C)
                if img == 'cross.png':
                    if crossFlag:
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
                elif img == '../pics/qingyi.png' or img == '../pics/qingyi2.png':
                    pydirectinput.click()
                    time.sleep(0.3)
                    pydirectinput.click()
                    break
                elif img == '../pics/shouyao.png':
                    count+=1
                    print('finished times: '+str(count))
                    pydirectinput.click()
                    time.sleep(1)
                    break
                else:
                    pydirectinput.click()
                    
                #T = random.randint(10,20)
                #time.sleep(T/1000)
print('Finished Times: '+str(Goal)+' Program Closed')
    