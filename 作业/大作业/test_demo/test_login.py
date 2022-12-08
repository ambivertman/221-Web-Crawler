import re
import requests
from time import sleep
from lxml import etree
from selenium import webdriver

# 实例化浏览器对象
bro = webdriver.Chrome(executable_path=r'./chromedriver.exe')
# 发送请求
bro.get('https://www.bilibili.com/')
# 标签定位
# search_input = bro.find_element_by_id('q')
# #标签交互
# search_input.send_keys("iPhone 13")
#
# bro.execute_script("window.scrollTo(0,document.body.scrollHeight)")
btn = bro.find_element_by_class_name("header-login-entry")

btn.click()

sleep(5)

bro.quit()
