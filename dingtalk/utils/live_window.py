# @author: xyz8848
# GitHub: https://github.com/xyz8848
# Copyright (c) 2022-2023 xyz8848. All rights reserved.

from dingtalk.utils import window
from dingtalk.utils.window import get_all_hwnd, hwnd_title
import logging
import time
import win32api
import win32con
import win32gui


def is_window_open():
    while True:
        # 查找所有窗口标题和句柄 StandardFrame
        win32gui.EnumWindows(get_all_hwnd, 0)
        try:
            for handle, title in hwnd_title.items():
                if title == '钉钉' and win32gui.GetClassName(handle) == "StandardFrame":
                    is_opened = True
                    return is_opened
        except:
            is_opened = False
            return is_opened


def is_live_open(screenshot):
    if screenshot.getpixel((5, 5)) == (224, 237, 254):
        logging.info("检测到直播开启，正在检测是否已启动直播页面")
        return True
    else:
        return False


def open_live(dingtalk_main_window_handle, dingtalk_chat_window_handle):
    # 打开钉钉主窗口
    window.show_window(dingtalk_main_window_handle)

    # 模拟鼠标点击（打开钉钉直播）
    left, top, right, bottom = win32gui.GetWindowRect(dingtalk_chat_window_handle)
    move_x = left + 5
    move_y = top + 5
    win32api.SetCursorPos((move_x, move_y))  # 鼠标挪到点击处
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)  # 鼠标左键按下
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)  # 鼠标左键抬起
    print("[INFO] 启动完成，等待直播进入...")
    time.sleep(8)

# # Legacy
# def open_live(dingtalk_main_window_handle, dingtalk_chat_window_handle):
#     is_opened = is_open()
#     if is_opened:
#         print("直播窗口已打开，正在监控直播窗口变化")
#         on_update()
#     else:
#         print("直播窗口未打开，正在尝试打开直播窗口")
#
#         # 打开钉钉主窗口
#         window.show_window(dingtalk_main_window_handle)
#
#         # 模拟鼠标点击（打开钉钉直播）
#         left, top, right, bottom = win32gui.GetWindowRect(dingtalk_chat_window_handle)
#         move_x = left + 5
#         move_y = top + 5
#         win32api.SetCursorPos((move_x, move_y))  # 鼠标挪到点击处
#         win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)  # 鼠标左键按下
#         win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)  # 鼠标左键抬起
#         print("启动完成，等待直播进入...")
#         time.sleep(8)
#         print("开始获取直播窗口...")
#         is_opened_1 = is_open()
#         if is_opened_1:
#             print("直播窗口已打开，开始监控直播窗口变化")
#             on_update()
#         else:
#             print("打开失败，" + str(60) + "s后再次尝试...")
