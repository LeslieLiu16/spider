import requests


url = 'http://www.baidu.com/'

response = requests.get(url)

# 一个类型六个属性
# Response类型
# print(type(response))
# 设置响应的编码格式
# response.encoding = 'utf-8'
# 网页源码
# print(response.text)

# print(response.url)
# 二进制的数据
# print(response.content)
# 状态码
# print(response.status_code)

# 响应头
# print(response.headers)