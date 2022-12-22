# @author: xyz8848
# GitHub: https://github.com/xyz8848/LDingTalk
# Gitee: https://gitee.com/xyz8848/LDingTalk
import os

import pyautogui

from dingtalk.utils import window
from main import base_dir, config


def check(num):
    if config["dingtalk"]["auto_check_in"]:
        locate = pyautogui.locateOnScreen(os.path.join(base_dir, "dingtalk/res/check_in.png"), grayscale=True,
                                          confidence=.9)
        if locate is None:
            print("未检测到签到（第" + str(num) + "次）")
        else:
            x, y, width, height = locate
            print("检测到签到！（第" + str(num) + "次）（签到按钮坐标：x=" + str(x) + ", y=" + str(y) + "）")
            window.get_screenshot((0, 0, 1920, 1080))
            pyautogui.click(x, y, button="left")
