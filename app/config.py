import os
import sys
import platform

STSTEM_TYPE = platform.system()

# 文件操作文件目录
TXT_DIR = os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))

TXT_DIR = ""

if STSTEM_TYPE == "Windows":
    TXT_DIR = os.path.dirname(os.path.realpath(sys.argv[0]))
else:
    TXT_DIR = os.path.dirname(os.path.dirname(
        os.path.abspath(__file__)))


# 用户账户数据文件
USER_TXT = TXT_DIR + "/user.txt"

# 抢购成功账户数据
SUCCESS_TXT = TXT_DIR + "/success.txt"
