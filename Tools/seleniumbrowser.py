# -*-coding:utf-8-*-

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class SeleniumBrowser(object):
    def __init__(self,exec_path):
        # 默认的browser位置
        self.executable_path = exec_path
    #接口：获取源码
    def getPageSource(self,pageUrl):
        pass

class SeleniumChrome(SeleniumBrowser):

    def __init__(self,head_model=''):
        super(SeleniumChrome, self).__init__('C:\\Users\\zyxwy\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe')

        if len(head_model)==0: # 指定的是默认的有头模式
            self.driver = webdriver.Chrome(executable_path= self.executable_path)
        else: # 指定为无头模式 headless
            chrome_option = Options()
            chrome_option.add_argument(head_model)
            self.driver = webdriver.Chrome(executable_path=self.executable_path,chrome_options= chrome_option)
        

    def getPageSource(self,pageUrl):
        #chrome_options.add_argument('-disable-gpu')
        self.driver.get(pageUrl)
        self.driver.implicitly_wait(20)
        s = self.driver.page_source
        self.driver.close()
        self.driver.quit()
        return s

class SeleniumPhantomJS(SeleniumBrowser):

    def __init__(self):
        super(SeleniumPhantomJS, self).__init__("D:\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe")
        # 无头
        self.browser = webdriver.PhantomJS(executable_path=self.executable_path)

    def getPageSource(self,pageUrl):
        self.browser.get(pageUrl)
        return self.browser.page_source



if __name__ == '__main__':
    pass