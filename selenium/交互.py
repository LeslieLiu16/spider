from selenium import webdriver
from selenium.webdriver.common.by import By
import time
path = "msedgedriver.exe"
browser = webdriver.Edge(path)

url = "https://www.baidu.com/"
browser.get(url)
time.sleep(2)


input_ = browser.find_element(By.ID,'kw')
input_.send_keys('周杰伦')

time.sleep(2)

button = browser.find_element(By.ID,'su')
button.click()

time.sleep(2)

js_bottom = 'document.documentElement.scrollTop=100000'
browser.execute_script(js_bottom)

time.sleep(2)

next_ = browser.find_element(By.XPATH,'//a[@class="n"]')
next_.click()

time.sleep(2)
browser.back()
time.sleep(2)
browser.forward()
time.sleep(2)
browser.quit()


