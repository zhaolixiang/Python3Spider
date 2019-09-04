from lxml import etree

html=etree.parse('28-2.html',etree.HTMLParser())
result=etree.tostring(html)
print(result.decode('utf-8'))

