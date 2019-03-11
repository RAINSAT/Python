# -*- coding: UTF-8 -*-

import os
# import sys
#
# src = sys.argv[1]
# dst = sys.argv[2]

formats = ['rar', 'zip', '7z', 'ace', 'arj', 'bz2',
           'cab', 'gz', 'iso', 'jar', 'lzh', 'tar', 'uue', 'z']


def rar(src_path,password):
    os.chdir(src_path)
    for file in os.listdir('.'):
        if os.path.isfile(file):
            fmat = file.split('.')[-1]
            if fmat in formats:
                # -p
                cmd = 'winrar x -ibck -p'+ password + ' ' + file
                os.system(cmd)
                os.remove(file)
                print('done '+file)


def rmfiles(src_path, file_name):
    li = os.listdir(src_path)
    for subpath in li:
        subpath = src_path + '\\' + subpath
        try:
            if os.path.isdir(subpath):
                os.chdir(subpath)
                file_li = os.listdir(subpath)
                for file in file_li:
                    if file == file_name:
                        os.remove("./"+file)
                        print("remove" + subpath)
                    elif file.split(".")[-1] == file_name:
                        os.remove("./"+file)
                        print("remove" + subpath)
        except:
            print("无该类型文件")


def rename(src_path, character):
    if os.path.isdir(src_path):
        os.chdir(src_path)
        li = os.listdir("./")
        for file in li:
            new_name = file.split(character)[-1]
            os.rename("./" + file, new_name)
            print("rename " + file)


def rename2(src_path):
    if os.path.isdir(src_path):
        os.chdir(src_path)
        li = os.listdir("./")
        for file in li:
            if file[0] != '【':
                os.rename("./"+file, "s"+file)
                print("rename" + file)


def rename3(src_path):
    if os.path.isdir(src_path):
        os.chdir(src_path)
        li = os.listdir("./")
        for i in range(0, len(li)):
            os.rename("./"+li[i], str(i)+"." + li[i].split(".")[-1])


"""
按照数字排序文件夹中的文件
"""


def rename_num(src_path, num):
    if os.path.isdir(src_path):
        os.chdir(src_path)
        li = os.listdir(src_path)
        i = num
        for file in li:
            kzname = file.split(".")[-1]
            dest = str(i) + "." + kzname
            try:
                os.rename(file, dest)
            except:
                print("异常！！")
            i = i + 1
            print("rename successful:", dest)


def rename_dir_num(src):
    path = os.listdir(src)
    i = 0
    for dir in path:
        dir = src + "\\" + dir
        rename_num(dir, 0)


def main():
    rename_num(R"",0)


if __name__ == '__main__':
    main()
