from lxml import etree
import urllib.request

url = 'http://www.baidu.com/'
headers ={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62'
}

request = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
# print(content)

tree = etree.HTML(content)
res = tree.xpath('//input[@id="su"]/@value')[0]

print(res)