# coding = utf-8
# 待爬的网址 https://www.biqugex.com/book_67257/23192827.html
# author :zyx 2018-10-4

import requests
import re
import os
import sys


def getHtml(url):
    return requests.get(url)


def writeToFile(htm, filename, code='gbk'):
    with open(filename, 'a') as f:
        # 获取系统编码
        # localcode = sys.getfilesystemencoding()
        # print(htm.encoding) #gbk
        f.write(htm)
        # f.write('\\r\\n')
        f.close()


# 获取标题
def getTextHeader(html):
    reg = "<title>(.+)</title>"
    pattern = re.compile(reg)
    head = re.search(pattern, html.text)
    headgroup = head.group(1).split('_')  # [' 第一章 天黑别出门', '牧神记', '笔趣阁']
    return headgroup[0]


# 获取内容
def getText(html):
    regText = '<div id="content" class="showtxt">(.+)</div>'
    maintext = re.compile(regText)
    event = re.search(maintext, html.text)
    streve = event.group(1)
    # 去掉空格 换行
    regbr = "(&nbsp;)*(.*?)<br />(.+?)>"
    r = re.compile(regbr)
    # txt = re.search(r,streve)
    txt = re.findall(r, streve)
    return txt


# 获取下一章 id

def getNextchapterid(html):
    regid = '(.*)67257/(.*?).html(.*?)下一章</a>'
    idg = re.compile(regid)
    idtext = re.search(idg, html.text)
    return idtext.group(2)

# https://www.52bqg.com/book_101833/32195935.html
def getAlltext(start, end=25555555):
    j = str(start)
    sid = 1
    while j != '0':
        url = "https://www.biqugex.com/book_67257/" + j + ".html"
        html = getHtml(url)
        if html.status_code == 200:
            head = getTextHeader(html)
            txt = getText(html)
            head = head + '.txt'
            for i in range(0, len(txt)):
                writeToFile(txt[i][1] + '\n', head)
            print("第{0}章下载完成".format(sid))
            j = getNextchapterid(html)
            sid = sid + 1
        else:
            print("下载完成")
            break


def main():
    path = os.getcwd()
    path = path + '\\' + 'novel'
    if os.path.exists(path):
        os.chdir(path)
    else:
        os.mkdir(path)
        os.chdir(path)
    getAlltext(23192827)


if __name__ == '__main__':
    main()
