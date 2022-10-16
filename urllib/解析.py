from lxml import etree

# xpath 解析

# 本地文件

# 服务器相应文件 response.read().decode('utf-8')
tree = etree.parse(source='./source/解析.html')

# print(tree)

# 查找ul下的li
# //子孙节点  /子节点
li_list = tree.xpath('//body/ul/li')
print(li_list)
print(len(li_list))

# 查找所有具有id属性的li标签
# text()获取标签中的内容
li_list_id = tree.xpath('//ul/li[@id]/text()')
print(li_list_id)

# 查找id为l1的标签 注意引号
li_list_id_l1 = tree.xpath('//ul/li[@id="l1"]/text()')
print(li_list_id_l1)

# 查找id为l1的li标签的class的属性值

li = tree.xpath('//ul/li[@id="l1"]/@class')
print(li)

#模糊查询
# 查询id里面包含l的li标签

li_list_mohu = tree.xpath('//ul/li[contains(@id,"l")]/text()')
print(li_list_mohu)

# 查找id以l开头的li标签

li_list_mohu_2 = tree.xpath('//ul/li[starts-with(@id,"c")]/text()')
print(li_list_mohu_2)

# 查找id为l1和class的标签

li_list_and = tree.xpath('//ul/li[@id="l1" and @class = "c1"]/text()')
print(li_list_and)

li_list_or = tree.xpath('//ul/li[@id="l1" or @id = "c3"]/text()')
print(li_list_or)