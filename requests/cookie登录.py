from bs4 import BeautifulSoup
import requests

url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49'
}

response = requests.get(url=url, headers=headers)

content = response.text

# print(content)

# 解析原码


soup = BeautifulSoup(content, 'lxml')

viewstate = soup.select('#__VIEWSTATE')[0].attrs.get('value')
viewstategenerator = soup.select('#__VIEWSTATEGENERATOR')[0].attrs.get('value')

# print(viewstate)
# print(viewstategenerator)

code = soup.select('#imgCode')[0].attrs.get('src')
# print(code)
code_url = 'https://so.gushiwen.cn'+code
# print(code_url)
session = requests.session()
response_code = session.get(code_url)
# 二进制数据
content_code = response_code.content

with open('code.jpg','wb') as fp:
    fp.write(content_code)

# urllib.request.urlretrieve(url=code_url,filename='code.jpg')
code_name = input('请输入你的验证码：')

url_post = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'
data_post = {

    '__VIEWSTATE': viewstate,
    '__VIEWSTATEGENERATOR': viewstategenerator,
    'from': 'http://so.gushiwen.cn/user/collect.aspx',
    'email': '2596943294@qq.com',
    'pwd': 'asdfasdf',
    'code': '',
    'denglu': '登录',
}

response_post = session.post(url=url, headers=headers, data=data_post)
content_post = response_post.text

with open('gushiwenwang.html', 'w', encoding='utf-8')as fp:
    fp.write(content_post)
