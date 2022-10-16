import urllib.request

url = 'https://www.baidu.com'

# url的组成
# 协议 http https
# 主机 baidu.com
# 端口号 http 80 https 443
# 路径  s
# 参数  ？
# 锚点

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49'
}

# 定制请求对象
request = urllib.request.Request(url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)
