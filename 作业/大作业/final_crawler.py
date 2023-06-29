import requests
from selenium import webdriver
from dm_pb2 import DmSegMobileReply
from google.protobuf.json_format import MessageToJson, Parse
from selenium.webdriver.common.by import By
from time import sleep
import json


class bili_dm_crawler:
    def __init__(self, bro):
        self.bro = bro
        self.se = requests.Session()

    def login(self):
        bro.get('https://www.bilibili.com/')
        sleep(2)
        bro.find_element_by_class_name("header-login-entry").click()
        sleep(2)
        # account = input("输入B站账号:")
        # passwords = input("输入B站账号密码:")
        bro.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[3]/div[2]/div[1]/input').send_keys(
            'youraccountID')
        sleep(2)
        bro.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[3]/div[2]/div[2]/div[1]/input').send_keys(
            'yourpassword')
        sleep(2)
        bro.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[3]/div[3]/div[2]').click()
        bro.delete_all_cookies()  # 先删除cookies
        # 手动操作或者利用超级鹰+动作链自动完成
        sleep(10)
        cookies_dict = bro.get_cookies()  # 读取登录之后浏览器的cookies
        # cookies_json = json.dumps(cookies_dict)  # 将字典数据转成json数据便于保存
        print(cookies_dict)
        for cookie in cookies_dict:
            self.se.cookies.set(cookie['name'], cookie['value'])

    def get_dm(self, url_history, headers):
        response = self.se.get(url_history, headers=headers)
        print(response)
        DM = DmSegMobileReply()
        DM.ParseFromString(response.content)
        original_target_dm = json.loads(MessageToJson(DM))['elems']
        final_dm = []
        for i, item in enumerate(original_target_dm):
            temp = {}
            if item.get('progress', 0) == 0:
                continue
            else:
                temp['content'] = item['content']
                temp['progress'] = item['progress']
            final_dm.append(temp)

        with open(f'dm-' + url_history[-10:] + '.txt', 'w', encoding='utf-8') as fp:
            fp.write(str(final_dm))


if __name__ == '__main__':
    bro = webdriver.Chrome(executable_path=r'./chromedriver.exe')
    craw = bili_dm_crawler(bro)
    craw.login()
    craw.bro.quit()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}
    url_history = 'https://api.bilibili.com/x/v2/dm/web/history/seg.so?type=1&oid=862913601&date=2022-10-17'  # input("输入目标视频的弹幕存储网址:")
    craw.get_dm(url_history, headers)
