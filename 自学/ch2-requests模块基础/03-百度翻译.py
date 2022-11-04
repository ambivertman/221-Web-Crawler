import json
import requests

if __name__ == '__main__':
    # UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }
    # 目标站点
    post_url = 'https://fanyi.baidu.com/sug'
    # 进行数据请求
    word = input("Enter a word:")
    data = {
        'kw': word
    }
    response = requests.post(url=post_url, data=data, headers=headers)
    obj_dict = response.json()
    filename = word + '.json'
    fp = open(filename, 'w', encoding='UTF-8')
    json.dump(obj_dict, fp=fp, ensure_ascii=False)

    print('over!!!')
