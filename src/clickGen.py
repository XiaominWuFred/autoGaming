import pyautogui
#get screen size
w,h = pyautogui.size()
#moving mouse
#pyautogui.moveTo(1160,693,duration = 1)
#while True:
#    pyautogui.doubleClick()

#pyautogui.moveRel() move relatively to current position
#pyautogui.moveRel(100,100,duration = 1)
#getting mouse position
print(pyautogui.position())
#pyautogui.scroll(-100)
#pyautogui.dragRel(0, -200, duration=0.2)
#loca = pyautogui.locateOnScreen('../pics/test.png', confidence =.8)
print(w)
print(h)
#print(loca)
