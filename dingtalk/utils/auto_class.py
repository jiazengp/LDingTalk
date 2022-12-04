# @author: xyz8848
# GitHub: https://github.com/xyz8848
# Copyright (c) 2022-2023 xyz8848. All rights reserved.

import time

import pyautogui

import dingtalk
from dingtalk.utils import window


def start(num):
    msg = pyautogui.locateOnScreen("dingtalk/res/end.png", grayscale=True, confidence=.9)
    if msg is None:
        auto_check_in(num)
    else:
        x, y, width, height = msg
        time.sleep(10)
        print("检测到直播结束（第", num, "次）")
        window.get_screenshot((0, 0, 1920, 1080))
        pyautogui.click(x + width - 15, y + height / 2, button="left")
        time.sleep(3)
        dingtalk.start()


def auto_check_in(num):
    # 签到 2.0
    msg = pyautogui.locateOnScreen("dingtalk/res/check_in.png", grayscale=True, confidence=.9)
    if msg is None:
        print("未检测到签到（第", num, "次）")
    else:
        x, y, width, height = msg
        print("检测到签到！（第", num, "次）")
        print("签到按钮位于：X={}，Y={}".format(x, y))
        window.get_screenshot((0, 0, 1920, 1080))
        pyautogui.click(x, y, button="left")
        window.get_screenshot((0, 0, 1920, 1080))

    # 签到 1.0
    # locate_center_on_screen = pyautogui.locateCenterOnScreen("dingtalk/res/check_in.png")  # 识别签到按钮
    # if locate_center_on_screen is not None:
    #     print("检测到签到！（第", num, "次）")
    #     window.get_screenshot((0, 0, 1920, 1080))
    #     pyautogui.click(x=1015, y=680)  # 点击签到按钮
    #     time.sleep(0.1)
    #     window.get_screenshot((0, 0, 1920, 1080))
    #
    # else:
    #     print("未检测到签到（第", num, "次）")
