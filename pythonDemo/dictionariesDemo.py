#修改字典元素
"""
dict1 = {'a':123,'b':234,1:"abc"}

print(dict1['a'])

dict1['a'] = 2345 #修改键对应的值
print(dict1)
"""

#删除字典元素
"""
dict1 = {'a':123,'b':234,1:"abc"}

del dict1['a'] #删除单一键值
print(dict1)


dict1.clear() #清空所有条目
print(dict1)

del dict1 #删除整个字典
"""

#字典内置函数
"""
dict1 = {'a':123,'b':234,1:"abc"}

print(len(dict1)) #计算键总数

print(dict1.keys()) #返回所有键

print(dict1.values()) #返回所有值

print(dict1.popitem()) #随机返回并删除一对键值
"""
