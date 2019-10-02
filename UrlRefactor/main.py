# coding:utf-8

import requests
import re


class UrlRefactor(object):
    def __init__(self):
        self.page_source = None

    def get_html(self, url, encoding='utf-8'):
        response = requests.get(url)
        response.encoding = encoding
        self.page_source = response.text

    def get_navigator(self):
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


def main():
    browser = UrlRefactor()
    browser.get_html("http://www.6666caiji.com/html/vodlist/727.html")
    # print(browser.page_source)
    dic = browser.get_navigator()
    print(dic)

if __name__ == '__main__':
    main()
