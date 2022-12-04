# @author: xyz8848
# GitHub: https://github.com/xyz8848
# Copyright (c) 2022-2023 xyz8848. All rights reserved.

import os
import shutil


def move(file1, path2):
    if not os.path.isfile(file1):
        print("%s not exist!" % (file1))
    else:
        path1, file1 = os.path.split(file1)  # 分离文件名和路径
        if not os.path.exists(path2):
            os.makedirs(path2)  # 创建文件夹
        shutil.move(file1, path2 + file1)  # 移动文件
        print("move %s -> %s" % (file1, path2 + file1))
