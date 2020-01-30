# coding:utf-8

import os

formats = ['jpg', 'png', 'mp4']


def rename_dir(path):
    os.chdir(path)
    file_list = os.listdir('../')
    i = 1
    for item in file_list:
        if os.path.isfile('./'+item):
            kz = item.split('.')[-1]
            if kz.lower() in formats:
                try:
                    if i <= 9:
                        os.rename(item, '00' + str(i) + '.' + kz.lower())
                    elif i >= 10 and i <= 99:
                        os.rename(item, '0' + str(i) + '.' + kz.lower())
                    else:
                        os.rename(item, str(i) + '.' + kz.lower())
                    i = i + 1
                    print(str(i) + kz + " success")
                except:
                    print("文件名已存在")
                    i = i + 1
        elif os.path.isdir('./' + item):
            rename_dir('./' + item)
    os.chdir('../../')


if __name__ == '__main__':
    #s = input("输入路径：")
    #s = s.replace("\\", "\\\\")
    # print(s)
    # while True:
    #     rename_dir(s)
    #     s = input("输入路径：")
    #     s = s.replace("\\", "\\\\")
    s = r"G:\\新建文件夹"
    rename_dir(s)
