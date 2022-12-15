# @author: xyz8848
# GitHub: https://github.com/xyz8848/LDingTalk
# Gitee: https://gitee.com/xyz8848/LDingTalk
import datetime
import os
import time

import win32con
import win32gui
from PIL import ImageGrab

from main import config

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
    screenshot = ImageGrab.grab(window_pos)  # 截图
    screenshot_name = "Screenshot_" + str(datetime.date.today()) + '_' + str(round(time.time() * 1000)) + ".png"
    screenshots_dir = config["dingtalk"]["screenshots_dir"]

    if config["dingtalk"]["save_screenshot"]:
        path = os.path.join(screenshots_dir, os.sep.join([str(screenshot_name)]))

        if not os.path.isdir(screenshots_dir):
            os.mkdir(screenshots_dir)

        screenshot.save(path)  # 保存截图

    return screenshot
