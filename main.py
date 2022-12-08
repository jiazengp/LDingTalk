# @author: xyz8848
# GitHub: https://github.com/xyz8848/LDingTalk
# Gitee: https://gitee.com/xyz8848/LDingTalk
import logging

import dingtalk

name = "LDingTalk"
author = "xyz8848"
version = "v1.2.0"

if __name__ == '__main__':
    print("====================")
    print(name + " " + version)
    print("Author: " + author)
    print("====================")

    logger = logging.getLogger()
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter("[%(levelname)s] %(message)s"))
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

    dingtalk.start()
