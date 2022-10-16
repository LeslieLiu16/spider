import urllib.request
import urllib.parse

# 多个参数的转换

data = {
    'wd': '周杰伦',
    'sex': '男',
    'location': '中国台湾省'
}

data = urllib.parse.urlencode(data)
# print(a)

base_url = 'http://www.baidu.com/s?'

url = base_url + data

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49'
}
request = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
print(content)
