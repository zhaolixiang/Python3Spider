from bs4 import BeautifulSoup

html = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
        </p>
        <p class="story">...</p>
"""

soup=BeautifulSoup(html,'lxml')
print(soup.a.parent)

print('*'*30)

print(type(soup.a.parents))
print(list(enumerate(soup.a.parents)))
