import requests

url = 'http://baidu.com/s?'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49'
}

data = {
    'wd': '北京'
}

response = requests.get(url=url, params=data, headers=headers)

content = response.text

print(content)
