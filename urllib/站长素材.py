import urllib.request
from lxml import etree


base_url = 'https://sc.chinaz.com/tupian/bangongrenwu.html'

headers ={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62'
}

def creat_request(page):
    if (page == 1):
        url = 'https://sc.chinaz.com/tupian/bangongrenwu.html'
    else:
        url = 'https://sc.chinaz.com/tupian/bangongrenwu_'+str(page)+'.html'
    
    # print(url)
    headers ={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62'
    }

    request = urllib.request.Request(url, headers=headers)

    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')

    return content


def down_load(content):

    # urllib.request.urlretrieve()
    tree = etree.HTML(content)

    name_list = tree.xpath('//div[@id="container"]//a/img/@alt')

    # for name in name_list:
    #     print(name)
    src_list = tree.xpath('//div[@id="container"]//a/img/@src')
    # print(len(name_list),len(src_list))
    for i in range(len(name_list)):
        name = name_list[i]
        src = src_list[i]
        # print(name,src)
        url = 'https:'+src
        # print(name, url)
        urllib.request.urlretrieve(url=url, filename = './下载/'+name+'.jpg')
    

if __name__ == '__main__':
    
    start = int(input('请输入起始页码：'))
    end = int(input('请输入结束页码：'))

    for page in range(start, end+1):
        # print(page)   
        request = creat_request(page)
        
        content = get_content(request)

        down_load(content)

