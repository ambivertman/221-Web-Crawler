import requests

if __name__ == "__main__":
    # 指定目标
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }
    url = 'https://sogou.com/web?'
    # 发送请求
    kw = input('Enter a keyword:')
    param = {
        'query': kw
    }

    response = requests.get(url=url, params=param, headers=headers)
    # 获取数据
    page_text = response.text
    # 存储数据
    filename = kw + '.html'
    with open(filename, 'w', encoding='UTF-8') as fp:
        fp.write(page_text)
    print(f"{filename} 保存成功")
