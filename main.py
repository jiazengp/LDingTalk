# @author: xyz8848
# GitHub: https://github.com/xyz8848
# Copyright (c) 2022-2023 xyz8848. All rights reserved.

import dingtalk

name = "LDingTalk"
author = "xyz8848"
version = "v1.1.0"

if __name__ == '__main__':
    print("====================")
    print(name + " " + version)
    print("Author: " + author)
    print("====================")

    dingtalk.start()
