from pyquery import PyQuery as pq
import requests

html = '''
<div id="container">
    <ul class="list">
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''
doc = pq(html)
print(doc('li'))


doc = pq(url='http://www.segmentfault.com')
print(doc('title'))


doc=pq(requests.get('http://www.segmentfault.com').text)
print(doc('title'))

doc=pq(filename='30-1.html')
print(doc('li'))

print(doc('#container .list li'))
print(type(doc('#container .list li')))
