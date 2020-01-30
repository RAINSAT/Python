# -*- coding:utf8 -*-

import os


def read_dir(startpath):
    if os.path.exists(startpath):
        subpath = os.listdir(startpath)
        return subpath

# def rename_file(subpath,startpath):
# 	for i in range(len(subpath)):
# 		spath = startpath + '/' + subpath[i]
# 		if os.path.exists(spath):
# 			if os.path.isfile(spath):
# 				# 判断文件后缀
# 				if str(subpath[i]).split('.')[-1] == 'jpg':
# 					#os.rename(spath,)
# 			elif os.path.isdir(spath):
# 				print(2)
# 				pass


def rename(src):
    os.chdir(src)
    li = os.listdir('./')
    i = 0
    for item in li:
        try:
            os.rename("./"+item, "./"+str(i)+".jpg")
            i = i + 1
        except Exception as e:
            i = i + 1
        finally:
            print(item + "rename success")


def main():
    startpath = ""
    spath = read_dir(startpath)
    # rename_file(spath, startpath)


if __name__ == '__main__':
    rename(r'E:\Users\Pictures\Saved Pictures\Weibo\weibo')
