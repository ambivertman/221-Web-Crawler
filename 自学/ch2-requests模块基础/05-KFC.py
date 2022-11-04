import requests
import json
import time

# 目标站点
url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'

# UA伪装
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}

# 数据请求
i = 1
while True:
    print(f"capturing page {i}")
    params = {
        'cname': '',
        'pid': '',
        'keyword': '南昌',
        'pageIndex': str(i),
        'pageSize': '10',
    }

    response = requests.post(url=url, params=params, headers=header)
    data = response.json()
    flag = int(data['Table'][0]['rowcount'])
    i += 1
    time.sleep(3)
    f = open("KFC餐厅信息.json", 'a', encoding='utf-8')
    json.dump(data, fp=f, ensure_ascii=False)
    f.close()
    if i > (flag / 10) + 1:
        break

# 数据存储


print("over!!!")
