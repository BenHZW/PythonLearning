#if
"""
#if else跟c一样
a = 10
if a == 1:
    print("这是1")
elif a == 2:
    print("这是2")
elif a == 3:
    print("这是3")
elif a == 4:
    print("这是4")
else:
    print("搜索失败")
"""

#while
"""
#while跟c语言中的一样直至条件为假退出循环

#while..else(可省略else)
count = 0
while count < 5:
    print(count,"小于5继续执行")
    count = count + 1
print("大于5退出循环")
"""

#for
"""
#for...in....
print("------------for...in...------------------")
for letter in "Python":
    if letter != 'n':
        print("当前字母为:",letter)
    else:
        print("当前字母为:",letter)
        print("\n")

names = ["jo","jack","Lily"]
for name in names:
    print("当前姓名为:",name)
print("结束\n")

#for的迭代
print("----------迭代------------------")
fruits = ['banana', 'apple', 'mango']
print(len(fruits))
print(range(len(fruits))) #0到3不包含3
for index in range(len(fruits)):
    print ('当前水果 :', fruits[index])
print("结束\n")

#for...in + else
print("----------for...in + else-------------")
for num in range(10,20):
    for i in range(2,num):
        if num % i == 0:
            j = num / i
            print("%d 等于 %d * %d" %(num,i,j))
            break
    else:
         print(num,"是一个质数")
"""

#break
"""
for i in "python":
    print("这是",i)
    if i == 'o':
        print("遇到o结束遍历")
        break;
"""

#continue
"""
for letter in "python":
    if letter == 't':
        continue
    print("这是:",letter)
"""

#pass
"""
#pass一般不做任何事情只占位
for letter in "python":
    if letter == 'o':
        pass
        print('已经到达o')
    print('当前字母为:',letter)
print("遍历结束")
"""