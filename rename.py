import pyautogui
import time
from flask import Flask
import pyperclip

from PIL import Image

pyautogui.PAUSE = 0.0001
pyautogui.FAILSAFE = True
app = Flask(__name__)
nickname = "去"

def findMumuPosition():
    x, y = pyautogui.locateCenterOnScreen('data/uuicon.PNG')
    return x, y

def findReID():
    x, y = pyautogui.locateCenterOnScreen('data/uuicon.PNG')
    return x, y

def findInput():
    x, y = pyautogui.locateCenterOnScreen('data/uuicon.PNG')
    return x, y

def findConfirm():
    x, y = pyautogui.locateCenterOnScreen('data/uuicon.PNG')
    return x, y

def typewrite(x):
    pyperclip.copy(x)
    pyperclip.paste()

def record(tag, t):
    open("data/time.txt", 'a').write(tag +": " + str(t) + "\n")

@app.route('/')
def process():
    print("开始改名")
    record("脚本b开始时间", time.time())
    pyautogui.click(findConfirm())
    record("脚本b结束时间", time.time())

def init_rename():
    pyautogui.click(findReID())
    pyautogui.click(findInput())
    typewrite(nickname)
    pyautogui.press("enter")


def init():
    init_rename()
    app.run(host='127.0.0.1', port=5000)
    # head_poi = findMumuPosition()


init()


