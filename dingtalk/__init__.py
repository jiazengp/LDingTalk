# @author: xyz8848
# GitHub: https://github.com/xyz8848
# Copyright (c) 2022-2023 xyz8848. All rights reserved.
import time

from dingtalk.utils import main_window, window, chat_window, live_window


def start():
    dingtalk_main_window_handle = main_window.get_handle()
    window.show_window(dingtalk_main_window_handle)
    dingtalk_child_window_handle = window.get_all_child_window(dingtalk_main_window_handle)
    dingtalk_chat_window_handle = chat_window.get_window_handle(dingtalk_child_window_handle)
    dingtalk_chat_window_pos = window.get_window_pos(dingtalk_chat_window_handle)
    dingtalk_chat_box_screenshot = window.get_screenshot(dingtalk_chat_window_pos)
    live_open = live_window.is_live_open(dingtalk_chat_box_screenshot)
    if live_open:
        live_window.open_live(dingtalk_main_window_handle, dingtalk_chat_window_handle)
    else:
        print("未检测到直播，60秒后进入下一轮检测")
        restart()


def restart():
    time.sleep(60)
    start()
