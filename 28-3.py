from lxml import etree

html=etree.parse('28-2.html',etree.HTMLParser())
result=html.xpath('//*')
print(result)


result=html.xpath('//li')
print(result)
print(result[0])


result=html.xpath('//li/a')
print(result)

result=html.xpath('//ul//a')
print(result)


result=html.xpath('//ul/a')
print(result)

result=html.xpath('//a[@href="link4.html"]/../@class')
print(result)


result=html.xpath('//a[@href="link4.html"]/parent::*/@class')
print(result)

result=html.xpath('//li[@class="item-0"]')
print(result)

result=html.xpath('//li[@class="item-0"]/text()')
print(result)

result=html.xpath('//li[@class="item-0"]/a/text()')
print(result)


result=html.xpath('//li[@class="item-0"]//text()')
print(result)


result=html.xpath('//li/a/@href')
print(result)