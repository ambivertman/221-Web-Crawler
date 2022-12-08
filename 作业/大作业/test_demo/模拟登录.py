from time import sleep
from selenium import webdriver
from lxml import etree

# #实例化浏览器对象
# bro = webdriver.Chrome(executable_path=r'./chromedriver.exe')
# bro.get('https://www.bilibili.com/')
#
# #模拟登录
# login_btn = bro.find_element_by_class_name(".header-login-entry")
#
# login_btn.click()
# #输入账号密码
# r = etree.xpath('//div[@class="bili-mini-account"]/input')
#
# account_input = bro.find_element_by_xpath(r)
# account_input.send_keys("15720938396")
#
# sleep(5)
