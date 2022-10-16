import urllib.request
import urllib.parse
import json

url = 'http://fanyi.baidu.com/sug'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49'
}

data = {
    'kw': 'spider'
}

# post请求参数必须进行编码

data = urllib.parse.urlencode(data).encode('utf-8')

# print(data)
request = urllib.request.Request(url=url, data=data, headers=headers)
# print(request)

response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')

print(content)
obj = json.loads(content)
print(obj)
