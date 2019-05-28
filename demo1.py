# -*- coding:utf-8 -*-

import requests
from multiprocessing import Pool
import re


class WeiWei(object):
    def __init__(self):
        self.header = {
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'
        }
        self.start_url = ['https://1111.me/category/long-serial']

    def parse(self):
        for url in self.start_url:
            response = requests.get(url, self.header)
            response.encoding = 'utf-8'
            # 解析目录
            mulu = self.__re_find_mulv(response.text)
            # 下载小说
            for novel in mulu:
                self.__download_single_novel(novel[0], novel[1])

    def __re_find_mulv(self, html: str):
        re_match_mulv = '<article>.+?<a href=\"(.+?)\" class="list-group-item">.+?<strong>(.+?)</strong>.+?</article>'
        re_obj = re.compile(re_match_mulv, re.S)
        return re_obj.findall(html)

    def __download_single_novel(self, url, name):
        response = requests.get(url, self.header)
        response.encoding = 'utf-8'
        content = response.text
        paragraph = re.findall('<div class="post-content">(.+?)</div>',
                               content, re.S)
        res = paragraph[0].replace('<br>', '\r\n').replace('&nbsp;', ' ')
        with open('./novel/' + name + '.txt', 'w+', encoding='utf-8') as f:
            f.write(res)
        print(name + '写入成功！')


if __name__ == "__main__":
    # p = Pool(25)
    # for i in range(824):
    #     p.apply_async(down, (i,))

    # p.close()
    # p.join()
    WeiWei().parse()
