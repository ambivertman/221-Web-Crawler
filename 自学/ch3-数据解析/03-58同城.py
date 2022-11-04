from lxml import etree
import requests

if __name__ == "__main__":
    # url
    url = 'https://bj.58.com/ershoufang/'
    # UA
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }
    # request
    page_text = requests.get(url=url, headers=header).text
    with open("demo.html", 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    # #
    # tree = etree.HTML(page_text)
    # #
    # r = tree.xpath('//')
