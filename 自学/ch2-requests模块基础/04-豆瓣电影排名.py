import requests
import json
import pprint

# 目标站点
url = "https://movie.douban.com/j/chart/top_list"

# UA伪装
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}
# 数据请求
params = {
    'type': '11',
    'interval_id': '100:90',
    'action': ' ',
    'start': "20",
    'limit': '20'
}
response = requests.get(url=url, params=params, headers=header)
response.encoding = response.apparent_encoding
# 数据存储
# 根据抓包工具显示的信息选取合适的数据类型进行存储
list_data = response.json()
f = open("豆瓣电影排名.json", 'w', encoding='utf-8')
json.dump(list_data, fp=f, ensure_ascii=False)
f.close()
print("over!!!")
