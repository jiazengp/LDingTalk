# @author: xyz8848
# GitHub: https://github.com/xyz8848
# Copyright (c) 2022-2023 xyz8848. All rights reserved.

import config
from dingtalk.utils import auto_class, chat_window, live_window, main_window, window
import logging
import time


def start():
    if config.DingTalk.auto_class:
        # 获取钉钉主窗口句柄
        dingtalk_main_window_handle = main_window.get_handle()

        # 将钉钉主窗口最大化显示在屏幕最前端
        window.show_window(dingtalk_main_window_handle)

        # 获取钉钉所有子窗口的句柄
        dingtalk_child_window_handle = window.get_all_child_window(dingtalk_main_window_handle)

        # 获取钉钉聊天窗口句柄
        dingtalk_chat_window_handle = chat_window.get_window_handle(dingtalk_child_window_handle)

        # 获取钉钉聊天窗口坐标和窗口大小
        dingtalk_chat_window_pos = window.get_window_pos(dingtalk_chat_window_handle)

        # 检测直播是否开启
        dingtalk_chat_box_screenshot = window.get_screenshot(dingtalk_chat_window_pos)  # 获取直播窗口截图
        live_open = live_window.is_live_open(dingtalk_chat_box_screenshot)  # 传入截图进行检测
        if live_open:
            live_window.open_live(dingtalk_main_window_handle, dingtalk_chat_window_handle)  # 打开直播
            var = 1
            num = 0

            while var == 1:
                # 检测签到间隔时间（单位：秒）
                time.sleep(5)

                # 统计检测次数
                num = num + 1

                auto_class.start(num)
        else:
            logging.info("未检测到直播，60秒后进入下一轮检测")
            restart()
    else:
        var = 1
        num = 0

        # 循环检测签到
        while var == 1:
            # 检测签到间隔时间（单位：秒）
            time.sleep(5)

            # 统计检测次数
            num = num + 1

            auto_class.auto_check_in(num)


def restart():
    time.sleep(60)
    start()
