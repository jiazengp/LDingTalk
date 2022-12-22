# @author: xyz8848
# GitHub: https://github.com/xyz8848/LDingTalk
# Gitee: https://gitee.com/xyz8848/LDingTalk
import os.path
import time

import pyautogui

import dingtalk
from dingtalk.utils import window, auto_check_in
from main import base_dir


def start(num):
    locate = pyautogui.locateOnScreen(os.path.join(base_dir, "dingtalk/res/end.png"), grayscale=True, confidence=.9)
    if locate is None:
        auto_check_in.check(num)
    else:
        x, y, width, height = locate
        time.sleep(10)
        print("检测到直播结束（第" + str(num) + "次）")
        window.get_screenshot((0, 0, 1920, 1080))
        pyautogui.click(x + width - 15, y + height / 2, button="left")
        time.sleep(3)
        dingtalk.start()
