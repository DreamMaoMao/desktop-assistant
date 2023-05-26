import keyboard
import mouse
import time
import os

# 定义一个函数，用来检测当前活动窗口是否是vlc player
def is_vlc_active():
    # 使用wmctrl命令来获取当前活动窗口的标题
    title = os.popen('wmctrl -l | grep $(xprop -root | grep _NET_ACTIVE_WINDOW | head -1 | awk \'{print $5}\' | awk -F "x" \'{print $2}\')').read()
    # 如果标题包含"VLC media player"，则返回True，否则返回False
    print(title)
    return "VLC media player" in title


# 定义一个回调函数，用来在鼠标左键单击时模拟按下空格键
def on_click():
    # 如果当前活动窗口是vlc player
    if is_vlc_active():
        # 模拟按下并松开空格键
        keyboard.press_and_release('space')

# 注册鼠标左键单击事件的回调函数
mouse.on_click(on_click)

# 无限循环，直到按下esc键退出
while True:
    # 等待，避免占用太多CPU资源
    time.sleep(1000000)

# 注销鼠标左键单击事件的回调函数
# mouse.unhook_all()
