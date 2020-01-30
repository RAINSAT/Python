#-*-  coding:utf-8 -*-
#主要用来测试selenium使用phantomJs

#导入webdriver
from selenium import webdriver
import time

#要想调用键盘按键操作需要引入keys包
from selenium.webdriver.common.keys import Keys

#调用环境变量指定的PhantomJS浏览器创建浏览器对象
driver = webdriver.PhantomJS()
driver.set_window_size(1366, 768)
#如果没有在环境变量指定PhantomJS位置
#driver = webdriver.PhantomJS(executable_path = "./phantomjs")

#get方法会一直等到页面加载，然后才会继续程序，通常测试会在这里选择time.sleep(2)

driver.get("http://www.baidu.com/")

#获取页面名为wraper的id标签的文本内容
data = driver.find_element_by_id('wrapper').text

#打印数据内容
print(data)

print driver.title

#生成页面快照并保存
driver.save_screenshot("baidu.png")

# id="kw"是百度搜索输入框，输入字符串"长城"
driver.find_element_by_id('kw').send_keys(u'长城')

# id="su"是百度搜索按钮，click()是模拟点击
driver.find_element_by_id('su').click()

#获取新的页面快照
driver.save_screenshot("长城.png")

#打印网页渲染后的源代码
print(driver.page_source)

#获取当前页面Cookie
print(driver.get_cookies())

#ctrl+a全选输入框内容
driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'a')
#ctrl+x剪切输入框内容
driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'x')

#输入框重新输入内容
driver.find_element_by_id('kw').send_keys('itcast')

#模拟Enter回车键
driver.find_element_by_id('su').send_keys(Keys.RETURN)
time.sleep(5)

#清空输入框内容
driver.find_element_by_id('kw').clear()

#生成新的页面快照
driver.save_screenshot('itcast.png')

#获取当前url
print(driver.current_url)

driver.quit()

#获取id标签值
element = driver.find_element_by_id("passwd-id")
#获取name值
element = driver.find_element_by_name("user-name")
#获取标签名
element = driver.find_element_by_tag("input")
#也可以通过XPath来匹配
element = driver.find_element_by_xpath(//input[@id="passwd-id"])


#导入ActionChains类
from selenium.webdrive import ActionChains

#鼠标移动到ac位置
ac = driver.find_elenemt_by_xpath('element')
ActionChains(driver).move_to_element(ac).perform()

#在ac位置单击
ac = driver.find_element_by_xpath('elementA')
ActionChains(driver).move_to_element(ac).click(ac).perform()

#在ac位置双击
ac = driver.find_element_by_xpath("elementB")
ActionChains(driver).move_to_element(ac).double_click(ac).perform()

#在ac位置右击
ac = driver.find_element_by_xpath('elementC')
ActionChains(driver).move_to_element(ac).context_click(ac).perform()

#在ac位置左键单击hold住
ac = driver.find_element_by_xpath('elementF')
ActionChains(driver).move_to_element(ac).click_and_hold(ac).perform()

#将ac1拖拽到ac2位置
ac1 = driver.find_element_by_xpath('elementD')
ac2 = driver.find_element_by_xpath('elementE')
ActionChains(driver).drag_and_drop(ac1, ac2).perform()



from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("https://cnblogs.com/")


from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.support.wait import WebDriverWait
if __name__ == "__main__":
options = Options()
options.add_argument('-headless') # 无头参数
driver = Firefox(executable_path='geckodriver', firefox_options=options) # 配了环境变量第一个参数就可以省了，不然传绝对路径
wait = WebDriverWait(driver, timeout=10)
driver.get('http://www.google.com')
wait.until(expected.visibility_of_element_located((By.NAME, 'q'))).send_keys('headless firefox' + Keys.ENTER)
wait.until(expected.visibility_of_element_located((By.CSS_SELECTOR, '#ires a'))).click()
print(driver.page_source)
driver.quit()