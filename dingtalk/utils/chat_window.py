# @author: xyz8848
# GitHub: https://github.com/xyz8848
# Copyright (c) 2022-2023 xyz8848. All rights reserved.

import win32gui


def get_window_handle(handle):
    for child_window_handle in handle:
        if win32gui.GetWindowText(child_window_handle) == "Chrome Legacy Window":
            print("获取到聊天窗口句柄：" + str(child_window_handle))
            # win32gui.ShowWindow(ding_main_window_handle, win32con.SW_MINIMIZE)  # 完成后最小化钉钉主窗口
            print("准备就绪，3s后开始检测")
            return child_window_handle
