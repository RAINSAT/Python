# -*- coding: gbk -*-
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="gbk")
# print(response.text.encode("gbk", "ignore").decode("gbk","ignore"))

import requests
import sys
import io
import re
import os


class Kudm(object):
    def __init__(self):
        self.__head = "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)" \
                    " AppleWebKit/537.36 (KHTML, like Gecko) " \
                    "Chrome/71.0.3578.80 Safari/537.36"
        self.__start_url = "http://comic.kukudm.com/comiclist/2335/"
        self.__index = self.get_index();

    def get_index(self):
        indexurl = "http://comic.kukudm.com/comiclist/2335/index.htm"
        txt = requests.get(indexurl,self.__head).text.encode('gbk', 'ignore').decode('gbk', 'ignore')
        pattern = 'http://comic.kukudm.com/comiclist/(.*?)target'
        reg = re.compile(pattern)
        li = reg.findall(txt)
        lis = []
        for l in li:
            index = str(l).split("/")[-2]
            lis.append(index)
        return lis

    def get_html_response(self, num, numChapter):
        start_url = self.__start_url + self.__index[numChapter] + "/" + str(num) + ".htm"
        print(start_url)
        response = requests.get(start_url, self.__head)
        pattern = "<IMG SRC=(.*?)>"
        reg = re.compile(pattern)
        li = reg.findall(response.text.encode('gbk', 'ignore').decode('gbk', 'ignore'))
        if len(li) != 0:
            url = str(li[0])
        else:
            print("list 为空。已到达结尾")
            return -1
        ti = url.split("/")
        host = "http://n5.1whour.com/newkuku/" + ti[-5] + "/" + ti[-4] + "/" + ti[-3] + "/五等分的花嫁"
        if numChapter < 10:
            url = (host + "/第0"+str(numChapter)+"话/" + url.split('/')[-1]).split("'")[0]
        else:
            url = (host + "第"+str(numChapter)+"话/" + url.split('/')[-1]).split("'")[0]
        print(url)
        respon = requests.get(url,self.__head)
        if respon.status_code == 200:
            with open("{0}.jpg".format(num),"wb") as f:
                f.write(respon.content)
                f.close()
                print("写入{0}.jpg成功".format(num))
                return 0
        else:
            print(respon.status_code,"失败！！！")
            return -2


    def download(self, nameDm, numChapter):
        path = './' + nameDm
        if os.path.exists(path):
            os.chdir(path)
        else:
            os.mkdir(path)
            os.chdir(path)
        os.mkdir("./"+str(numChapter) + "话")
        os.chdir("./" + str(numChapter) + "话")

        for i in range(1, 100):
            ret = self.get_html_response(i, numChapter)
            if ret == -1:
                break

def main():
    ku = Kudm()

    ku.download("五等分的花嫁", 19)
    pass


if __name__ == '__main__':
    main()
