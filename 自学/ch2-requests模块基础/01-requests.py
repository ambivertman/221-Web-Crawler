import requests

if __name__ == "__main__":
    # 目标地址
    url = 'https://www.sogou.com/'
    # 发送请求
    response = requests.get(url=url)
    # 获取数据
    page_text = response.text
    print(page_text)
    # 存储数据
    with open('sogou.html', 'w', encoding='utf-8') as fp:
        fp.write(page_text)

    print('爬取结束了!')
