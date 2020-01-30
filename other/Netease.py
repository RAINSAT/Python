 # -*- coding: utf-8 -*-
 # https://www.cnblogs.com/miqi1992/p/8093958.html

import sys
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


class NeteaseMusic:
    def __init__(self,url):
        self.url = url
        self.name = None
    def __str__(self):
        if self.name.strip()=='':
            return self.url
        else:
            return self.name
    
    def getUrl(self):
        # requests send get 
        response = requests.get(self.url)
        print(response.text)

    def seleniumPhantonjsUrl(self):
        # load the phantomjs driver
        phant = webdriver.PhantomJS(executable_path="D:/phantomjs-2.1.1-windows/bin/phantomjs.exe")
        phant.set_window_size(1366,768)
        # use selenium to create a session
        phant.get(self.url)
        # get the name of the music
        self.name=phant.title
        print(self.name)
    
    def seleniumChromeUrl(self):
        option = Options()
        option.add_argument('--headless')
        option.add_argument('--disable-gpu')
        chrome = webdriver.Chrome(chrome_options=option)
        chrome.get(self.url)
        self.name = chrome.title
        #lyricelement = chrome.find_element_by_xpath(r'//div[@data-module="discover"]')
        print(chrome.page_source)
        
        

def main():
    music = NeteaseMusic(r"https://music.163.com/#/song?id=473742028")
    music.seleniumChromeUrl()


if __name__ == "__main__":
    main()