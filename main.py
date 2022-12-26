# @author: xyz8848
# GitHub: https://github.com/xyz8848/LDingTalk
# Gitee: https://gitee.com/xyz8848/LDingTalk
import os.path
import sys

import requests as requests
import yaml

import dingtalk

name = "LDingTalk"
author = "xyz8848"
version = "v2.1.0"
github = "https://github.com/xyz8848/LDingTalk"
gitee = "https://gitee.com/xyz8848/LDingTalk"

base_dir = os.path.dirname(os.path.realpath(sys.argv[0]))

config_file = os.path.join(base_dir, "config.yml")

config = yaml.load(open(config_file, encoding="UTF-8"), Loader=yaml.FullLoader)

if config["dingtalk"]["get_latest_version"]:
    latest_version = requests.get("https://api.github.com/repos/xyz8848/LDingTalk/releases/latest").json()["tag_name"]

if __name__ == '__main__':
    print("=============== " + name + " ===============")
    print("当前版本: " + version)
    if config["dingtalk"]["get_latest_version"]:
        print("最新版本: " + latest_version)
    print("Author: " + author)
    print("GitHub: " + github)
    print("Gitee: " + gitee)
    print("=========================================")

    dingtalk.start()
