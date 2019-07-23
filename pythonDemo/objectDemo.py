#创建类
'''
class Test:
    def prt(self):  #类的方法必须有代表本类实例的参数
        print("这是输出")
        print(self)  #当前对象地址
        print(self.__class__)

t = Test()
t.prt()
'''

#类的调用
'''
class student:  #声明类(__类的私有属性和方法不能被外部访问)
    studentCout = 0

    def __init__(self,name,number):
        self.name = name
        self.number = number
        student.studentCout += 1

    def dispayCount(self):
        print("一共有%d个学生"%(self.studentCout))

    def displayStudent(self):
        print("姓名:",self.name,",学号:",self.number)

student1 = student("jack",1)  #创建实例对象
student2 = student("ben",2)

student2.displayStudent()  #访问属性
student1.displayStudent()
student1.dispayCount()

student1.age = 20  #添加改变删除属性
student1.age = 10
del student1.age
setattr(student2,"age",21)  #添加属性
print(hasattr(student2,"age"))  #检查sutdent1是否存在哦age属性
print(getattr(student2,"age"))  #返回指定类的属性
delattr(student2,"age")  #删除属性
print(hasattr(student2,"age"))
'''

#对象销毁
'''
a = 20
b = a
c = [b]

del  a
del  b
del  c
print(b)
'''

#类的继承
'''
class father:  #定义父类
    fatherAttr = 100
    def __init__(self):
        print("调用父类构造函数")

    def fatherMethod(self):
        print("调用父类方法")

    def setAttr(self,attr):
        father.fatherAttr = attr

    def getAttr(self):
        print("父类属性:",father.fatherAttr)

class Child(father):  #定义子类
    def __init__(self):
        print("调用子类构造方法")
    def childMethod(self):
        print("调用子类方法")

c = Child()
c.childMethod()
c.fatherMethod()
c.setAttr(200)
c.getAttr()
'''

#方法重写
'''
class father:
    def myMethod(self):
        print("调用父类的方法")

class Child(father):
    def myMethod(self):
        print("调用子类的方法")

c = Child()
c.myMethod()
'''

