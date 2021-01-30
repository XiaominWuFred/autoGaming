import pyautogui
import pydirectinput
import random
import time
import sys

pyautogui.FAILSAFE = False
#Sw,Sh = pyautogui.size()

piao = '../pics/piao4.png' #'piaotuzi.png'
piaoType = 'name' #'name' 
fabao = '../pics/fabaozhu.png'

count = 0
Goal = int(sys.argv[1])
     
imgs = ['../pics/zhandou.png',
        '../pics/jixu.png',
        '../pics/shouyao.png',
        piao,
        '../pics/queding.png',
        '../pics/tiaozhan.png',
        '../pics/shuaxin.png',
        '../pics/kaishifuben.png',
        fabao,
        '../pics/qingyi.png',
        '../pics/qingyi2.png']


while count < Goal:
    for img in imgs:
        #left conner
        loca = pyautogui.locateOnScreen(img, region = (0,0,1400,800), confidence =.85)
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
                    elif piaoType == 'pic':
                        pyautogui.moveTo(loca[0]+loca[2]//R,loca[1]+loca[3]//C,duration = 0.1)
                else:
                    pyautogui.moveTo(loca[0]+loca[2]//R,loca[1]+loca[3]//C,duration = 0.1)
                #pydirectinput.moveTo(loca[0]+loca[2]//R,loca[1]+loca[3]//C)


                if img == '../pics/jixu.png':
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
                    

print('Finished Times: '+str(Goal)+' Program Closed')