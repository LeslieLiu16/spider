# https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20

import urllib.request
import urllib.parse

# url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20'

# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49'
# }

# request = urllib.request.Request(url, headers=headers)

# response = urllib.request.urlopen(request)

# content = response.read().decode('utf-8')


def creat_request(page):

    data = {
        'start': (page-1) * 20,
        'limit': 20

    }
    data = urllib.parse.urlencode(data)
    base_url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&'
    url = base_url + data
    print(url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49'
    }
    request = urllib.request.Request(url, headers=headers)

    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content


def download_(page, content):
    with open('douban' + str(page) + '.json', 'w', encoding='utf-8') as fp:
        fp.write(content)


if __name__ == '__main__':
    start_page = int(input('起始的页码：'))
    end_page = int(input('结束的页码：'))

    for page in range(start_page, end_page+1):
        # print(page)
        request = creat_request(page)
        content = get_content(request)
        download_(page, content)
