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
        self.url = url_history

    def login(self):
        self.bro.get('https://www.bilibili.com/')
        sleep(2)
        login_btn = self.bro.find_element_by_class_name('.header-login-entry')
        sleep(2)
        login_btn.click()
        account = input("输入B站账号:")
        passwords = input("输入B站账号密码:")
        self.bro.find_element(By.XPATH, '/html/body/div[11]/div/div[2]/div[3]/div[2]/div[1]/input').sent_keys(account)
        self.bro.find_element(By.XPATH, '/html/body/div[11]/div/div[2]/div[3]/div[2]/div[2]/div[1]/input').sent_keys(
            passwords)
        self.bro.find_element_by_class_name('.universal-btn login-btn').click()
        bro.delete_all_cookies()  # 先删除cookies
        # 手动操作或者利用超级鹰+动作链自动完成
        sleep(60)
        cookies_dict = bro.get_cookies()  # 读取登录之后浏览器的cookies
        cookies_dict = bro.get_cookies()  # 读取登录之后浏览器的cookies
        # cookies_json = json.dumps(cookies_dict)  # 将字典数据转成json数据便于保存
        se = requests.Session()
        for cookie in cookies_dict:
            se.cookies.set(cookie['name'], cookie['value'])

        return se

    def get_dm(url_history, se):
        response = se.get(url_history)
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
                temp['progress'] = temp['progress']
            final_dm.append(temp)

        with open(f'dm-' + url_history[-10:] + '.txt', 'w', encoding='utf-8') as fp:
            fp.write(str(final_dm))


if __name__ == '__main__':
    bro = bro = webdriver.Chrome(executable_path=r'./chromedriver.exe')
    craw = bili_dm_crawler(bro)
    se = craw.login()
    url_history = input("输入目标视频的弹幕存储网址:")
    craw.get_dm(url_history, se)
