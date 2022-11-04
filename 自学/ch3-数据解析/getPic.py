import requests
import re

if __name__ == "__main__":
    # 指定url
    url = 'https://bz.zzzmh.cn/index#classify'
    # UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }
    # 发起请求
    html_data = requests.get(url=url, headers=headers).txt()
    print()
    # 持久存储
    with open('./qiutu_logo.jpg', 'w', encoding='utf-8') as fp:
        fp.write()
    print("Over!!!")
