from lxml import etree

if __name__ == "__main__":
    tree = etree.parse('test.html')
    r = tree.xpath('/html/head/title')
    r = tree.xpath('/html//div')
    r = tree.xpath('//div')
    # r = tree.xpath('//div[@class="song"]')
    # r = tree.xpath('//div[@class="tang"]//li[5]/a/text()')
    # r = tree.xpath('//li[7]//text()')
    # r = tree.xpath('//div[@class="tang"]//text()')
    # r = tree.xpath('//div[@class="song"]/img/@src')
    r = tree.xpath('//div[@class="tang"]')
    print(r)
