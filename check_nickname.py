import pyautogui
import time
import pyperclip
import hotkey
import requests

pyautogui.PAUSE = 0.0001
pyautogui.FAILSAFE = True
threshold = 5000

def findMumuPosition():
    x, y = pyautogui.locateCenterOnScreen('data/uuicon.PNG')
    return x, y

def typewrite(x):
    pyperclip.copy(x)
    pyperclip.paste()

#(79, 175)
#Point(x=894, y=275)
#Point(x=245, y=364)

head_poi= findMumuPosition()
search_poi = (head_poi[0] + 815, head_poi[1] + 100)
input_poi = (head_poi[0] + 675, head_poi[1] + 100)
check_poi = (head_poi[0] + 166, head_poi[1] + 189)
cancel_poi = (head_poi[0] + 735, head_poi[1] + 100)

nickname = "去"
pyautogui.click(input_poi)
time.sleep(1)
pyautogui.click(input_poi)
time.sleep(1)
pyautogui.press(['backspace', 'backspace', 'backspace'])
typewrite(nickname)
time.sleep(1)
pyautogui.press("enter")
time.sleep(1)
pyautogui.moveTo(search_poi)
region = (10, 10)
pyautogui.click(search_poi)
time.sleep(1)
target = pyautogui.screenshot(region=check_poi + region, imageFilename="tmp/sc.png")
target = target.load()

def diff(a, b):
    return sum([sum([abs(a[i, j][k] - b[i, j][k]) for k in range(3)]) for i in range(region[0]) for j in range(region[1])])


def weakup():
    requests.get('http://localhost:5000')

def record(tag, t):
    open("data/time.txt", 'a').write(tag +": " + str(t) + "\n")

count = 100
res = []
time_start = time.time()
times = []
while count > 0:
    count -= 1
    pyautogui.click(search_poi)
    im = pyautogui.screenshot(region=check_poi + region).load()
    dif = diff(target, im)
    if dif >= threshold:
        print("检测冻结期结束")
        record("脚本a结束时间", time.time())
        weakup()
        break
    # res.append(diff(target, im))
    time_now = time.time()
    print(time_now - time_start, count)
    times.append(time_now - time_start)
    time_start = time_now
    #time.sleep(5)

record("平均采集间隔", sum(times) / len(times))
while True:
    print(pyautogui.position())
    time.sleep(1)
    if hotkey.EXIT:
        print("退出程序")
        exit()
