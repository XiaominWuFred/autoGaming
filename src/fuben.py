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

parser = argparse.ArgumentParser()
parser.add_argument('--goal', type=int, default=100, help='goal')
parser.add_argument('--anying',action='store_true', default=False,help='go anying.')
parser.add_argument('--doge',action='store_true', default=False,help='doge .')
parser.add_argument('--seq', action="store", default='111',type=str)

args = parser.parse_args()

piao = ['../pics/piaotuzi.png',
        '../pics/piaoziji.png',
        #'../pics/piao1.png',
        '../pics/piao2.png',
        '../pics/piao.png',
        #'../pics/piao9.png',
        '../pics/piaotudi.png',
        #'../pics/piao5.png',
        #'../pics/piao6.png',
        #'../pics/piao7.png'
        ]
        
class fuben():
    def __init__(self,goal):
        self.goal = goal
        self.count = 0
        self.meitili = False
        self.generalIter = 0
        self.bossCount = 0
        
        self.skillPos = [[1036,1072,360,400],[1161,1184,369,392],[1265,1295,367,396]]
        self.settingPos = [1277,1339,226,280]
        self.posClicked = [False,False,False]
        self.clicks = [self.clickPos1,self.clickPos2,self.clickPos3]
        
    
    def clickPos1(self):
        if hasImgsRegion(['../pics/zhandou.png','../pics/zhandou2.png','../pics/zhandou3.png','../pics/zhandou3.png'],1119,561,1305-1119,748-561):
            randomClickWithinRegion(1036,1072,369,392)
            #if hasImgsRegion(['../pics/setting.png'],1277,226,1339-1277,280-226):
            if hasImgsRegion(['../pics/zhandou.png','../pics/zhandou2.png','../pics/zhandou3.png'],1119,561,1305-1119,748-561):            
                pass
            else:
                if not hasImgsRegion(['../pics/dot.png'],1113,224,1276-1113,290-224):
                    print('                              set pos1 True')
                    self.posClicked[0] = True 
                else:
                    print('                                  found dot')
    
    def clickPos2(self):
        if hasImgsRegion(['../pics/zhandou.png','../pics/zhandou2.png','../pics/zhandou3.png'],1119,561,1305-1119,748-561):
            randomClickWithinRegion(1161,1184,369,392)
            if hasImgsRegion(['../pics/zhandou.png','../pics/zhandou2.png','../pics/zhandou3.png'],1119,561,1305-1119,748-561):
                pass
            else:
                if not hasImgsRegion(['../pics/dot.png'],1113,224,1276-1113,290-224):
                    print('                              set pos2 True')
                    self.posClicked[1] = True 
                else:
                    print('                                  found dot')
        
    def clickPos3(self):
        if hasImgsRegion(['../pics/zhandou.png','../pics/zhandou2.png','../pics/zhandou3.png'],1119,561,1305-1119,748-561):
            randomClickWithinRegion(1265,1295,369,392)
            if hasImgsRegion(['../pics/zhandou.png','../pics/zhandou2.png','../pics/zhandou3.png'],1119,561,1305-1119,748-561):
                pass
            else:
                if not hasImgsRegion(['../pics/dot.png'],1113,224,1276-1113,290-224):
                    print('                              set pos3 True')
                    self.posClicked[2] = True 
                else:
                    print('                                  found dot')
        
    #sequence = [1,2,3]    
    def skills(self,sequence):
        print(self.posClicked)
        if sequence[0] == sequence[1] and sequence[1] == sequence[2]:
            print('auto ordering')
            pass
        else:
            if self.posClicked[sequence[0]-1] == False:
                self.clicks[sequence[0]-1]()
                   
            while not hasImgsRegion(['../pics/zhandou.png','../pics/zhandou2.png','../pics/zhandou3.png'],1119,561,1305-1119,748-561):
                time.sleep(0.1)
                if hasImgsRegion(['../pics/shouyao.png'],884,420,1058-884,543-420):
                    break
                if not hasImgsRegion(['../pics/haoyou.png'],363,687,474-363,779-687):
                    break
                
            if self.posClicked[sequence[0]-1] == True and self.posClicked[sequence[1]-1] == False:
                self.clicks[sequence[1]-1]()
                
            while not hasImgsRegion(['../pics/zhandou.png','../pics/zhandou2.png','../pics/zhandou3.png'],1119,561,1305-1119,748-561):
                time.sleep(0.1)
                if hasImgsRegion(['../pics/shouyao.png'],884,420,1058-884,543-420):
                    break
                if not hasImgsRegion(['../pics/haoyou.png'],363,687,474-363,779-687):
                    break
               
            if self.posClicked[sequence[1]-1] == True and self.posClicked[sequence[2]-1] == False:
                self.clicks[sequence[2]-1]()

            while not hasImgsRegion(['../pics/zhandou.png','../pics/zhandou2.png','../pics/zhandou3.png'],1119,561,1305-1119,748-561):
                time.sleep(0.1)
                if hasImgsRegion(['../pics/shouyao.png'],884,420,1058-884,543-420):
                    break
                if not hasImgsRegion(['../pics/haoyou.png'],363,687,474-363,779-687):
                    break

            if self.posClicked[0] and self.posClicked[1] and self.posClicked[2]:
                self.posClicked[0] = False
                self.posClicked[1] = False
                self.posClicked[2] = False
            
    def general(self,starts):
        if clickWhenSeeRegionS(starts,24,40,1322-24,765-40):
            self.posClicked[0] = False
            self.posClicked[1] = False
            self.posClicked[2] = False
        
        
        clickWhenSeeRegion('../pics/shouyao.png',870,408,1069-870,533-408)
        
        if clickWhenSee('../pics/jixu.png'):
            tc = 18
            while not hasImgs(starts) and tc > 0:
                clickWhenSee('../pics/jixu.png')
                print('jixu count down: '+str(tc))
                tc-=1
            
        if hasImgsRegion(['../pics/buzaitixing.png'],587,459,827-587,538-459):
            return
        
        if clickWhenSee('../pics/queren.png'):
            dis = random.randint(150,200)
            randomDragUpWithinRegion(650,700,350,420,-dis)
            time.sleep(0.3)
            if hasImgsRegion(['../pics/meitili.png'],924,475,1070-924,514-475):
                self.meitili = True
                clickWhenSee('../pics/cross.png')
                time.sleep(0.1)
                clickWhenSee('../pics/back.png')
                time.sleep(0.1)
                clickWhenSee('../pics/backhuodong.png')
                time.sleep(0.1)
                clickWhenSee('../pics/huodongcross.png')
                return
            
            tc = 10
            while not clickImgsRelBotRight(['../pics/shihe.png'],600,0) and tc>0:
                print('finding shihe '+str(tc))
                tc-=1
            
            clickWhenSee('../pics/cross.png')
            time.sleep(0.2)
            clickWhenSee('../pics/cross.png')
            time.sleep(0.2)
            
        if hasImgs(['../pics/shuaxin.png']):  
            countDown = 2
            while not clickImgsRel(piao,0,150):
                print('shuaxin count down: '+str(countDown))
                #clickWhenSee('../pics/shuaxin.png')
                
                randomClickWithinRegion(247,285,287,328)
                time.sleep(0.4)
                clickWhenSeeRegion('../pics/zhuzhan.png',175,268,1137-175,390-268)
                time.sleep(0.4)
                countDown-=1
                if countDown == 0:
                    clickWhenSee('../pics/shuaxin.png')
                    countDown = 2
                    time.sleep(0.4)
            time.sleep(1)
            
        if clickWhenSee('../pics/kaishifuben.png'):
            self.count+=1
            print('With Goal :'+str(self.goal)+' Finished count : '+str(self.count))
            return 
            
        if clickImgsRel(['../pics/qingyi.png',
                         '../pics/qingyi4.png',
                         '../pics/qingyi5.png',
                         '../pics/qingyi2.png',
                         '../pics/qingyi3.png'],0,0):
            time.sleep(0.1)
            pydirectinput.click()
            return 
        
        clickWhenSee('../pics/zhidaole.png')
        clickWhenSee('../pics/queren2.png')  
        clickWhenSee('../pics/tuichufuben.png')
        clickWhenSee('../pics/cross.png')

    def bianshen(self):
        self.generalIter += 1
        #print(self.generalIter)
        if self.generalIter == 2:
            randomClickWithinRegion(49,80,172,205)
            self.generalIter = 0
    
    def anying(self,starts,seq):

        if args.doge:
            imgs = ['../pics/fabaozhu.png',
                         '../pics/fabao2.png',
                         '../pics/doge.png']
        else:
            imgs = ['../pics/fabaozhu.png',
                         '../pics/fabao2.png']
                         
        if clickImgsRel(imgs,0,0):
            pass
        
        if hasImgs(['../pics/zhandou.png','../pics/zhandou2.png','../pics/zhandou3.png']):
            self.skills(seq)
            print('sleep...zzz')
            self.bianshen()
            time.sleep(2)   
            return False
        else:
            #print('xiansuo')
            #if hasImgsRegion(['../pics/qingqiuzhiyuan.png'],720,562,950-720,653-562)
            
            isQuexiao = clickWhenSeeRegion('../pics/quxiao.png',274,444,507-274,547-444)
            if isQuexiao:
                randomClickWithinRegion(28,67,40,75)
                time.sleep(0.5)
                clickWhenSeeRegion('../pics/fenxiang.png',705,544,952-705,665-544)
                time.sleep(0.1)
                randomClickWithinRegion(884,993,478,516)
                #time.sleep(0.1)
                randomClickWithinRegion(1253,1302,473,508)
                time.sleep(3)
                randomClickWithinRegion(28,67,40,75)
                self.bossCount += 1
                print('Have triggered BOSS count: '+str(self.bossCount))
                #finish, goto jiayuan
                return True
                
            else:
                clickWhenSeeRegion('../pics/xunzhaoxiansuo.png',755,524,1190-755,693-524)
                clickWhenSeeRegion('../pics/teji.png',794,421,1275-794,576-421)
            
        
            self.general(starts)
            return False
    
    def target(self,starts,seq):
        if args.doge:
            imgs = ['../pics/fabaozhu.png',
                         '../pics/fabao2.png',
                         '../pics/doge.png']
        else:
            imgs = ['../pics/fabaozhu.png',
                         '../pics/fabao2.png']
                         
        if clickWhenSeeRegionS(['../pics/jump.png'],1100,38,1196-1100,84-38):
            time.sleep(0.5)
            clickWhenSeeRegionS(['../pics/queren.png'],835,461,1045-835,542-461)
                       
        if clickImgsRel(imgs,0,0):
            pass
        
        if hasImgs(['../pics/zhandou.png','../pics/zhandou2.png','../pics/zhandou3.png']):          
            self.skills(seq)
            print('sleep...zzz')
            self.bianshen()
            time.sleep(2)    
        else:
            self.general(starts)

if __name__ == '__main__':
    window = gw.getWindowsAt(650,350)[0]
    print(window.size)
    window.moveTo(0,0)
    window.resizeTo(1350, 790)

    sequnce = []
    for char in args.seq:
        sequnce.append(int(char))

    print(sequnce)
	
    Goal = args.goal
    fb = fuben(Goal)
    wuxing = False    
    while fb.count < fb.goal and not fb.meitili:
        if args.anying:
            if hasImgsRegion(['../pics/fengyaozhong.png'],967,437,1196-967,561-437):
                break
            if fb.anying(['../pics/tiaozhan.png'],sequnce):
                break
        else:
            fb.target(['../pics/tiaozhan.png','../pics/danren.png','../pics/kaishixiulian.png'],sequnce)
            
    time.sleep(3)
    
    '''
    lastFinish = False
    finalCount = fb.count
    while fb.count >= fb.goal and not lastFinish:
        if args.wuxing:
            start = '../pics/kaishixiulian.png'
            lastFinish = hasImgs([start])
            if not lastFinish:
                fb.wuxingxiulian(start)
            
        if args.huanjing:
            start = '../pics/danren.png'
            lastFinish = hasImgs([start])
            if not lastFinish:
                fb.huanjing(start)
            
        if args.huodong:
            start = '../pics/tiaozhan.png'
            lastFinish = hasImgs([start])
            if not lastFinish:
                fb.huodong(start)
            
        
    fb.count = finalCount
    '''
    
    time.sleep(0.5)
    clickWhenSee('../pics/cross.png')   
    time.sleep(0.5)             
    clickWhenSee('../pics/back.png')
    time.sleep(0.5)
    clickWhenSee('../pics/backhuodong.png')
    time.sleep(0.5)
    clickWhenSee('../pics/huodongcross.png')

    print('Finished Times: '+str(fb.count)+' Program Closed')

    
    