from selenium import webdriver
from selenium.webdriver.common.by import By
path = "msedgedriver.exe"

browser = webdriver.Edge(path)

url = 'https://www.baidu.com/'
browser.get(url)


# 元素定位

# button = browser.find_element(By.ID,'su')
# print(button)

# button = browser.find_element(By.NAME, 'wd')
# print(button)

# button = browser.find_elements(By.XPATH, '//input[@id="su"]')
# print(button)

# button = browser.find_elements(By.TAG_NAME, value='input')
# print(button)

# button = browser.find_elements(By.CSS_SELECTOR, '#su')
# print(button)

button = browser.find_elements(By.LINK_TEXT,'新闻')
print(button)
