#coding:utf-8
from requests import get


class M3u8:
    def __init__(self, name, indexUrl, head):
        self.__FileName = name
        self.__m3u8IndexUrl = indexUrl
        self.__head = head
    # 读取本地下载后的m3u8文件
    def read(self,path):
        li = []
        try:
            with open(path,"r") as f:
                s = f.readline(200)
                while 1:
                    if len(s) != 0:
                        li.append(s)
                    else:
                        break
                    s = f.readline(200)
            f.close()
        except:
            print("打开文件异常：{0}".format(__file__))
            f.close()
        return li
    #获取视频的index.m3u8文件
    def get_File_m3u8(self):
        try:
            response = get(self.__m3u8IndexUrl, self.__head).text
            if len(response) != 0:
                with open("./index.m3u8", "w") as f:
                    f.write(response)
                    f.close()
                print("index.m3u8文件下载成功")
            else:
                print("文件下载失败")

        except:
            print("发生异常：{0}".format(__file__))
    #获取密钥
    def get_File_key(self,keyurl):
        try:
            response = get(keyurl, self.__head).text
            if len(response) != 0:
                with open("./key.key", "w") as f:
                    f.write(response)
                    f.close()
                print("key.key文件下载成功")
            else:
                print("文件下载失败")

        except:
            print("发生异常：{0}".format(__file__))

    #解析index文件
    def parse_index(self,indexList):
        li = []
        if len(indexList) != 0:
            for index in indexList:
                if str(index).startswith('#'):
                    continue
                else:
                    #去掉结尾的“\n"
                    index = str(index).split("\n")[0]
                    li.append(index)
        else:
            print("列表为空！")
        return li

    @staticmethod
    def ToLocalLinkFile(localpath):
        with open("list.m3u8","w") as fp:
            with open("./index.m3u8","r") as f:
                s = f.readline(200)
                while 1:
                    if len(s) != 0:
                        if s[0] == "#":
                            fp.write(s)
                        else:
                            s = localpath + "/" + s
                            str(s).replace("\n","\r\n")
                            fp.write(s)
                            print(s)
                    else:
                        break
                    s = f.readline(200)
            print("格式化完成")
            f.close()
        fp.close()

