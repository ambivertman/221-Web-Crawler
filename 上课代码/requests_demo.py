import requests

r = requests.get("http://www.baidu.com")
print(r.status_code)
r.encoding = r.apparent_encoding
#
with open('baidu_index.html', 'w', encoding='utf-8') as fp:
    r.text.encode('iso-8859-1').decode('gbk')
    fp.write(r.text)

print(len(r.text))
