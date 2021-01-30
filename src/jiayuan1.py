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


window = gw.getWindowsAt(650,350)[0]
print(window.size)
window.moveTo(0,0)
window.resizeTo(1350, 790)
#window.resizeTo(2560, 790)

print(window.size)
time.sleep(2)

parser = argparse.ArgumentParser()
parser.add_argument('--wuxing',action='store_true', default=False,help='go wuxing.')
parser.add_argument('--anying',action='store_true', default=False,help='go anying.')
parser.add_argument('--songli',action='store_true', default=False,help='do songli.')
parser.add_argument('--pengren',action='store_true', default=False,help='do pengren.')
args = parser.parse_args()

pyautogui.FAILSAFE = False
#near 1349 789
#(jing zhi) or (gao qing) , gao zhen ping
screenSize = [1400,800]
path = 'jiayuan'
#Sw,Sh = pyautogui.size()


class jiayuan():
    def __init__(self):
        self.zhongzhiing = False
        self.replaceCount = 0
        self.replacePoss = [[354,387,253,285],
                            [454,485,277,307],
                            #[1053,1084,559,588],
                            #[456,477,609,634],
                            #[325,347,570,599],
                            #[354,387,253,285],
                            #[949,987,529,561],
                            ] 
        
        self.gifts = ['../'+path+'/muma.png',
                      '../'+path+'/jiu1.png',
                      '../'+path+'/jiu2.png',
                      '../'+path+'/jiu3.png',
                      '../'+path+'/jiu4.png',
                      '../'+path+'/shi1.png',
                      '../'+path+'/shi2.png',
                      '../'+path+'/shi3.png',
                      '../'+path+'/shi4.png',
                      '../'+path+'/shi5.png',
                      
                      
                      '../'+path+'/wan1.png',
                      
                      
                      '../'+path+'/xiang1.png',
                      '../'+path+'/xiang2.png',
                      
                      '../'+path+'/bao1.png',
                      '../'+path+'/bao2.png',
                      '../'+path+'/bao3.png',
                      '../'+path+'/bao4.png',
                      '../'+path+'/bao5.png',
                      
                      '../'+path+'/zhuang1.png',
                      '../'+path+'/zhuang2.png',
                      
                      '../'+path+'/wuqi1.png',
                      '../'+path+'/wuqi2.png',
                      
                      '../'+path+'/guihuo.png',
                      
                      '../'+path+'/shiwu1.png',
                      '../'+path+'/shiwu2.png',
                      '../'+path+'/shiwu3.png',
                      '../'+path+'/shiwu4.png',
                      '../'+path+'/shiwu5.png',
                      
                      '../'+path+'/yanzhi.png',
                      '../'+path+'/qingshui.png',
                      '../'+path+'/gudong.png',
                      
                      '../'+path+'/mianju.png',
                      '../'+path+'/zhuqingting.png'
                      ]

    def enter(self,imgs):
        loca = findImgRegion(imgs[0],0,0,1400,800)
        isDone = click(loca)
        if isDone:
            tillFindClick(imgs[1])  
            tillFindClick(imgs[2])  
            tillFindClick(imgs[3])  
    
    def findYao2(self,imgs):
        isTrue = hasImgs(['../'+path+'/tuichu.png'])
        if isTrue:
            time.sleep(0.5)
            clickWhenSee(imgs[0])
            time.sleep(0.5)
            clickWhenSee(imgs[1])
            #pack = findImgSize(imgs[1])
            isTrue = True
            while isTrue:
                isTrue = hasImgsRegion(['../'+path+'/zhongzhizhong.png',
                                        '../'+path+'/zhongdi1.png',
                                        '../'+path+'/zhongdi2.png',
                                        '../'+path+'/zhongdi3.png',
                                        '../'+path+'/zaotai1.png',
                                        '../'+path+'/zaotai2.png'], x=955,y=258,w=290,h=126)#'../'+path+'/zaotai1.png', '../'+path+'/zaotai2.png'],
                if isTrue:
                    dis = random.randint(70,85)
                    viewUpDown(screenSize[0],screenSize[1],-dis)
                    time.sleep(0.2)
                
            #moveToWhenSee(imgs[1])    
            #if pack != None:
            #clickRelative(0,3.5*pack[1])
            randomClickWithinRegion(273,400,315,320)
            time.sleep(0.2)
            clickWhenSee(imgs[2])
            clickWhenSee('../'+path+'/quedingqingyi.png')
            clickWhenSee('../'+path+'/qingyiqueding.png')
            
        #viewLeftRight(screenSize[0],screenSize[1],-100)
        #timedExecute(viewLeftRight,5,[screenSize[0],screenSize[1],-100])
        time.sleep(0.1)
        count = 5
        isDone = False
        while count > 0 and not isDone:
            randomClickWithinRegion(1020,1060,542,586)
            time.sleep(0.5)
            count -=1
            if hasImgsRegion(['../'+path+'/tuichu.png'],x =1152 ,y=668,w = 1322-1152,h = 773-668 ):
                time.sleep(1.5)
            else:
                if hasImgsRegion(['../'+path+'/songli.png'],x = 831,y=313,w = 1184-831,h = 430-313 ):
                    time.sleep(0.5)
                    randomClickWithinRegion(923,1127,338,390)
                    time.sleep(0.5)
                    #songli
                    random.shuffle(self.gifts)
                    idx,found = findImgsRegion(self.gifts,x=888,y=206,w=1297-888,h=625-206)
                    click(found)
                    randomClickWithinRegion(1082,1150,665,685)  
                    time.sleep(0.5)
                    randomClickWithinRegion(44,134,42,71)
                    time.sleep(0.5)
                    randomClickWithinRegion(44,134,42,71)
                    time.sleep(0.5)
                else:
                    times = 30
                    while times > 0:
                        print('clicking '+str(times))

                        randomClickWithinRegion(934,964,274,291)
                        times -= 1
                        
                        if hasImgs(['../'+path+'/daojishi.png']):
                            isDone = True
                            break
                        
                        hasimg = hasImgs(['../'+path+'/huida.png',
                                          '../'+path+'/shouxia.png',
                                          '../'+path+'/shouxia2.png',
                                          '../'+path+'/tuichu.png',
                                          '../'+path+'/kanban.png'])
                        if hasimg:
                            time.sleep(2)
                            if hasImgs(['../'+path+'/huida.png',
                                          '../'+path+'/shouxia.png',
                                          '../'+path+'/shouxia2.png',
                                          '../'+path+'/tuichu.png',
                                          '../'+path+'/kanban.png']):
                                isDone = True
                                break
                        
                        clickWhenSee('../'+path+'/huaquan.png')
                        time.sleep(0.3)
                        clickWhenSee('../'+path+'/huaquanqueding.png')
                        clickWhenSee(imgs[6])
                        clickWhenSee(imgs[5])
                        clickWhenSee('../'+path+'/touxiang.png')
                        clickWhenSee('../'+path+'/touxiang2.png')
                        
                        if clickWhenSee('../'+path+'/generalBack.png'):
                            time.sleep(0.1)
                            clickWhenSee('../'+path+'/generalBack.png')
                            time.sleep(0.1)
                            clickWhenSee('../'+path+'/generalBack.png')
                            time.sleep(0.1)
                            clickWhenSee('../'+path+'/generalBack.png')
                            time.sleep(0.1)
                        clickWhenSee('../'+path+'/queding.png')
                        clickWhenSee('../'+path+'/mapcross.png')
                        clickWhenSee('../'+path+'/shuzhaiback.png')
                        clickWhenSee('../'+path+'/qingyiqueding.png')
                        clickWhenSee('../'+path+'/quedingqingyi.png')
                        
                            
                    print('interact done') 
        if count == 0:
            randomDis = random.randint(200, 400)
            timedExecute(viewLeftRight,1,[screenSize[0],screenSize[1],-100-randomDis])
            dis = random.randint(100,200)
            randomDragUpWithinRegion(164,201,600,641,-dis)
            dis = random.randint(100,200)
            randomDragUpWithinRegion(164,201,600,641,-dis)
        
        return count
    
    def findYao(self,imgs):
        isTrue = hasImgs(['../'+path+'/tuichu.png'])
        if isTrue:
            time.sleep(0.5)
            clickWhenSee(imgs[0])
            time.sleep(0.5)
            clickWhenSee(imgs[1])
            #pack = findImgSize(imgs[1])
            isTrue = True
            while isTrue:
                isTrue = hasImgsRegion(['../'+path+'/zhongdi1.png',
                                        '../'+path+'/zhongdi2.png',
                                        '../'+path+'/zhongdi3.png',
                                        '../'+path+'/zaotai1.png',
                                        '../'+path+'/zaotai2.png'],x=955,y=258,w=290,h=126)
                if isTrue:
                    dis = random.randint(70,85)
                    viewUpDown(screenSize[0],screenSize[1],-dis)
                    time.sleep(0.2)
                
            #moveToWhenSee(imgs[1])    
            #if pack != None:
            #clickRelative(0,3.5*pack[1])
            randomClickWithinRegion(273,480,315,320)
            time.sleep(0.2)
            clickWhenSee(imgs[2])
        #viewLeftRight(screenSize[0],screenSize[1],-100)
        #timedExecute(viewLeftRight,5,[screenSize[0],screenSize[1],-100])
        time.sleep(0.1)
        isDone = None
        count = 5
        while isDone == None and count > 0:
            count -= 1
            clickWhenSee(imgs[5])
            clickWhenSee(imgs[6])
            clickWhenSee('../'+path+'/shouxia.png')
            clickWhenSee('../'+path+'/shouxiapengren.png')
            clickWhenSee('../'+path+'/mapcross.png')
            clickWhenSee('../'+path+'/ccross.png')
            clickWhenSee('../'+path+'/backhuodong.png')
            if clickWhenSee('../'+path+'/generalBack.png'):
                time.sleep(0.2)
                clickWhenSee('../'+path+'/huaquanqueding.png')
            
            print('finding tanhao times '+str(count))
            pyautogui.scroll(-500)
            isDone = tillFindClickTime([imgs[3],imgs[4],'../'+path+'/tanhao3.png','../'+path+'/tanhao4.png'],1)
            time.sleep(2)
            notThere = findImgRegion('../'+path+'/tuichu.png',0,0,1400,800)
            if notThere != None:
                isDone = None
            
            if isDone != None:
                times = 30
                while times > 0:
                    print('clicking '+str(times))
                    clickWhenSee('../'+path+'/huaquan.png')
                    time.sleep(0.3)
                    clickWhenSee('../'+path+'/huaquanqueding.png')
                    clickWhenSee('../'+path+'/touxiang.png')
                    if clickWhenSee('../'+path+'/generalBack.png'):
                        clickWhenSee('../'+path+'/generalBack.png')
                        clickWhenSee('../'+path+'/generalBack.png')
                        clickWhenSee('../'+path+'/generalBack.png')
                    clickWhenSee(imgs[6])
                    clickWhenSee(imgs[5])
                    clickWhenSee('../'+path+'/mapcross.png')
                    clickWhenSee('../'+path+'/shuzhaiback.png')
                    randomClickWithinRegion(934,964,274,291)
                    times -= 1
                    
                    if hasImgs(['../'+path+'/daojishi.png']):
                        break
                    
                    hasimg = hasImgs(['../'+path+'/huida.png',
                                      '../'+path+'/shouxia.png',
                                      '../'+path+'/shouxia2.png',
                                      '../'+path+'/tuichu.png',
                                      '../'+path+'/kanban.png'])
                    if hasimg:
                        time.sleep(2)
                        if hasImgs(['../'+path+'/huida.png',
                                      '../'+path+'/shouxia.png',
                                      '../'+path+'/shouxia2.png',
                                      '../'+path+'/tuichu.png',
                                      '../'+path+'/kanban.png']):
                            break
                        
                print('interact done')
            else:
                randomDis = random.randint(200, 400)
                timedExecute(viewLeftRight,1,[screenSize[0],screenSize[1],-100-randomDis])
                
        return count
                
    def Act(self,imgs):
        finishOne = False
        print('doing Act')
        count = 20
        while not finishOne and count > 0:
            hasimg = hasImgs(['../'+path+'/tuichu.png'])
            if hasimg:
                break
            print('doing Act While')
            idx,found = findImgs(imgs)
            count -= 1
            if imgs[idx] == '../'+path+'/shouxia.png':
                finishOne = True
                click(found)
            elif imgs[idx] == '../'+path+'/lingqujiangli.png':
                finishOne = True
                click(found)
            elif imgs[idx] == '../'+path+'/huaquan.png':
                clickWhenSee('../'+path+'/huaquanqueding.png')
            elif imgs[idx] == '../'+path+'/huidaqueren.png':
                randomClickWithinRegion(616,667,281,341)
                time.sleep(0.5)
                clickWhenSee('../'+path+'/huidaqueren2.png')
                time.sleep(0.5)
                clickWhenSee('../'+path+'/lingqujiangli.png')
                randomClickWithinRegion(1049,1114,432,506)
                time.sleep(0.5)
                clickWhenSee('../'+path+'/huidaqueren2.png')
                time.sleep(0.5)
                clickWhenSee('../'+path+'/lingqujiangli.png')
                clickWhenSee('../'+path+'/xiacinuli.png')
            elif imgs[idx]=='../'+path+'/daojishi.png':
                print('wait for zhuomicang')
                time.sleep(90)
            else:
                print('Shouxia not found, continue try times: '+str(count))
                click(found)
                
            if count == 0:
                notThere = findImgRegion('../'+path+'/tuichu.png',0,0,1400,800)
                if notThere == None:
                    count +=1
              
                
        return finishOne
                
            
    def zhongzhi(self):
        #cli = clickWhenSee('../'+path+'/qianwangzhongzhi.png')
        randomClickWithinRegion(1034,1178,690,728)
        time.sleep(1)
        while hasImgs(['../'+path+'/chengshou.png','../'+path+'/chengshou2.png','../'+path+'/tuichu.png']):
            print('walking....')
            time.sleep(1.5)
        
        for i in range(3):
            tc = 3
            while not clickWhenSee('../'+path+'/shouge.png') and tc > 0:
                print('waiting shouge....'+str(tc))
                time.sleep(0.25)
                tc-=1
            time.sleep(0.5)
            clickWhenSeeRegion('../'+path+'/zhongzhiqueding.png',556,634,797-556,725-634)
            
            tc = 3
            while not clickWhenSee('../'+path+'/shouxiazuowu.png') and tc > 0:
                print('waiting shouxia....'+str(tc))
                time.sleep(0.25)
                tc-=1
            time.sleep(0.5)    
            clickWhenSeeRegion('../'+path+'/zhongzhiqueding.png',556,634,797-556,725-634)

            '''
            tc = 3    
            while not hasImgs(['../'+path+'/bozhong.png']) and tc > 0:
                print('waiting bozhong....'+str(tc))
                time.sleep(0.25)
                tc-=1
            
            for i in range(8):
                if hasImgs(['../'+path+'/chanchuzuowu.png']):
                    break
                clickWhenSee('../'+path+'/bozhong.png')
                print('bozhong ing ......'+str(i))
                time.sleep(0.5)
            '''
            
            randomClickWithinRegion(813,827,397,419)
        
        tc = 3
        while not clickWhenSee('../'+path+'/tuichuzhongzhi.png') and tc > 0:
            print('waiting tuichu....'+str(tc))
            time.sleep(0.5)
            tc-=1

    def pengren(self):
        randomClickWithinRegion(1282,1307,253,272)
        time.sleep(0.5)
        if not hasImgs(['../'+path+'/tuichu.png']):
            time.sleep(0.3)
            randomClickWithinRegion(1179,1258,127,174)
            time.sleep(0.3)
            randomClickWithinRegion(1089,1132,105,125)
            time.sleep(0.3)
            dis = random.randint(100, 200)
            randomDragUpWithinRegion(841,1158,353,554,-dis) 
            
            time.sleep(1)
            tc = 10
            while not clickWhenSeeRegion('../'+path+'/pengrenicon.png',729,119,1275-729,735-119) and tc > 0:
                tc =- 1
                print('finding pengren: '+str(tc))
                time.sleep(0.2)

            time.sleep(1)
            randomClickWithinRegion(1056,1159,694,718)
            time.sleep(1.5)
            while hasImgs(['../'+path+'/tuichu.png']):
                print('walking....')
                time.sleep(0.5) 

            if clickWhenSeeRegion('../'+path+'/pengrenshouqu.png',1104,682,1315-1104,769-682):
                tc = 3
                while not clickWhenSeeRegion('../'+path+'/shouxiapengren.png',556,632,791-556,723-632) and tc > 0:
                    print('waiting shouxia pengren....'+str(tc))
                    time.sleep(0.5)
                    tc-=1
                    
                tc = 3
                while not clickWhenSeeRegion('../'+path+'/shouxiapengren.png',556,632,791-556,723-632) and tc > 0:
                    print('waiting shouxia pengren....'+str(tc))
                    time.sleep(0.5)
                    tc-=1

            time.sleep(0.5)
            hasZhizuo = hasImgs(['../'+path+'/zhizuo.png'])
            bb = random.choice([0,1])
            if not hasZhizuo:
                if bb == 0:
                    cliJia = clickWhenSeeRegion('../'+path+'/jiapengren.png',43,490,570,205)
                elif bb == 1:
                    cliJia = clickWhenSeeRegion('../'+path+'/jiapengren.png',726,507,595,175)

            time.sleep(0.5)
            hasjz = hasImgs(['../'+path+'/hasjiaozi.png'])
            
            cli = clickWhenSee('../'+path+'/zhizuo.png')
            #isfinished = hasImgs(['../'+path+'/chaochushangxian.png'])
            time.sleep(0.5)
            isquxiao = hasImgs(['../'+path+'/yiyuanquxiao.png'])
            if isquxiao:
                randomClickWithinRegion(901,974,481,512)
                
                #songli 
                random.shuffle(self.gifts)
                idx,found = findImgsRegion(self.gifts,x=841,y=239,w=1262-841,h=628-239)
                click(found)
                randomClickWithinRegion(1100,1175,665,692)
                time.sleep(0.5)
                randomClickWithinRegion(44,134,42,71)
            else:
                randomClickWithinRegion(668,795,58,90)
                time.sleep(0.5)
                randomClickWithinRegion(668,795,58,90)
                time.sleep(0.5)
                randomClickWithinRegion(668,795,58,90)

                    
            time.sleep(0.5)
            cli = clickWhenSee('../'+path+'/pengren.png')
            time.sleep(0.5)
            cli = clickWhenSee('../'+path+'/pengren.png')
            time.sleep(0.5)
            cli = clickWhenSee('../'+path+'/pengren.png')

    def gozhongzhi(self):
        randomClickWithinRegion(1282,1307,253,272)
        time.sleep(0.5)
        if not hasImgs(['../'+path+'/tuichu.png']):
            time.sleep(0.3)
            randomClickWithinRegion(1179,1258,127,174)
            time.sleep(0.3)
            randomClickWithinRegion(1089,1132,105,125)
            time.sleep(0.3)
            dis = random.randint(100, 200)
            randomDragUpWithinRegion(841,1158,353,554,-dis) 
            
            time.sleep(1)
            tc = 10
            while not clickWhenSeeRegion('../'+path+'/zhongzhi.png',729,119,1275-729,735-119) and tc > 0:
                tc =- 1
                print('finding zhongzhi: '+str(tc))
                time.sleep(0.2)

            time.sleep(1)
            randomClickWithinRegion(1056,1159,694,718)
            time.sleep(1.5)
            while hasImgs(['../'+path+'/tuichu.png']):
                print('walking....')
                time.sleep(0.5) 

            #entered
            for i in range(3):        
                tc = 3    
                while not hasImgs(['../'+path+'/bozhong.png']) and tc > 0:
                    print('waiting bozhong....'+str(tc))
                    time.sleep(0.25)
                    tc-=1
                
                for i in range(8):
                    if hasImgs(['../'+path+'/chanchuzuowu.png']):
                        self.zhongzhiing = True
                        break
                    #clickWhenSee('../'+path+'/bozhong.png')
                    randomClickWithinRegion(1052,1130,647,681)
                    print('bozhong ing ......'+str(i))
                    time.sleep(0.5)
                
                randomClickWithinRegion(813,827,397,419)
            
            tc = 3
            while not clickWhenSee('../'+path+'/tuichuzhongzhi.png') and tc > 0:
                print('waiting tuichu....'+str(tc))
                time.sleep(0.5)
                tc-=1


    def shoupengren(self):
        cli = clickWhenSee('../'+path+'/pengrenwancheng.png')

        if cli:
            time.sleep(0.5)
            clickWhenSee('../'+path+'/qianwangpengren.png')
            while hasImgs(['../'+path+'/pengrenwancheng.png']):
                print('walking....')
                time.sleep(0.5)
                   
            tc = 10
            while not clickWhenSee('../'+path+'/pengrenshouqu.png') and tc > 0:
                print('waiting shoupengren....'+str(tc))
                time.sleep(0.5)
                tc-=1
                
            tc = 10
            while not clickWhenSee('../'+path+'/shouxiapengren.png') and tc > 0:
                print('waiting shouxia pengren....'+str(tc))
                time.sleep(0.5)
                tc-=1
                
            tc = 10
            while not clickWhenSee('../'+path+'/shouxiapengren.png') and tc > 0:
                print('waiting shouxia pengren....'+str(tc))
                time.sleep(0.5)
                tc-=1
                
            tc = 10
            while not clickWhenSee('../'+path+'/pengren.png') and tc > 0:
                print('waiting pengren....'+str(tc))
                time.sleep(0.5)
                tc-=1
                
        return cli
                

    #wuxing: goFuben('../'+path+'/wuxingxiulian.png','python fuben.py --goal 10 --wuxing')      
    #huanjing, huodong add based on needs
    def goFuben(self,fuben,cmd):
        tc = 10
        while not clickWhenSee('../'+path+'/tiaomu.png') and tc > 0:
            randomDis = random.randint(100, 200)
            timedExecute(viewLeftRight,1,[screenSize[0],screenSize[1],-100-randomDis])
            time.sleep(1)
            tc -=1
            print('finding tiaomu wuxing count: '+str(tc))
        
        if tc > 0: 
            time.sleep(0.5)
            cli = clickWhenSee('../'+path+'/xingnang.png')
            eatCount = 10
            while hasImgs(['../'+path+'/qingtuan.png','../'+path+'/lvjiaozi.png','../'+path+'/qingtuan2.png']) and eatCount>0:
                clickWhenSee('../'+path+'/qingtuan.png')
                time.sleep(0.5)
                cli = clickWhenSee('../'+path+'/shiyong.png')
                clickWhenSee('../'+path+'/qingtuan2.png')
                time.sleep(0.5)
                cli = clickWhenSee('../'+path+'/shiyong.png')
                clickWhenSee('../'+path+'/lvjiaozi.png')
                time.sleep(0.5)
                cli = clickWhenSee('../'+path+'/shiyong2.png')
                eatCount-=1
                print('eatCount : '+str(eatCount))
                
            time.sleep(0.5)
            cli = clickWhenSee('../'+path+'/xingnangback.png')
            time.sleep(0.5)
            cli = clickWhenSee('../'+path+'/huodong.png')
            time.sleep(0.5)
            tc = 10
            while not hasImgs([fuben]) and tc>0:
                dis = random.randint(100, 150)
                randomDragUpWithinRegion(1055,1101,392,471,-dis)
                tc -= 1
                print('tc count: '+str(tc))
            if tc != 0:
                time.sleep(0.5)
                while not clickWhenSee(fuben):
                    time.sleep(0.3)
                
                time.sleep(1)
                for i in range(4):
                    dis = random.randint(100, 200)
                    randomDragUpWithinRegion(841,1158,353,554,-dis)
                    time.sleep(0.4)
                randomClickWithinRegion(851,1184,650,736)
                #os.system('python wuxing2.py 100')
                os.system(cmd)
                print('Wuxing finished')
            else:
                clickWhenSee('../'+path+'/generalBack.png')
                time.sleep(0.5)
                clickWhenSee('../'+path+'/huodongcross.png')
            
    def dacan(self):
        cli = clickWhenSee('../'+path+'/dacanjieshu.png')

        if cli:
            time.sleep(0.5)
            clickWhenSee('../'+path+'/dacanqueding.png')
            
            while hasImgs(['../'+path+'/tuichu.png']):
                print('walking....')
                time.sleep(0.5)  
            
            time.sleep(0.5)
            clickWhenSee('../'+path+'/dacanlingqujiangli.png')
            time.sleep(0.5)
            clickWhenSee('../'+path+'/fangzhidacan.png')
            time.sleep(0.5)
            clickWhenSee('../'+path+'/zhuli300.png')
            time.sleep(0.5)
            clickWhenSee('../'+path+'/dacanqueding.png')
            time.sleep(0.5)
            clickWhenSee('../'+path+'/dacanBack.png')
            time.sleep(0.5)
            clickWhenSee('../'+path+'/kanban.png')
    
    def replaceYao(self):
        hasXinxi = clickWhenSeeRegion('../'+path+'/xinxi.png',1155,680,1253-1155,771-680)
        if hasXinxi:
            print("replacing")
            random.shuffle(self.replacePoss)
            repPos = self.replacePoss[0]
            randomClickWithinRegion(*repPos)
            time.sleep(0.5)
           
            randomClickWithinRegion(*[919,939,255,276])
            time.sleep(0.5)
            randomClickWithinRegion(*[1057,1113,679,700])
            time.sleep(0.5)
            randomClickWithinRegion(*[49,66,47,66])
        else:
            print("not ready to replace")
         
if __name__ == '__main__':
    
    jy = jiayuan()
    
    #test place
    
    notThere = findImgRegion('../'+path+'/tuichu.png',0,0,1400,800)
    if notThere == None:
        jy.enter(['../'+path+'/tiaomu.png','../'+path+'/'+path+'.png','../'+path+'/huijia.png','../'+path+'/kanban.png'])
    
    countPengren = 0
    countWuxing = 0
    countAnying = 0
    while True:
        print('new iteration')
        #cli = clickWhenSee('../'+path+'/chengshou.png')
        #idx,found = findImgsRegion(['../'+path+'/chengshou.png','../'+path+'/chengshou2.png'],x=499,y=1127,w=1127-499,h=218-37)
        idx,found = findImgs(['../'+path+'/chengshou.png','../'+path+'/chengshou2.png'])
        if found != None:
            click(found)
            time.sleep(1)
            jy.zhongzhi()

            jy.zhongzhiing = False
        else:
            
            if args.songli:
                count = jy.findYao2(['../'+path+'/yaoling.png',
                            '../'+path+'/yiyuan.png',
                            '../'+path+'/quzhaota.png',
                            '../'+path+'/tanhao.png',
                            '../'+path+'/tanhao2.png',
                            '../'+path+'/pengren.png',
                            '../'+path+'/kanban.png'])
            else:
                count = jy.findYao(['../'+path+'/yaoling.png',
                            '../'+path+'/yiyuan.png',
                            '../'+path+'/quzhaota.png',
                            '../'+path+'/tanhao.png',
                            '../'+path+'/tanhao2.png',
                            '../'+path+'/pengren.png',
                            '../'+path+'/kanban.png'])
            if count != 0:
                jy.Act(['../'+path+'/shouxia.png',
                        '../'+path+'/shouxia2.png',
                        '../'+path+'/lingqujiangli.png',
                        '../'+path+'/huida.png',
                        '../'+path+'/huaquan.png',
                        '../'+path+'/queding.png',
                        '../'+path+'/huidaqueren.png',
                        '../'+path+'/daojishi.png',
                        '../'+path+'/kanban.png'])
        jy.replaceCount += 1
        if jy.replaceCount == 1:
            jy.replaceCount = 0
            jy.replaceYao()
         
        clickWhenSee('../'+path+'/queding2.png')
        
        #pengrenDone = jy.shoupengren()
        #if pengrenDone:
        #    print('go pengren')
        #    if args.pengren:
        #        jy.pengren()
        
        jy.dacan()
        
        if hasImgsRegion(['../'+path+'/tuichu.png'],x =1152 ,y=668,w = 1322-1152,h = 773-668 ):
            countPengren+=1
            countWuxing+=1
            countAnying+=1
            print('count to pengren: '+str(countPengren))
            print('count to wuxing: '+str(countWuxing))
            print('count to anying: '+str(countAnying))
            
            if countPengren == 1 or countPengren == 5:
                print('go pengren timely')
                if args.pengren:
                    jy.pengren()
                if countPengren == 5:
                    countPengren = 2
            
            if countWuxing == 1 or countWuxing == 15:
                print('go wuxing timely')
                if args.wuxing:
                    jy.goFuben('../'+path+'/wuxingxiulian.png','python fuben.py --goal 65535 --seq 132 --doge')             
                if countWuxing == 15:
                    countWuxing = 2
                  
            if countAnying == 1 or countAnying == 7:
                print('go anying timely')
                if args.anying:
                    jy.goFuben('../'+path+'/yunmenganying.png','python fuben.py --goal 65535 --anying --doge')             
                if countAnying == 7:
                    countAnying = 2

            if not jy.zhongzhiing:
                jy.gozhongzhi()


    '''
    while True:
        jy.pengren()
        #jy.goWuxing()
    '''
