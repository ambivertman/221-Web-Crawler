import requests
from lxml import etree
import re
import time

if __name__ == "__main__":
    url = "https://sc.chinaz.com/jianli/free.html"
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }
    response = requests.get(url=url, headers=header)
    response.encoding = response.apparent_encoding
    page_text = response.text
    # method 1 Regular Expression
    Re = r'<a class="title_wl" target="_blank" href="(.*?.htm)">'
    links = re.findall(Re, page_text, re.S)
    # method 2 xpath
    tree = etree.HTML(page_text)
    names = tree.xpath('//div[@id="main"]//a[@class="title_wl"]/text()')
    page_num = int(tree.xpath('//b/text()')[-1])
'''
    # temp_url = "https:" + links[0]
    # response = requests.get(temp_url,header)
    # response.encoding = response.apparent_encoding
    # temp_page_text = response.text
    # tree = etree.HTML(temp_page_text)
    # r = tree.xpath('//div[@id="down"]/div[2]//a/@href')
    #
    #print(r)
    # temp_Re = r'<a href="(.*?.rar)" target="_blank">'
    # temp_links = re.findall(temp_Re,temp_page_text)
    # print(temp_links)

    for i,link in enumerate(links):
        temp_url = "https:" + link
        response = requests.get(temp_url,header)
        response.encoding = response.apparent_encoding
        page_text = response.text
        tree = etree.HTML(page_text)
        r = tree.xpath('//div[@id="down"]/div[2]//a/@href')
        print(temp_url,names[i])
        time.sleep(1)


    # tree = etree.parse('demo.html')
    # r = tree.xpath()
    # print(r)
'''
