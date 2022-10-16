# http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname
# cname: 兰州
# pid:
# pageIndex: 1
# pageSize: 10


import urllib.request
import urllib.parse
# base_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'


def creat_request(page):
    '''Creates ashx'''
    base_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
    data = {
        'cname': '兰州',
        'pid': '',
        'pageIndex': page,
        'pageSize': '10',
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49'
    }
    data = urllib.parse.urlencode(data).encode('utf-8')
    request = urllib.request.Request(url=base_url, data=data, headers=headers)
    return request


def get_content(request):
    '''get_content'''
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content


def download_(page, content):
    '''download'''
    with open('kfc_'+str(page)+'.json', 'w', encoding='utf-8') as fp:
        fp.write(content)


if __name__ == '__main__':
    start_page = int(input('请输入起始页：'))
    end_page = int(input('请输入结束页：'))

    for page in range(start_page, end_page+1):
        # print(page)
        request = creat_request(page)

        content = get_content(request)

        download_(page, content)
