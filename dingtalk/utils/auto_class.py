# @author: xyz8848
# GitHub: https://github.com/xyz8848/LDingTalk
# Gitee: https://gitee.com/xyz8848/LDingTalk
import time

import pyautogui

import config
import dingtalk
from dingtalk.utils import window


def start(num):
    locate = pyautogui.locateOnScreen("dingtalk/res/end.png", grayscale=True, confidence=.9)
    if locate is None:
        auto_check_in(num)
    else:
        x, y, width, height = locate
        time.sleep(10)
        print("检测到直播结束（第" + str(num) + "次）")
        window.get_screenshot((0, 0, 1920, 1080))
        pyautogui.click(x + width - 15, y + height / 2, button="left")
        time.sleep(3)
        dingtalk.start()


# 自动签到
def auto_check_in(num):
    if config.DingTalk.auto_check_in:
        locate = pyautogui.locateOnScreen("dingtalk/res/check_in.png", grayscale=True, confidence=.9)
        if locate is None:
            print("未检测到签到（第" + str(num) + "次）")
        else:
            x, y, width, height = locate
            print("检测到签到！（第" + str(num) + "次）（签到按钮坐标：x=" + str(x) + ", y=" + str(y) + "）")
            window.get_screenshot((0, 0, 1920, 1080))
            pyautogui.click(x, y, button="left")
