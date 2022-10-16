import urllib.request

# 下载网页
url_page = 'http://www.baidu.com/'

urllib.request.urlretrieve(url=url_page, filename='baidu.html')
# 下载图片

url_img = 'https://img1.baidu.com/it/u=3217543765,3223180824&fm=253&fmt=auto&app=120&f=JPEG?w=1200&h=750'
urllib.request.urlretrieve(url=url_img, filename='img.jpg',)

# 下载视频
url_video = 'https://vd2.bdstatic.com/mda-ngdybca81uwtqxaf/sc/cae_h264/1657839127511194898/mda-ngdybca81uwtqxaf.mp4?v_from_s=hkapp-haokan-nanjing&amp;auth_key=1657857466-0-0-25b780fac99e83e19230f1d9818f4d1c&amp;bcevod_channel=searchbox_feed&amp;pd=1&amp;cd=0&amp;pt=3&amp;logid=1666288522&amp;vid=9016888792624074570&amp;abtest=103525_2&amp;klogid=1666288522'
urllib.request.urlretrieve(url=url_video, filename = 'video.mp4')