# coding:utf-8

import os

"""
del all the files with the extension in the __dir__
"""


def del_file(path, fmt: tuple):
    li = os.listdir(path)
    for item in li:
        if os.path.isdir(path + "/" + item):
            del_file(path + "/" + item, fmt)
        else:
            if item.split(".")[-1] in fmt:
                print("remove:" + path + "/" + item)
                os.remove(path + "/" + item)


"""
delete all the blank dir in the __path__
if the __path__ is blank ,it will del __path 
"""


def remove_blank_dir(path):
    li = os.listdir(path)
    if len(li) == 0:
        os.removedirs(path)
        print("remove:" + path)
        return
    for item in li:
        if os.path.isdir(path + "/" + item):
            remove_blank_dir(path + "/" + item)
