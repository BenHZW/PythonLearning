# del删除单个或多个对象引用
"""
num1 = 1
num2 = 2
print(num1,num2)
del num1,num2
"""

# 常用函数应用
"""
import cmath
import math
import operator
import random


#1.比较两数大小(引入operator,使用operator.lt(x,y))
'''
print(operator.lt(5,10)) #5<10是不是真的
'''

#2.返回给定参数的最大最小值(max(x,y,z,...),min(x,y,z...))
'''
print(max(1,2,3,4,5,6,7,8,9,10))
print(min(1,2,3,4,5,6,7,8,9,10))
'''

#3.算术平方根(引入math,使用math.sqrt())
'''
print(math.sqrt(4))
'''

#4.随机数(引入random)
'''
print(random.choice([1,2,3,4,5,6])) #随机choice(),括号内的一个数字

print(random.uniform(1,10)) #uniform(a,b)，随机a到b内一个实数

print(random.randint(1,100))  #randint(a,b)，随机a到b内一个实数
'''
"""
