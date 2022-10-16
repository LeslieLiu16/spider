import urllib.request
import json
import jsonpath


url = 'https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1658407318052_104&jsoncallback=jsonp105&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'

headers = {
    'cookie': 't=8e9ba149707867a9358c632d2a700bc0; cna=S+NOG29ODhMCASpbpzYUnsjr; tb_city=110100; tb_cityName="sbG+qQ=="; cookie2=17fdc18e4befac6008279ecc794beeb7; v=0; _tb_token_=4e376dfae6a1; l=eBMgXf0gLWfyRZfWBO5ZPurza77OaQRbz1PzaNbMiInca1-CtF1tlOCHCtHMSdtjgt5fietrJ6F2hd3pyb4LRFsWHpfuKtyuJeJBRe1..; isg=BPPzpc1FlUN4elkZOHH0tvzwgvcdKIfqAAz6oKWSkpJJpBFGLfzUOrB6XtRKA9_i',
    'referer': 'https://dianying.taobao.com/',
    'user-agent': ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62',
    'x-requested-with': ' XMLHttpRequest',
}

request = urllib.request.Request(url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

content = content.split('(')[1].split(')')[0]

# print(content)

with open('./source/淘票票.json','w',encoding='utf-8') as f:
    f.write(content)



obj = json.load(open('./source/淘票票.json','r',encoding='utf-8'))
city_list =jsonpath.jsonpath(obj, '$..regionName')
print(city_list)
