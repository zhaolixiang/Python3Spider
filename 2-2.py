from selenium import  webdriver
import aiohttp

browser=webdriver.PhantomJS()
browser.get('https://www.baidu.com')
print(browser.current_url)