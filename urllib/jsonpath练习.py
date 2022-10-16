import jsonpath
import json

obj = json.load(open('./source/json测试文件.json', 'r', encoding='utf8'))

# print(obj)

author_list = jsonpath.jsonpath(obj, '$.store.book[*].author')
# print(author_list)

all_author_list = jsonpath.jsonpath(obj, '$..author')
# print(all_author_list)

all_elm = jsonpath.jsonpath(obj, '$.store.*')
# print(all_elm)

all_price = jsonpath.jsonpath(obj, '$.store..price')
# print(all_price)

third_book = jsonpath.jsonpath(obj, '$..book[2]')
# print(third_book)

last_book = jsonpath.jsonpath(obj, '$..book[(@.length-1)]')
# print(last_book)

two_book = jsonpath.jsonpath(obj,'$..book[0,1]')
# print(two_book)

two_book_2 = jsonpath.jsonpath(obj,'$..book[:2]')
# print(two_book_2)

book_list_isbn = jsonpath.jsonpath(obj, '$..book[?(@.isbn)]')
# print(book_list_isbn)

book_price_10 = jsonpath.jsonpath(obj, '$..book[?(@.price>10)]')
print(book_price_10)
