#正则表达式

#1.re.match 首字母开始才有效的查找方法
'''
import re
print(re.match("www","www.runoob.com"))  #match需要起始位置匹配模式
print(re.match("www","www.runoob.com").span())  #span返回一个函数起始元组
'''


#2.*核心:re.search查找方法
'''
import re

line = "I am a boy Do you konw that?"
searchObj = re.search("Do",line,re.M)
print(searchObj.span())
searchObj1 = re.search(r"(.*)boy(.*).*",line,re.M)  #r"转义，(.*)代表分组
print("searchObj1.group():",searchObj1.group(0))
print("searchObj1.group():",searchObj1.group(1))
print("searchObj1.group():",searchObj1.group(2))
'''

#3.re.sub替换方法
'''
import re

phone = "135-709-737-38"  #这是一个国内的电话号码
num = re.sub(r"\D","",phone)  #\D匹配任意非数字
print(num)
'''

#4.compile(返回正则表达式对象)和findall(返回匹配列表(需要正则表达式对象))
'''
import re
pattern = re.compile(r'\d+')  #匹配至少一个数字
m = pattern.match('one123two123four123',3,10)
print(m)

pattern1 = re.compile(r"\d+")  #查找数字
result = pattern.findall("abc123 asd123")
print(re.findall(r"\d+","abc123 asd123"))  #同上
print(result)
'''