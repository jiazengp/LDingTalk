# @author: xyz8848
# GitHub: https://github.com/xyz8848
# Copyright (c) 2022-2023 xyz8848. All rights reserved.
import time

import pyautogui


def clicker(x, y):
    var = 1
    s = 0
    # 循环点击
    while var == 1:
        # 循环点击间隔时间（单位：秒）
        time.sleep(5)

        # 统计点击次数
        s = s + 1

        # 点击指定坐标
        pyautogui.click(x, y)
        print("点击", s, "次")
