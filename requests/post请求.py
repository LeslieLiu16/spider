

import json
import requests

url = 'https://fanyi.baidu.com/sug'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49'
}

data = {
    'kw': 'eye'
}

response = requests.post(url=url, data=data, headers=headers)

content = response.text


obj = json.loads(content)
print(obj)
