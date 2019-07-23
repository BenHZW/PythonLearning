#函数定义与调用
"""
def functionPrint(str):  #定义函数
    "打印传入的在字符" #说明函数作用这句可有可无
    print(str)
    return

functionPrint("正在调用函数")  #调用函数
"""

#参数传递(数字字符元组不可变，字典列表可变)
"""
#1.不可变
def changeInt(a):   #number不可变,只能复制不改变本身
    a = 10
    return a

b = 2
changeInt(b)
print(b)

def changeChar(c):  #字符不可变,只能复制不改变本身
    c = "abcd"
    return c
x = 'a'
changeChar(x)
print(x)


#2.可变
def changeList(myList):
    myList.append([1,2,3,4])
    print("函数内取值:",myList)
    return

mylist = [10,20,30]
changeList(mylist)
print("函数外值:",mylist)
"""

#调用函数，参数顺序可变
"""
def printInfo(name,age):
    print("Name",name)
    print("Age",age)
    return

printInfo(age = 19,name = "jack")
"""

#不定长参数
"""
def printInfo(arg1,*vartuple): # *+参数名存放所有未命名的变量参数
    print(arg1)
    for var in  vartuple:
        print(var)
    return
printInfo(10,20,30,40)
"""

#匿名函数
'''
sum = lambda num1, num2, num3 : num1 + num2 +num3  # lambda 参数1 参数2... : 表达式
print("10 + 20 + 30 =",sum(10,20,30))
'''
