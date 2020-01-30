# coding:utf-8

"""
抓取 http://www.6666caiji.com/ 所有资源的 下载地址
"""

# 导入模块

import requests
import os
import re
from lxml import etree


# Tool

class OSHelper(object):
    @staticmethod
    def mkdir(path: str):
        path = path.strip()
        path = path.rstrip("\\")
        is_exists = os.path.exists(path)
        if not is_exists:
            os.makedirs(path)


# 请求
class Request(object):
    def __init__(self, url, header):
        self.url = url
        self.header = header


class NetworkManager(object):

    def __init__(self, request: Request):
        self.request = request
        executable_path = "D:\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe"
        # self.browser = webdriver.PhantomJS(executable_path=executable_path)

    def setRequest(self, request: Request):
        self.request = request

    def get(self):
        """
        进行GET 请求
        :return: 网页源代码 : str
        """
        print("正在请求:" + self.request.url + " ...")
        response = requests.get(self.request.url, headers=self.request.header)
        response.encoding = "utf-8"
        return response.text

    def get_by_phantomjs(self):
        print("正在请求:" + self.request.url + " ...")
        self.browser.get(self.request.url)
        return self.browser.page_source

class Parse(object):
    def __init__(self, content):
        self.content = content

    def parse_navgator(self):
        """
        解析导航栏
        :return: dict
        """
        nav_dict = {}
        reg = "<li><a href=\"(/html/.+?)\">(.+?)</a></li>"
        regobj = re.compile(reg, re.S)
        nav_list = regobj.findall(self.content)
        # print(nav_list)
        for item in nav_list:
            nav_dict[item[1]] = item[0]
        return nav_dict

    def parse_subpage_content(self):
        """
        解析子页面
        :return: dict
        """
        print("开始解析...")
        subpage_content = {}
        reg = "<li class=\"name\"><a href=\"(/html/.+?)\" target.+?>(.+?)</a></li>"
        regobj= re.compile(reg, re.S | re.M)
        content_list = regobj.findall(self.content)
        for item in content_list:
            subpage_content[item[1]] = item[0]
        # del subpage_content[0]
        return subpage_content

    def find_next_page(self):
        """
        寻找下一页
        :return: str
        """
        print("查找下一页...")
        html = etree.HTML(self.content)
        next_page = html.xpath("/html/body/div[@id='mainbody']/div[@id='hellobox']/div[@class='pager']/a[last()-1]")
        last_page= html.xpath("/html/body/div[@id='mainbody']/div[@id='hellobox']/div[@class='pager']/a[last()]")
        return next_page,last_page

    def find_m3u8(self):
        """
        查找m3u8
        :return: tuple
        """
        try:
            thunder = re.search("<input type=\"text\" id=\"downid\" value=\"(thunder.+?)\">",self.content,re.S | re.M)
            play = re.search("<input type=\"text\" id=\"downid\" value=\"(http://p.+?)\">",self.content,re.S | re.M)
            m3u8 = re.search("<input type=\"text\" id=\"downid\" value=\"(https://.+?m3u8)\">",self.content,re.S | re.M)
            return m3u8.group(1), play.group(1), thunder.group(1)
        except:
            return None

class Application(object):

    @staticmethod
    def main():
        m_url = "http://www.6666caiji.com"
        m_header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                  'Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}
        request = Request(url=m_url, header=m_header)
        manager = NetworkManager(request)
        # 首页 src
        src = manager.get()
        # 解析
        parse = Parse(src)
        nav_dict = parse.parse_navgator()

        url_list = []
        # 对子页面进行遍历
        for item in nav_dict.items():
            subpage = item[1]
            sub_url = m_url + subpage
            url_list.append(sub_url)
            while len(url_list) != 0:
                # 构造请求对象
                request_subpage = Request(url=url_list[0], header=m_header)
                url_list.pop(0)
                # 设置请求
                manager.setRequest(request_subpage)
                # 请求源码
                request_subpage_src= manager.get()
                # 解析源码内容
                parse = Parse(request_subpage_src)
                # 寻找所有的 item
                subpage_list = parse.parse_subpage_content()
                # 遍历这一页所有的item 拿到 m3u8
                for i in subpage_list.items():
                    single_item_url = m_url + i[1]
                    req = Request(url=single_item_url, header=m_header)
                    manager.setRequest(req)
                    # m3u8 网页源码
                    m3u8_src = manager.get()
                    m3_parse = Parse(m3u8_src)
                    address = m3_parse.find_m3u8()
                    if address is not None:
                        with open("./json.txt", "a+", encoding="utf-8") as f:
                            f.write(i[0] + "\n")
                            f.write("m3u8: " + address[0] + "\n")
                            f.write("play: " + address[1] + "\n")
                            f.write("thunder: " + address[2] + "\n")
                            f.write("\n")
                            print("m3u8" + "下载成功" + str(i))

                # 寻找下一页的 url
                next_page_url, last_page_url = parse.find_next_page()
                if next_page_url[0].attrib['href'] == last_page_url[0].attrib['href']:
                    break
                for it in next_page_url:
                    s = it.attrib['href']
                    s_url = m_url + s
                    url_list.append(s_url)



if __name__ == '__main__':
    Application.main()
