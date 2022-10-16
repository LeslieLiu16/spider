import urllib.request
import urllib.error

# url = 'https://blog.csdn.net/m0_37623374/article/details/1255489774'
url = 'http://www.goudan145.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49'
}

try:
    request = urllib.request.Request(url, headers=headers)

    response = urllib.request.urlopen(request)

    content = response.read().decode('utf-8')

    print(content)

except urllib.error.HTTPError:
    print('HTTP Error')

except urllib.error.URLError:
    print('URLError')