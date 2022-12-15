# @author: xyz8848
# GitHub: https://github.com/xyz8848/LDingTalk
# Gitee: https://gitee.com/xyz8848/LDingTalk
import os.path
import sys

import yaml

import dingtalk

name = "LDingTalk"
author = "xyz8848"
version = "v2.0.0"
github = "https://github.com/xyz8848/LDingTalk"
gitee = "https://gitee.com/xyz8848/LDingTalk"

base_dir = os.path.dirname(os.path.realpath(sys.argv[0]))

config_file = os.path.join(base_dir, "config.yml")

config = yaml.load(open(config_file, encoding="UTF-8"), Loader=yaml.FullLoader)

if __name__ == '__main__':
    print("=============== " + name + " ===============")
    print(name + " " + version)
    print("Author: " + author)
    print("GitHub: " + github)
    print("Gitee: " + gitee)
    print("=========================================")

    dingtalk.start()
