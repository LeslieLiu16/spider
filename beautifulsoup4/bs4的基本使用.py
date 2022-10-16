from bs4 import BeautifulSoup

# 解析本地文件

soup = BeautifulSoup(open('../source/bs4解析.html',encoding='utf-8'),'lxml')
# print(soup)
# 找到的是第一个符合条件的数据
# print(soup.a)
# 获取标签的属性和属性值
# print(soup.a.attrs)

# bs4 的一些函数

# find
# 返回的是第一个符合条件的数据

# print(soup.find('a'))
# print(soup.find('a',title='a2'))
# 根据class_的值找到对象
# print(soup.find('a',class_='ab'))


# find_all
# 添加的是列表的数据
# print(soup.find_all(['a','span']))
# selecte
# 查找前几个数据
# print(soup.find_all('li',limit=2))

# selecte
# 返回的是多个数据
# print(soup.select('a'))
# 可以通过.表示class
# print(soup.select('.ab'))
# 可以通过#，表示id
# print(soup.select('#l1'))


# 属性选择器
# li标签中有id的
# print(soup.select('li[id]'))

# li标签中id为l2的
# print(soup.select('li[id="l2"]'))

# 层级选择器
# 后代选择器
# div下的li
# print(soup.select('div li'))

# 子代选择器 第一级子标签
# print(soup.select('div>ul>li'))

# 找到a标签和li标签的所有对象
# print(soup.select('a,li'))


# 节点信息
# 获取节点内容

# obj = soup.select('#d1')[0]
# 如果标签中只有内容，都可以使用
# 如果除了内容还有标签，只能用get_text
# print(obj.string)
# print(obj.get_text())

# 节点属性

# obj = soup.select('#p1')[0]
# name是标签的名字
# print(obj.name)
# 将属性值作为一个字典返回
# print(obj.attrs)

# 获取节点的属性
obj = soup.select('#p1')[0]
print(obj.attrs.get('class'))
print(obj.get('class'))
print(obj['class'])