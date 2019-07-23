#更新列表
"""
list = ['a','b',123]
list.append('newChange')
print(list)
"""

#删除列表元素
"""
list = ['a',"jack",1995,2000]
print(list)
del list[0] #删除元素
print(list)
"""

#列表函数
"""
import operator
list1 = [1,2,3]
list2 = [4,2,5,7,6,8,9]
tuple = (1,2,3,4,5)

print(operator.lt(list1,list2)) #类似字符串比较
print(max(list1,list2)) #返回最大列

print(list(tuple)) #把元组转化成列

print(list1.count(2)) #统计某元素出现次数

list1.insert(1,'xx') #在某个位置插入新元素
print(list1)

list1.reverse() #元素反向
print(list1)

list2.sort()
print(list2)
"""

