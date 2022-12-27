# @author: xyz8848
# GitHub: https://github.com/xyz8848/LDingTalk
# Gitee: https://gitee.com/xyz8848/LDingTalk
import os
import time

import pyautogui
from PIL import ImageGrab

from dingtalk.utils import chat_window, live_window, main_window, window, auto_check_in
from main import config, base_dir


def start():
    while config["dingtalk"]["auto_class"]["enable"]:
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
        dingtalk_chat_box_screenshot = ImageGrab.grab(dingtalk_chat_window_pos)  # 获取直播窗口截图
        is_live_open = live_window.is_live_open(dingtalk_chat_box_screenshot)  # 传入截图进行检测
        if is_live_open:
            live_window.open_window(dingtalk_main_window_handle, dingtalk_chat_window_handle)  # 打开直播

            num = 0

            while True:
                time.sleep(config["dingtalk"]["auto_class"]["check_end_delay_time"])

                # 统计检测次数
                num = num + 1

                locate = pyautogui.locateOnScreen(os.path.join(base_dir, "dingtalk/res/end.png"), grayscale=True,
                                                  confidence=.9)
                if locate is None:
                    auto_check_in.check(num)
                else:
                    x, y, width, height = locate
                    print("检测到直播结束（第" + str(num) + "次）")
                    pyautogui.click(x + width - 15, y + height / 2, button="left")
                    break
        else:
            auto_class_delay_time = config["dingtalk"]["auto_class"]["check_open_delay_time"]
            print("未检测到直播，" + str(auto_class_delay_time) + "秒后进入下一轮检测")
            time.sleep(auto_class_delay_time)

    while config["dingtalk"]["auto_check_in"]["enable"]:

        num = 0

        # 循环检测签到
        while True:
            time.sleep(config["dingtalk"]["auto_check_in"]["delay_time"])

            # 统计检测次数
            num = num + 1

            auto_check_in.check(num)
