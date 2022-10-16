import urllib.request

url = 'http://www.baidu.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49'
}

request = urllib.request.Request(url, headers=headers)

# handler  build_opener  open
# 获取handler对象
handler = urllib.request.HTTPHandler()
# 通过handler 获取opener对象

opener = urllib.request.build_opener(handler)

# 调用open方法

response = opener.open(request)

content = response.read().decode('utf-8')

print(content)