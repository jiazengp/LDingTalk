# @author: xyz8848
# GitHub: https://github.com/xyz8848/LDingTalk
# Gitee: https://gitee.com/xyz8848/LDingTalk
import win32gui


# 获取聊天窗口句柄
def get_window_handle(handle):
    for child_window_handle in handle:
        if win32gui.GetWindowText(child_window_handle) == "Chrome Legacy Window":
            print("获取到聊天窗口句柄：" + str(child_window_handle))
            print("准备就绪，3s后开始检测")
            return child_window_handle
