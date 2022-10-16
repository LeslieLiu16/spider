
import urllib.request
import urllib.parse
import json

url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'
headers = {
    'Accept': '*/*',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Acs-Token': '1657868408768_1657892149304_l0nld04ZaX22RejqGPuOGBeQd7nlWR1f0T+ujzDsRV6TtlDFMpPRyZfKxSk2Zr/m7O717GSQ2KldBOT6WHYlPeDCSI2SZaxTl6se0Gir87xR0cMjwUXCjij2yIY7IaHOzHCLWpN6b+s+WRTD/puMfI/8v+mXdnMs/AldPmW2lQZoGMpq8TYL4Sk08Y4mqMutkpNKUNMlbpYVmdI63aaw9EMsvgyIcKz/ENh7lzxbtv8CTDS7T7E93RKNgRNJX0Q0b3vLQ2ZMcjInWXSCT+cFVdIAdsWgxie+aImE/O85pB0WzGimA7PB34WCPE9uP1JLfar/QOaX7ABKQALrvKOzSw==',
    'Connection': 'keep-alive',
    'Content-Length': '116',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'BIDUPSID=D1F5C054400B766F6EF2769F6705F878; PSTM=1655432314; BAIDUID=D1F5C054400B766FF883889402668EC5:SL=0:NR=10:FG=1; BDUSS=FhbThsVUVNMlNNVk5vQVpwalNuR3JSMFJ0akpwOEkwRTZCfjZmUjBpa0FKZHBpRVFBQUFBJCQAAAAAAAAAAAEAAACNabc4x6fK1tb5vORsAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACYsmIAmLJiZ2; BDUSS_BFESS=FhbThsVUVNMlNNVk5vQVpwalNuR3JSMFJ0akpwOEkwRTZCfjZmUjBpa0FKZHBpRVFBQUFBJCQAAAAAAAAAAAEAAACNabc4x6fK1tb5vORsAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACYsmIAmLJiZ2; av1_switch_v3=0; RT="z=1&dm=baidu.com&si=o0e2ysqi94&ss=l5lwgj9x&sl=1&tt=107&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=22m&ul=ihp&hd=iip"; BDRCVFR[brmhvwvKpQR]=mk3SLVN4HKm; delPer=0; PSINO=1; BA_HECTOR=8g0k0la50l8005al2k82gnir1hd2mfr17; ZFY=OKo0nMHtmRGopsdf0RuCZ2jMqCVsprH6cFfcEcOfRzk:C; APPGUIDE_10_0_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1657891120; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=36545_36466_36820_36454_36414_36453_36691_36167_36816_36772_36746_36762_36771_36765_26350; BAIDUID_BFESS=C847194DD11116F8E6EBDD5A426A626B:FG=1; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1657892149',
    'DNT': '1',
    'Host': 'fanyi.baidu.com',
    'Origin': 'https://fanyi.baidu.com',
    'Referer': 'https://fanyi.baidu.com/',
    'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49',
    'X-Requested-With': 'XMLHttpRequest',
}
data = {
    'from': 'en',
    'to':'zh',
    'query':'love',
    'simple_means_flag': '3',
    'sign': '198772.518981',
    'token': '14ac6c021f8079b43e4f9a11ae6da149',
    'domain': 'common'
}

data = urllib.parse.urlencode(data).encode('utf-8')

request = urllib.request.Request(url, data, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)
obj = json.loads(content)
print(obj)