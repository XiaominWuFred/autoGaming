import pyautogui
import time

time.sleep(2)

for i in range(500):
    path = '../train/zuo/'+str(i)+'.png'
    im = pyautogui.screenshot(region = (1045,299,1105-1045,366-299))
    im.save(path)
    time.sleep(0.1)
    print('pic '+str(i)+' took')