from re import U
from urllib import response
import urllib.request

url = 'http://www.baidu.com/'

# 模拟浏览器向服务器发送请求

response = urllib.request.urlopen(url)

# 一个类型和六个方法
# http.client.HTTPResponse
# print(type(response))


# content = response.read().decode('utf-8')
# print(content)

# content = response.read(5)
# # 返回多少个字节
# print(content)

# 读一行
# content = response.readline()
# print(content)

# 读到末尾
# content = response.readlines()
# print(content)

# 返回状态码
print(response.getcode())

print(response.geturl())
# 获取状态信息
print(response.getheaders())
