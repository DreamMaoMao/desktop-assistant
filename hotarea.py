# 导入模块
import pyautogui
import time


inarea = False
pyautogui.FAILSAFE = False

# 循环检测鼠标位置
while True:
    # 获取鼠标的当前位置
    mouse_x, mouse_y = pyautogui.position()
    
    # 如果鼠标在右上角
    if mouse_x < 10 and mouse_y < 10 and not inarea:
        pyautogui.press('win')
        inarea = True
    elif inarea and (mouse_x >= 10 or mouse_y >= 10):
        inarea =  False
    time.sleep(0.1)