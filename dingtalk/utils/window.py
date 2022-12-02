# @author: xyz8848
# GitHub: https://github.com/xyz8848
# Copyright (c) 2022-2023 xyz8848. All rights reserved.
import datetime
import os
import time

import win32con
import win32gui
from PIL import ImageGrab

hwnd_title = {}


# 获取所有窗口的句柄
def get_all_hwnd(hwnd, a):  # 不要删除未使用形参 'a' ！！！
    if (win32gui.IsWindow(hwnd) and
            win32gui.IsWindowEnabled(hwnd) and
            win32gui.IsWindowVisible(hwnd)):
        hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})


# 获取窗口的所有子窗口的句柄
def get_all_child_window(parent):
    if not parent:
        return
    child_window_hwnd_list = []
    win32gui.EnumChildWindows(
        parent, lambda hwnd, param: param.append(hwnd), child_window_hwnd_list)
    return child_window_hwnd_list


# 强制窗口在最前端显示
def set_foreground(handle):
    while True:
        try:
            win32gui.SetForegroundWindow(handle)  # 强制在最前端显示
            return
        except:
            time.sleep(0.1)


def show_window(handle):
    win32gui.ShowWindow(handle, win32con.SW_MAXIMIZE)  # 最大化
    set_foreground(handle)  # 强制在最前端显示
    time.sleep(2)


def get_window_pos(handle):
    x_start, y_start, x_end, y_end = win32gui.GetWindowRect(handle)
    window_pos = (x_start, y_start, x_end, y_end)
    return window_pos


def get_screenshot(window_pos):
    t1 = str(datetime.date.today())
    t2 = str(round(time.time() * 1000))
    t = str(t1) + '_' + str(t2)
    screenshot = ImageGrab.grab(window_pos)  # 截图
    screenshot.save(os.sep.join(["Screenshot_" + str(t) + ".png"]))  # 保存截图
    return screenshot
