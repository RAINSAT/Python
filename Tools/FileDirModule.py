# coding:utf-8

import os
import time
from re import split


# 月份对应数字
month_dict = {
    "Jan": 1,
    "Feb": 2,
    "Mar": 3,
    "Apr": 4,
    "May": 5,
    "Jun": 6,
    "Jul": 7,
    "Aug": 8,
    "Sep": 9,
    "Oct": 10,
    "Nov": 11,
    "Dec": 12
}

# Global variable area
flag = 1


class FileInfo(object):
    """
    about file info
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    def get_file_time(file: str):  # 获得文件时间
        if os.path.isfile(file):
            return [time.ctime(os.path.getatime(file)),
                    time.ctime(os.path.getctime(file)),
                    time.ctime(os.path.getmtime(file))]
        else:
            return []

    @staticmethod
    def parse_time_str(ti: str):  # 解析时间字符串 Sun Sep 22 09:21:27 2019
        tim_lis = split("\s{1,}", ti)
        month = tim_lis[1]
        month_num = month_dict[month]
        hour = tim_lis[-2].split(':')
        return '{0}{1}{2}{3}{4}{5}'.format(tim_lis[-1], "{:0>2d}".format(month_num), "{:0>2d}".format(int(tim_lis[2])), hour[0], hour[1], hour[2])


class FileOperation(object):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # 重命名 按照时间
    @staticmethod
    def rename_on_time(file: str):  # 对文件按照创建时间重命名
        if os.path.isfile(file):
            ti = FileInfo.get_file_time(file)
            s = FileInfo.parse_time_str(ti[2])
            extension_name = file.split('.')[-1]  # 扩展名
            global flag
            try:
                os.rename(file, s + "." + extension_name)
            except:
                os.rename(file, s + "(" + str(flag) + ")" +
                          "." + extension_name)
                flag = flag + 1
        print(file + " rename success")

    @staticmethod
    def rename_dir(dir):
        os.chdir(dir)
        for f in os.listdir():
            if os.path.isfile(f):
                FileOperation.rename_on_time(f)
            else:
                os.chdir(dir + "/" + f)
                rename_dir(dir + "/" + f)
                os.chdir("../../")
                global flag
                flag = 1

    # 删除指定目录下 某扩展名的所有文件
    @staticmethod
    def delete_file_by_extension(dir: str, ex: list):
        if os.path.isdir(dir):
            stack = []
            stack.append(dir)
            while len(stack) > 0:
                start_dir = stack.pop()
                file_list = os.listdir(start_dir)
                for file in file_list:
                    if os.path.isdir(start_dir + "/" + file):
                        stack.append(start_dir + "/" + file)
                    else:
                        if file.split(".")[-1] in ex:
                            os.remove(start_dir + "/" + file)
                            print(start_dir+"/" + file + " 删除")


if __name__ == "__main__":
    FileOperation.rename_dir(r"E:\Users\Pictures\weibo")
