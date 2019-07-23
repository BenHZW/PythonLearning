#字符串的访问(字符串不允许单个更新)
"""
char = "Hello world!"

print(char[2:7])
"""

#字符串拼接
"""
char = "Hello world"
newChar = char[:6] + "change"

print("新的字符串为:",newChar)
"""

#字符串索引
"""
char = "Hello world"
print(char[-11:]) #从左到右完整显示
print(char[:-1]) #从右到左缺失一个
print(char[:10]) #从右到左缺失一个
print(char[0:]) #从左到右完整显示
"""

#转义字符
"""
print("aaa\
aaaaa") # \续行

print("a\\abc") #输出反斜杠
print("b\'ac") #输出反引号(双引号一样)
"""

#字符运算
"""
char = "abcdefg"
print('a'in char)
print(r'/n') #r'原始字符串'
"""

#核心*****字符串格式化
"""
print("这是一个%s的字符串，还可以包含数字%d"%("格式化，",10)) #%s %d格式化
print("网站:{name},地址:{url}".format(name = "百度",url = "http://www.baidu.com")) #formate格式化
print("这是一个{aa}的字符串，还可以包含数字{bb}".format(aa = "格式化",bb = "100"))
"""

#三引号
"""
print( '''hi #三引号可同时单双,可输出隔行
there''')
"""

#创建一个Unicode
"""
print(u"Hello\u0020World")
"""

#字符串内建函数
"""
str = "this is a sentence"

print(str.capitalize()) # .capitalize()把字符串第一个字母大写
print(str.count('s',0,)) #返回s[0-] 出现的次数
print(str.find("en",0,)) #查询是否找到，如果查到返回开始索引，否则返回-1
"""