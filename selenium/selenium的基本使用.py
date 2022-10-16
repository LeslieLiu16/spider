from selenium import webdriver

path = 'msedgedriver.exe'

browser = webdriver.Edge(path)

# 访问网站

# url = 'https://www.baidu.com/'

# browser.get(url)

url = 'https://www.bilibili.com/'
browser.get(url)
# content = browser.page_source
