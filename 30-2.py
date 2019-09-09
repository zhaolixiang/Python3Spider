from pyquery import PyQuery as pq
import requests

html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''
doc = pq(html)

items=doc('.list')
print(type(items))
print(items)

lis=items.find('li')
print(type(lis))
print(lis)

print('*'*30)

lis=items.children()
print(type(lis))
print(lis)

lis=items.children('.active')
print(lis)

container=items.parent()
print(type(container))
print(container)

print('-'*30)

items=doc('.list')
parents=items.parents()
print(type(parents))
print(parents)

print('*'*30)
parent=items.parents('.wrap')
print(parent)

print('-'*30)

li=doc('.list .item-0.active')
print(li.siblings())

print('-'*30)

print(li.siblings('.active'))

print('*'*30)

li=doc('.item-0.active')
print(li)
print(str(li))

lis=doc('li').items()
print(type(lis))
for li in lis:
    print(li,type(li))

print('*'*30)

a=doc('.item-0.active a')
print(a,type(a))
print(a.attr('href'))

print('*'*30)

a=doc('a')
print(a,type(a))
print(a.attr('href'))
print(a.attr.href)

print('-'*30)

a=doc('a')

for item in a.items():
    print(item.attr.href)


a=doc('.item-0.active a')
print(a)
print(a.text())
print(a.html())

print('-'*30)

li=doc('li')
print(li.html())
print(li.text())
print(type(li.text()))


print('-'*30)

li=doc('.item-0.active')
print(li)
li.remove_class('active')
print(li)
li.add_class('active')
print(li)

print('*'*30)

li=doc('.item-0.active')
print(li)
li.attr('name','link')
print(li)
li.text('change item')
print(li)
li.html('<span>mark</span>')
print(li)


