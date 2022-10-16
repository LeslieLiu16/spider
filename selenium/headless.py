

# from selenium import webdriver
# from selenium.webdriver.edge.options import Options


# edge_options = Options()
# edge_options.add_argument('--headless')
# edge_options.add_argument('--disable-gpu')

# path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
# edge_options.binary_location = path

# browser = webdriver.Edge(options=edge_options)

# url = 'https://www.baidu.com/'
# browser.get(url)
# browser.save_screenshot("baidu.png")


from selenium import webdriver
from selenium.webdriver.edge.options import Options


def share_browser():
    edge_options = Options()
    edge_options.add_argument('--headless')
    edge_options.add_argument('--disable-gpu')

    path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
    edge_options.binary_location = path

    browser = webdriver.Edge(options=edge_options)
    return browser


browser = share_browser()

url = 'https://www.baidu.com/'
browser.get(url)
browser.save_screenshot('baidu.png')