from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
import json

bro = webdriver.Chrome(executable_path=r'./chromedriver.exe')
# 打开b站
bro.get(
    'https://www.bilibili.com/video/BV1Yh411o7Sz/?p=77&spm_id_from=333.1007.top_right_bar_window_history.content.click&vd_source=763026b3fd930918486c9b0c9858abdc')
sleep(2)

# 关掉弹幕
bro.find_element(By.CLASS_NAME, 'bui-danmaku-switch-input').click()
sleep(2)

# 点击登陆
bro.find_element(By.XPATH, '//*[@id="biliMainHeader"]/div/div/ul[2]/li[1]/li/div/div').click()

# 切换进账号输入界面,将xxx 和 yyy 改成你的账号和密码
sleep(5)
bro.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div[3]/div[2]/div[1]/input').send_keys('15720938396')
bro.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div[3]/div[2]/div[2]/div[1]/input').send_keys('liu2947107208~')
bro.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div[3]/div[3]/div[2]').click()

bro.delete_all_cookies()  # 先删除cookies

# 60秒时间留你进行登陆
sleep(60)
dictcookies = bro.get_cookies()  # 读取登录之后浏览器的cookies
jsoncookies = json.dumps(dictcookies)  # 将字典数据转成json数据便于保存

# 生成cookies.txt文件
with open('cookies.txt', 'w') as f:  # 写进文本保存
    f.write(jsoncookies)
print('cookies is ok')
