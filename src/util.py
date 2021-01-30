import pyautogui
import pydirectinput
import random
import time
import sys
import os

confidence = 0.85 #0.75

def click(loca):
    if loca != None:
        R = random.randint(2, 8)
        C = random.randint(2,7)
        pyautogui.moveTo(loca[0]+loca[2]//R,loca[1]+loca[3]//C,duration = 0.1)
        pydirectinput.click()
        return True
    else:
        return False
        
def moveTo(loca):
    if loca != None:
        R = random.randint(2, 8)
        C = random.randint(2,7)
        pyautogui.moveTo(loca[0]+loca[2]//R,loca[1]+loca[3]//C,duration = 0.1)
        
        return True
    else:
        return False
    

def clickWhenSee(img):
    tmp = findImgRegion(img,0,0,1400,800)
    if tmp != None:
        click(tmp)
        return True
    else:
        return False

def clickWhenSeeRegion(img,x,y,w,h):
    tmp = findImgRegion(img,x,y,w,h)
    if tmp != None:
        click(tmp)
        return True
    else:
        return False

def clickWhenSeeRegionS(imgs,x,y,w,h):
    idx, tmp = findImgsRegion(imgs,x,y,w,h)
    if tmp != None:
        click(tmp)
        return True
    else:
        return False

def moveToWhenSee(img):
    tmp = findImgRegion(img,0,0,1400,800)
    if tmp != None:
        moveTo(tmp)
        return True
    else:
        return False

def tillFindClick(img):
    tmp = None
    while tmp == None:
        tmp = findImgRegion(img,0,0,1400,800)
        #time.sleep(0.3)
    click(tmp)

def tillFindMoveTo(img):
    tmp = None
    while tmp == None:
        tmp = findImgRegion(img,0,0,1400,800)
        #time.sleep(1)
    moveTo(tmp)
    
def tillFindClickTime(imgs,sec):
    tmp = None
    while tmp == None and sec > 0:
        idx,tmp = findImgs(imgs)
        #time.sleep(0.1)
        sec-=1
    if tmp != None:
        randomDis = random.randint(5, 40)
        clickRelativeImg(tmp,0,60+randomDis)

    
    return tmp
    
def clickRelative(disW,disH):
    R = random.randint(1, 10)
    C = random.randint(1,11)
    pyautogui.moveRel(R+disW,C+disH,duration = 0.1)
    pydirectinput.click()
    
def clickRelativeImg(loca,disW,disH):
    if loca != None:
        R = random.randint(2, 8)
        C = random.randint(2,7)
        pyautogui.moveTo(loca[0]+loca[2]//R+disW,loca[1]+loca[3]//C + disH,duration = 0.1)
        pydirectinput.click()
        return True
    else:
        return False
        
def clickRelativeImgBotRight(loca,disW,disH):
    if loca != None:
        R = random.randint(2, 8)
        C = random.randint(2,7)
        pyautogui.moveTo(loca[0]+loca[2]+disW+R,loca[1]+loca[3] + disH+C,duration = 0.1)
        pydirectinput.click()
        return True
    else:
        return False

def findImgRegion(img,x,y,w,h):
    found = pyautogui.locateOnScreen(img, region = (x,y,w,h), confidence = confidence)
    if found != None:
        print(os.path.split(img)[1].split('.')[0]+' has been found')
    else:
        #print(img+' is not found')
        pass
    return found
    
def clickImgsRel(Imgs,disW,disH):
    idx,loca = findImgs(Imgs)
    isSuccess = clickRelativeImg(loca,disW,disH)
    return isSuccess
    
def clickImgsRelBotRight(Imgs,disW,disH):
    idx,loca = findImgs(Imgs)
    isSuccess = clickRelativeImgBotRight(loca,disW,disH)
    return isSuccess

def findImgs(Imgs):
    found = None
    for i,each in enumerate(Imgs):
        found = pyautogui.locateOnScreen(each, region = (0,0,1400,800), confidence = confidence)
        if found != None:
            print(os.path.split(each)[1].split('.')[0]+' has been found')
            break
        else:
            #print(each+' is not found')
            
            pass
    
    return i,found
    
def findImgsRegion(Imgs,x,y,w,h):
    found = None
    for i,each in enumerate(Imgs):
        found = pyautogui.locateOnScreen(each, region = (x,y,w,h), confidence = confidence)
        if found != None:
            print(os.path.split(each)[1].split('.')[0]+' has been found')
            break
        else:
            #print(each+' is not found')
            if i == len(Imgs) - 1:
                i = i + 1
                print('nothing is not found')
            
    
    return i,found
    
def hasImgs(imgs):
    idx,found = findImgs(imgs)
    if found != None:
        return True
    else:
        return False 
        
def hasImgsRegion(imgs,x,y,w,h):
    idx,found = findImgsRegion(imgs,x,y,w,h)
    if found != None:
        return True
    else:
        return False 
    
def findImgSize(img):
    found = findImgRegion(img,0,0,1400,800)
    if found !=None:
        return found[2],found[3]
    else:
        print('size is not available')
        return None

def viewLeftRight(screenW,screenH,dis):
    R = random.randint(1, 10)
    C = random.randint(1,11)
    pyautogui.moveTo(screenW//2-R,screenH//2+C,duration = 0.1)
    pyautogui.dragRel(dis, 0, duration=0.2)

def viewUpDown(screenW,screenH,dis):
    R = random.randint(1, 55)
    C = random.randint(1,44)
    pyautogui.moveTo(screenW//2-R,screenH//2-C,duration = 0.1)
    pyautogui.dragRel(0, dis, duration=0.15)
    
def timedExecute(func,sec,arguments):
    while sec>0:
        func(*arguments)
        #time.sleep(1)
        sec-=1
        
def randomClickWithinRegion(x1,x2,y1,y2):
    x = random.randint(x1, x2)
    y = random.randint(y1,y2)
    pydirectinput.click(x,y)
    
def randomDragUpWithinRegion(x1,x2,y1,y2,dis):
    x = random.randint(x1, x2)
    y = random.randint(y1,y2)
    pyautogui.moveTo(x,y,duration = 0.1)
    pyautogui.dragRel(0, dis, duration=0.2)

def randomDragWithinRegion(x1,x2,y1,y2,disX,disY,holdTime):
    x = random.randint(x1, x2)
    y = random.randint(y1,y2)
    pyautogui.moveTo(x,y)
    pyautogui.dragRel(disX, disY, duration=holdTime)

def randomDragRightWithinRegion(x1,x2,y1,y2,dis):
    x = random.randint(x1, x2)
    y = random.randint(y1,y2)
    pyautogui.moveTo(x,y,duration = 0.1)
    pyautogui.dragRel(dis, 0, duration=0.2)