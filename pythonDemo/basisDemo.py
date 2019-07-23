#输入输出
"""
from pip._vendor.distlib.compat import raw_input

#变量直接赋值
c = raw_input("按下enter可返回\n")
print (c)
"""

#多变量赋值
"""
a,b,c = 1,2,"jo"

print(a,b)
"""

#简介字符串
"""
a = "abcdefg"

print(a[0])
print(a[1:3]) #包含头下标，尾下标-1
print(a[0:])
print(a[-7:])
print(a * 2) #输出两次
print(a + "Test") #加后面连接符
"""

#简介列表
"""
#可复合元组列表字典等(可二次赋值)
line = ['a',1,['a',"abc",2],'d','e']

print(line[0:4:2])
print(line[0:2])
print(line[0:])
print(line[-5:])
print(line * 2) #列表内容重复两次组成新的列表
print(line + ['a','b']) #两列表内容相加组成新的列表

line[1] = 'a'#列表允许更新数据
print(line[1])
"""

#简介元组
"""
#可复合元组列表字典等(不可二次赋值)
tuple = ("runoob",123,2.2,"john")

print(tuple[0])
print(tuple[0:])
print(tuple[-4:])
print(tuple * 2)   #元组内容重复形成新元组
print(tuple + ("joker",12))  #两元组内容拼接形成新元组

#元组不允许更新内容
#tuple[0] = 100
#print(tuple)
"""

#简介字典
"""
#可复合字典元组列表等(可二次赋值)
#demo1
dict = {}
dict['1'] = "This is one"
dict["two"] = "This is two"
print(dict)

#demo2
dictDemo = {1:"jack",2:"lily",3:"kg"}

print(dictDemo)
print(dictDemo[1])
print (dictDemo.keys())
print(dictDemo.values())

dictDemo[1] = "test" #字典允许二次赋值
print(dictDemo)
"""

#运算符号
'''
#1.算术运算符
"""
a = 10
b = 20

c = a % b # %为取模,取余数
print("c的值为:",c)

d = a ** b # **为x的y次幂
print("d的值为:",d)

e = a //b # //为整除
print("e的值为:",e)

print(a / b) #python2.x整数除以整数还是整数，3.x会自动转换浮点数
"""

#2.比较运算符
"""
a = 10
b = 20

print("a等于b吗?",a == b ) # == 类似还有>=,<=,!=都是返回true和False
"""

#3.逻辑运算符
"""
a = 10
b = 20

print("a and b的值为:",a and b) #a为False返回False，否则返回b
print("a or b的值为:",a or b)  #a为非0返回a，否则返回b
print("not a的值为:",not a)
"""

#4.成员运算符
"""
a = 10
b = 20
list1 = [1,2,3,4,5,6]
list2 = [10,20,30,40]

print("a在list1中吗？",a in list1) #在指定队列中是否找到a
print("b在list2中吗?",b in list2)
print("a不在list1中吗?",a not in list1)
print("b不在list2中吗?",a not in list2)
"""

#5.身份运算符
"""
a = [1,2,3]
b = a[:]
c = a

print("a的内存地址:",id(a))
print("b的内存地址:",id(b))
print("c的内存地址:",id(c))
print("a跟b引用自同一对象吗?",a is b) #判断标志符是否两值相等地址也相等
print("a跟c不是引用同一对象吗？",a is not c)
print("a跟c引用自同一对象吗?",a is c)
"""

'''