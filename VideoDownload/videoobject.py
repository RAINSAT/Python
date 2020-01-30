# coding:utf-8
import m3u8
import os
import requests
import timer

global flag
flag = 1

class CallFunc:

    def __call__(self, *args, **kwargs):
        print("下载已超时，退出当前文件下载！")
        global flag
        flag = 0

class VideoObject:
    # 构造函数
    def __init__(self, indexurl, tsurl,tshead, head=""):
        self.__m3u8IObj = m3u8.M3u8("index.m3u8", indexurl,head)
        self.__tsForeUrl = tsurl
        self.__tsHead = tshead

    def ts_downLoad(self, filename):
        global flag
        if not os.path.exists("./index.m3u8"):
            self.__m3u8IObj.get_File_m3u8()
        else:
            li = self.__m3u8IObj.read("index.m3u8")
            index = self.__m3u8IObj.parse_index(li)
        if not os.path.exists(filename):
            os.mkdir(filename)
        os.chdir(filename)
        for si in index:
            id = timer.set_timer(3000, CallFunc())
            ts = self.__tsForeUrl + str(si)
            if flag == 0:
                flag = 1
            while flag == 1:
                res = requests.get(ts,self.__tsHead)
                if res.status_code == 200:
                    with open("{0}".format(si), "wb") as f:
                        f.write(res.content)
                        f.close()
                    print("{0}下载成功".format(si))
                    break
            timer.kill_timer(id)

    def key_download(self,keyurl):
        self.__m3u8IObj.get_File_key(keyurl)
