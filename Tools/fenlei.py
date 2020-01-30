# -*- coding:utf-8 -*-

import os

# from PIL import Image
# Rename
dir_path = r"E:\Users\Pictures\sina\weibo"

os.chdir(dir_path)

file_lists = os.listdir(dir_path)

"""
format time
"""


def format_time(long_time):
    import time
    return time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime(long_time))


def rename(file: str):
    # get file info
    fileinfo = os.stat(file)
    # 最后一次修改时间
    mtime = fileinfo.st_mtime
    # 文件大小
    fileinfo.st_size
    return format_time(mtime)


for file in file_lists:
    s = rename(file)
    os.rename(file, s + ".jpg")
    print(s)
