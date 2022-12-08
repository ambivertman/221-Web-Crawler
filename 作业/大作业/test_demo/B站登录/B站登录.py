import requests
import time
import qrcode
import os
from queue import Queue
from threading import Thread

'''
思路：
to do:
1.首先创建一个登录的方法和保存cookies的方法。
2.构造二维码创建的类，其中包含创建方法和显示二维码的方法。
3.构造一个检验是否登录成功的类，如果成功则保存cookies，失败则返回失败原因。
4.构造一个执行登录方法的类，其中包含运行函数和检验函数。

'''


def login_ajax(method, url, data=''):
    '''
    login_ajax():请求url返回json
    method:请求方法,GET返回json,POST返回一个请求对象
    url:网址
    data:post请求参数
    '''
    headers = {
        'Accept': 'application/json',
        "UserAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
        "referer": "https://www.bilibili.com/",
    }
    if method == 'GET':
        return requests.get(url, headers=headers).json()
    else:
        return requests.post(url, headers=headers, data=data)


def save_cookies(headers):
    '''
    save_cookies():保存登录cookies并写入当前目录下的cookies.txt
    headers:返回response的headers,包含cookies
    '''
    with open(os.path.join(os.getcwd(), 'cookies.txt'), 'w', encoding='utf8') as f:
        f.write(headers['set-cookie'])
    return headers['set-cookie']


class Login_Bili_Message:
    ''''
    验证登录信息的类,如果成功则设置cookies并保存在类中
    '''

    def __init__(self):
        # 是否成功设置cookies,成功为True
        self.surces_status = False
        # cookies 存放点
        self.cookies = ''

    def sucess(self, headers):
        print('登录成功')
        cookies = save_cookies(headers)
        self.cookies = cookies
        self.surcess_statue = True

    def failure(self, js):
        if js['data'] == -4:
            print('等待扫描')
        elif js['data'] == -5:
            print('手机已经扫描等待确认')
        elif js['data'] == -2:
            print('二维码超时')
        else:
            print('扫码失败')


class Qrcode_Bili:
    '''
    生成二维码的类
    '''

    def __init__(self):
        # 初始化二维码对象
        self.qr = qrcode.QRCode(
            version=5,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )

    def add_data(self, url):
        """
        add_data():生成二维码图片信息
        url:二维码生成链接地址
        """
        self.qr.add_data(url)

    def show_qr(self):
        self.qr.make(fit=True)
        img = self.qr.make_image()
        filename = 'qrcode_dome1.png'
        img.save(filename)
        print(f'{"*" * 12}扫描后请关闭二维码图片!{"*" * 12}')
        img.show()
        os.remove(filename)


class Bili_Server:

    def __init__(self):
        # 获取二维码地址
        self.getLoginUrl = 'http://passport.bilibili.com/qrcode/getLoginUrl'
        # 验证登录信息
        self.getLoginInfo = "http://passport.bilibili.com/qrcode/getLoginInfo"
        # 初始化登录信息类
        self.lg_ms = Login_Bili_Message()
        # 初始化二维码生成类
        self.qr = Qrcode_Bili()
        # 初始化队列
        self.q = Queue()
        # 初始化检验线程
        self.th = Thread(target=self.check_status)
        # 循环检验信号
        self.lg_status = True

    def check_status(self):
        '''
        check_status():检验登录状态
        '''
        oauthKey = self.q.get(block=True, timeout=15)
        count = 0
        with open('status.txt', 'a', encoding='utf8') as x:
            while self.lg_status:
                response = login_ajax('POST', self.getLoginInfo, data={'oauthKey': oauthKey})
                res_js = response.json()
                x.write(str(res_js))
                try:
                    if res_js['status'] == True:
                        self.lg_ms.sucess(response.headers)
                        self.lg_status = False
                    else:
                        self.lg_ms.failure(res_js)
                        count += 1
                        if count > 1500:
                            time.sleep(4)
                            print('登录超时！')
                            break
                except:
                    print(res_js['message'])

    def run(self):
        '''
        run():执行方法
        '''
        # 请求获取二维码和oauthkey返回json
        ms = login_ajax('GET', self.getLoginUrl)
        # 将oautkey加入队列
        self.q.put(ms['data']['oauthKey'])
        # 生成二维码
        self.qr.add_data(ms['data']['url'])
        # 显示二维码
        self.th.start()
        self.qr.show_qr()
        # 开始检验是否扫码成功

        # 阻塞等待返回信息
        self.th.join()
        # 如果扫码成功
        if self.lg_ms.surces_status == True:
            # 返回cookies
            return str(self.lg_ms.cookies)


if __name__ == '__main__':
    # 实例化
    blserver = Bili_Server()
    # 返回cookies
    co = blserver.run()
    print(co)
