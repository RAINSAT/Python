# coding: utf-8

import requests
import re
import os


def spider_single_url_pic(url):
    # <img alt="精选长发美少女高清动漫图片壁纸大全" src="https://t1.hddhhn.com/uploads/tu/201812/411/10.jpg">
    # <img alt="黑长直床上妙龄柔美少女低胸裙肤白貌美撩人写真" src="http://t2.hddhhn.com/uploads/tu/201710/9999/b5d9f11e8d.jpg">
    # <a href="313637_6.html">下一页</a>
    response = requests.get(url)
    response.encoding = 'gbk'
    html = response.text
    link = re.search('<img alt=\"(.+?)\" src=\"(.+?)\">', html)
    # 查找下一页
    try:
        next_page = re.search(
            '<li id=\"nl\">.+?\'(.+?)\'.+?</li>', html).group(1)
    except:
        next_page = None
    return link.group(1), link.group(2), next_page


def down_pic(url, name):
    with open(url.split('/')[-1], 'wb') as f:
        f.write(requests.get(url).content)
    print('download success', url)


def main():
    url = 'https://www.2717.com/ent/meinvtupian/2017/236355.html'
    link = spider_single_url_pic(url=url)
    while link[2] is not None:
        down_pic(url=link[1], name=link[0])
        link = spider_single_url_pic(
            url='https://www.2717.com/ent/meinvtupian/2017/' + link[2])


if __name__ == '__main__':
    main()
