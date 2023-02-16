import random
import pyautogui as p
import time
name=['C','C++','JAVA','PYTHON','SQL','HTML','CSS','JAVASCRIPT']
time.sleep(8)

for i in range(15):
    a=random.choice(name)
    p.write("Welcome"+" To"+" "+a+"  Language")
    p.press('enter')
