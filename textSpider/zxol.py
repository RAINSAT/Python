# -*- coding:UTF-8 -*-

import requests
import os
import sys
import chardet
import re
import codecs
from lxml import etree
import pymysql

# def parserCodeFromHtml(url):
#    print(sys.getfilesystemencoding())
#    print('html code:',chardet.detect(getHtml(url)))

def getHtml(url):
    # 请求头信息
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}
    
    # 请求
    html = requests.get(url,headers =header)
    
    # 1.print(html.encoding) ISO-8859-1 apperent_encoding:gb2312
    # html = html.content.decode("ISO-8859-1","ignore").encode("gb2312","ignore")
    
    #指定编码格式
    html.encoding = 'gb2312'
    
    return html.text,html.status_code

def writeToFile(t,name):
    file = name +'.txt'
    if os.path.exists(file):
        print("已存在..")
    else:
        with codecs.open(file,'a+',encoding ='gb2312') as f:
            f.write(str(t))
            f.close()

def spider(sub):
    toUrl = sub[0]
    toTitle = sub[1]
    #构造url
    spiderUrl = 'http://www.zxol.net'+toUrl
    #保存路径
    path = './'+toTitle
    if not os.path.exists(path):
        os.mkdir(path)
    while True:
        # 请求网页
        secHtml,statecode = getHtml(spiderUrl)
        if statecode != 200:
            break
        #writeToFile(secHtml,"sec")
        # 匹配内容 (.+?)</a>.+?class=\"C\">(.+?)</td>
        r = '<tr bgcolor="#FFFFFF">(.+?)</tr>'
        reg = re.compile(r,re.S)
        listInfo= reg.findall(secHtml)
        # 二次匹配
        secr = 'class="L".+?href="(.+?)">(.+?)</a>.+?"C">(.+?)</td>.+?"R">(.+?)</td>.+?"C">(.+?)</td>.+?"C">(.+?)</td>'
        lis = []
        secreg = re.compile(secr,re.S)
        for i in range(0,listInfo.__len__()):
            lis.append(secreg.findall(listInfo[i]))
        # 对结果进行拆包 所有结果都保存在lis在
        for s in range(0,lis.__len__()):
            # 真正的文本下载地址是将 book 替换成 txt
            seUrl = re.search("\d{4,7}",lis[s][0][0]).group() # 有异常存在
            urls = 'http://www.zxol.net/txt/' + seUrl + '.html'
            mysql_insert(urls, # url
                        lis[s][0][1], # name 
                        lis[s][0][2], # author
                        lis[s][0][3], # length
                        lis[s][0][4], # time
                        lis[s][0][5]) # state
        # 更新下一页
        renext = '.*<a href="(.+?)" class="next"'
        nextre = re.compile(renext,re.S)
        nextUrllist = nextre.findall(secHtml)
        spiderUrl = nextUrllist[0]    
    

#执行MySQL插入
def mysql_insert(*arg):
    if arg.__len__() != 6:
        print("error:argument!")
    print(arg[0])
    # 组包
    query = 'insert into zxolxh(name,author,length,time,state,html) values("{0}","{1}","{2}","{3}","{4}","{5}")'.format(arg[1],arg[2],arg[3],arg[4],arg[5],arg[0])
    # 查询
    try:
        cur.execute(query)
        con.commit()
    except:
        print("异常....")
    else:    
        print("插入成功：{0}".format(arg[1]))
    pass

def parser(tx):
    #正则解析
    rex = '<li>.+?href=\"(.+?)\">(.+?)</a></li>'
    regex = re.compile(rex)
    ti = regex.findall(tx)
    title = []
    
    # 找到标题栏
    for i in range(0,11):
        title.append(ti[i])
        
    #进入各标题栏
    for j in range(1,title.__len__()):
        subhtml = title[j]
        # 爬虫进入导航栏
        spider(subhtml)

def mysqlconnect():
    # 连接 MYSQL
    global con
    con = pymysql.connect(host='localhost',user='yuxin',password ='123456',db ='textspiderdatabase',port=3306)
    # 定游标
    global cur 
    cur = con.cursor()
    
def main():
    url = 'http://www.zxol.net'
    html,state = getHtml(url)
    if state == 200:
        mysqlconnect()
        parser(html)


if __name__ == '__main__':
    main()

'''
create table zxolxh(id int primary key auto_increment,
		name varchar(20) not null,
		author varchar(10) not null,
		length varchar(10) not null,
		time varchar(15) not null,
		state varchar(10) not null,
		html varchar(50) not null);
'''
