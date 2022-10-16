import urllib.request
import random

url = 'http://www.baidu.com/s?&wd=ip'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49'
}

proxies_pool = [
    {'http':'47.106.105.236:70'},
    {'http':'47.106.105.236:80'},
    ]

proxies = random.choice(proxies_pool)

request = urllib.request.Request(url, headers=headers)

# response = urllib.request.urlopen(request)

handler = urllib.request.ProxyHandler(proxies=proxies)

opener = urllib.request.build_opener(handler)

response = opener.open(request)

content = response.read().decode('utf-8')

with open('daili.html', 'w', encoding='utf-8') as fp:
    fp.write(content)
