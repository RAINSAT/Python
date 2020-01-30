# coding:utf-8

import requests
import re

class UrlRefactor(object):
    def __init__(self):
        self.page_source = None

    def get_html(self, url, encoding='utf-8'):
        """
        获得网页源码
        :param url: 网页url
        :param encoding: 编码
        :return: none
        """
        response = requests.get(url)
        response.encoding = encoding
        self.page_source = response.text

    def get_navigator(self):
        """
        获得网页内所有 ul>li 并将内容返回
        :return: dict
        """
        if  self.page_source is not None:
            ul_content = re.findall("<ul(.+?)</ul>",self.page_source, re.S)
            content = dict()
            for ul in ul_content:
                url = self.__parse_url(ul)
                for item in url:
                    content[item[1]] = item[0]
            return content

    def __parse_url(self,s):
        reg = re.compile("<a.+?href=\".+?\">.+?</a>",re.S)
        url_list = reg.findall(s)
        ret = []
        for url in url_list:
            eve = re.search("href=\"(.+?)\".*?>(.+?)</a>", url, re.S)
            if eve is not None:
                ret.append((eve.group(1), eve.group(2)))
        return ret

    @staticmethod
    def get_html_m3u8(htm):
        return re.search('(https?|ftp|file)://([-A-Za-z0-9+&@#/%?=~_|!:,.;]|[^\x00-\xff])+[-A-Za-z0-9+&@#/%=~_|]', htm,
                         re.S).group(0)

def main():
    browser = UrlRefactor()
    browser.get_html("")
    # print(browser.page_source)
    s = UrlRefactor.get_html_m3u8(browser.page_source)
    print(s)