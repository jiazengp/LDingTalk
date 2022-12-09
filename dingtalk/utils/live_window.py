# @author: xyz8848
# GitHub: https://github.com/xyz8848/LDingTalk
# Gitee: https://gitee.com/xyz8848/LDingTalk
import time

import win32api
import win32con
import win32gui

from dingtalk.utils import window
from dingtalk.utils.window import get_all_hwnd, hwnd_title


# 检测直播窗口是否打开
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


# 检测直播是否开启
def is_live_open(screenshot):
    if screenshot.getpixel((5, 5)) == (224, 237, 254):
        print("检测到直播开启，正在检测是否已启动直播页面")
        return True
    else:
        return False


# 打开直播窗口
def open_window(dingtalk_main_window_handle, dingtalk_chat_window_handle):
    # 打开钉钉主窗口
    window.show_window(dingtalk_main_window_handle)

    # 模拟鼠标点击（打开钉钉直播）
    left, top, right, bottom = win32gui.GetWindowRect(dingtalk_chat_window_handle)
    move_x = left + 5
    move_y = top + 5
    win32api.SetCursorPos((move_x, move_y))  # 移动鼠标
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)  # 鼠标左键按下
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)  # 鼠标左键抬起
    print("启动完成，等待直播进入...")
    time.sleep(8)
