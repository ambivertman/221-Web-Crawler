from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import json

web = webdriver.Chrome(executable_path=r'./chromedriver.exe')
web.get(
    'https://www.bilibili.com/video/BV1Yh411o7Sz/?p=77&spm_id_from=333.1007.top_right_bar_window_history.content.click&vd_source=763026b3fd930918486c9b0c9858abdc')
f = open('cookies.txt', 'r')
listcookie = json.loads(f.read())  # 读取文件中的cookies数据
for cookie in listcookie:
    web.add_cookie(cookie)  # 将cookies数据添加到浏览器
web.refresh()  # 刷新网页
