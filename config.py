# @author: xyz8848
# GitHub: https://github.com/xyz8848/LDingTalk
# Gitee: https://gitee.com/xyz8848/LDingTalk

# 钉钉自动上课脚本
class DingTalk(object):
    auto_check_in = True  # 自动签到
    auto_check_in_delay_time = 5  # 自动签到间隔时间（单位：秒）
    auto_class = True  # 自动上课 & 自动下课
    check_is_live_open_delay_time = 60  # 检测直播是否开启的间隔时间（单位：秒）
    save_screenshot = True  # 保存截图
