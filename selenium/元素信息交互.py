from selenium import webdriver
from selenium.webdriver.common.by import By

path = "msedgedriver.exe"
browser = webdriver.Edge(path)

url = 'https://www.baidu.com/'
browser.get(url)   



input_ = browser.find_element(By.ID,'su')
print(input_.get_attribute('class'))
print(input_.tag_name)
a = browser.find_element(By.LINK_TEXT,('新闻'))
print(a.text)