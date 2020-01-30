# coding : utf-8

import requests
import re


class Dhmyg(object):

    def __init__(self, url):
        self.__url = url

    def get_source_html(self):
        header = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
        }
        try:
            res = requests.get(self.__url, headers=header, timeout=15)
            return res.text
        except:
            return ""


class DownloadPipeLine(object):
    def __init__(self, pic_url):
        self.__pic_url = pic_url

    def download(self):
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
        }
        # param = [("max-age",3600)]
        try:
            res = requests.get(url=self.__pic_url, headers=header, timeout=15)
            return res.content
        except:
            return ""

    @staticmethod
    def save(bytes, file_path):
        with open(file_path, "wb+") as f:
            f.write(bytes)
        print(file_path + " save success...")

    @staticmethod
    def get_file_name(item: str):
        name = item.split('/')[-1]
        return name.split('?')[0]


class ParseSource(object):
    def __init__(self, src):
        self.__src = src

    def parse_url(self):
        reg = "<img class=\"img\".+?data-src=\"(https://.+?3600)\"/>"
        regobj = re.compile(pattern=reg)
        url_list = regobj.findall(self.__src)
        return url_list


if __name__ == '__main__':
    my = Dhmyg("https://dhmyg.com/25")
    text = my.get_source_html()
    # print(text)

    parse = ParseSource(text)
    url_list = parse.parse_url()
    # print(url_list)

    for item in url_list:
        Down = DownloadPipeLine(item)
        response = Down.download()
        if response != "":
            file = DownloadPipeLine.get_file_name(item)
            DownloadPipeLine.save(bytes=response, file_path="./" + file)
