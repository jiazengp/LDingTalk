# @author: xyz8848
# GitHub: https://github.com/xyz8848/LDingTalk
# Gitee: https://gitee.com/xyz8848/LDingTalk
import dingtalk

name = "LDingTalk"
author = "xyz8848"
version = "v1.4.0"
github = "https://github.com/xyz8848/LDingTalk"
gitee = "https://gitee.com/xyz8848/LDingTalk"

if __name__ == '__main__':
    print("=============== " + name + " ===============")
    print(name + " " + version)
    print("Author: " + author)
    print("GitHub: " + github)
    print("Gitee: " + gitee)
    print("=========================================")

    dingtalk.start()
