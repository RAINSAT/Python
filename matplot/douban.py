# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import re

url = 'https://movie.douban.com/chart'


def crawl():
    response = requests.get(url)
    # print(response.text)
    soup = BeautifulSoup(response.text, 'html.parser')
    s = soup.find_all(name='a', attrs='nbg', recursive=True)
    regImg = re.compile(r'src="(.*?)"\s')
    regtitle = re.compile('title="(.*?)">')
    for i in range(0, len(s)):
        ss = str(s[i])
        img = regImg.search(ss).group(1)
        title = regtitle.search(ss).group(1)
        title = title + '.jpg'
        image = Image.open(BytesIO(requests.get(img).content))
        image.save(title)


def main():
    crawl()


if __name__ == '__main__':
    main()
