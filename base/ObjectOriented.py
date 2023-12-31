# -*- coding: UTF-8 -*-

# python 面向对象
# 类
class ClassName:
    '类的定义'   #类的文档信息 ，可以通过ClassName.__doc__
    classAttr=1  # 变量是一个类变量，它的值将在这个类的所有实例之间共享。  # class_suite  类体，由类成员，方法，数据属性组成
    def __init__(self,numb1,numb2) : #__init__()方法是一种特殊的方法，被称为类的构造函数或初始化方法，当创建了这个类的实例时就会调用该方法
        self.numb1=numb1
        self.numb2=numb2
        ClassName.classAttr+=1

    def printStr(self) : # self 代表类的实例，self 在定义类的方法时是必须有的，虽然在调用时不必传入相应的参数。
        # print(self)
        print('我是类的一个输出函数')
def commonMethon ():  #类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self。
    print('我是一个普通函数')

#实例化类其他编程语言中一般用关键字 new，但是在 Python 中并没有这个关键字，类的实例化类似函数调用方式。
demo=ClassName(1,2) #使用类的名称 ClassName 来实例化，并通过 __init__ 方法接收参数。
print(demo.classAttr) #使用点号 . 来访问对象的属性。
demo.printStr()

commonMethon()
#添加，删除，修改类的属性
demo.addAttr=1 #添加
print(demo.addAttr)
demo.addAttr=2 #修改
print(demo.addAttr)
del demo.addAttr #删除
# print(demo.addAttr)
#函数的方式来操作属性
print(hasattr(demo,'addAttr'))#hasattr(obj,name) : 检查是否存在一个属性。
setattr(demo,'addAttr',3)#setattr(obj,name,value) : 设置一个属性。如果属性不存在，会创建一个新属性。
print(getattr(demo,'addAttr'))#getattr(obj, name[, default]) : 访问对象的属性。
delattr(demo,'addAttr')#delattr(obj, name) : 删除属性。

setattr(demo,'addAttr',4)
#python 内置类属性
#__dict__ : 类的属性（包含一个字典，由类的数据属性组成）
print(ClassName.__dict__)
# __doc__ :类的文档字符串
print(ClassName.__doc__)
# __name__: 类名
print(ClassName.__name__)
# __module__: 类定义所在的模块（类的全名是'__main__.className'，如果类位于一个导入模块mymod中，那么className.__module__ 等于 mymod）
print(ClassName.__module__)
#__bases__ : 类的所有父类构成元素（包含了一个由所有父类组成的元组）
print(ClassName.__bases__)

#python对象销毁(垃圾回收)
# Python 使用了引用计数这一简单技术来跟踪和回收垃圾。
# 在 Python 内部记录着所有使用中的对象各有多少引用。
# 一个内部跟踪变量，称为一个引用计数器。
# 当对象被创建时， 就创建了一个引用计数，
#  当这个对象不再需要时， 也就是说， 这个对象的引用计数变为0 时， 它被垃圾回收。但是回收不是"立即"的， 由解释器在适当的时机，将垃圾对象占用的内存空间回收。
# a = 40      # 创建对象  <40>
# b = a       # 增加引用， <40> 的计数
# c = [b]     # 增加引用.  <40> 的计数

# del a       # 减少引用 <40> 的计数
# b = 100     # 减少引用 <40> 的计数
# c[0] = -1   # 减少引用 <40> 的计数

# 垃圾回收机制不仅针对引用计数为0的对象，
# 同样也可以处理循环引用的情况。循环引用指的是，
# 两个对象相互引用，但是没有其他变量引用他们。
# 这种情况下，仅使用引用计数是不够的。
# Python 的垃圾收集器实际上是一个引用计数器和一个循环垃圾收集器。作为引用计数的补充，
# 垃圾收集器也会留心被分配的总量很大（即未通过引用计数销毁的那些）的对象。
# 在这种情况下， 解释器会暂停下来， 试图清理所有未引用的循环。


#类的继承
class ClassNameSon(ClassName) :
    '继承‘ClassName’类'  #通过继承创建的新类称为子类或派生类，被继承的类称为基类、父类或超类。
#在python中继承中的一些特点：
# 1、如果在子类中需要父类的构造方法就需要显式的调用父类的构造方法，或者不重写父类的构造方法。详细说明可查看： python 子类继承父类构造函数说明。
# 2、在调用基类的方法时，需要加上基类的类名前缀，且需要带上 self 参数变量。区别在于类中调用普通函数时并不需要带上 self 参数
# 3、Python 总是首先查找对应类型的方法，如果它不能在派生类中找到对应的方法，它才开始到基类中逐个查找。（先在本类中查找调用的方法，找不到才去基类中找）。
# 如果在继承元组中列了一个以上的类，那么它就被称作"多重继承" 。

# 类属性与方法
# 类的私有属性
# __private_attrs：两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问。在类内部的方法中使用时 self.__private_attrs。
# 类的方法
# 在类的内部，使用 def 关键字可以为类定义一个方法，与一般函数定义不同，类方法必须包含参数 self,且为第一个参数
# 类的私有方法
# __private_method：两个下划线开头，声明该方法为私有方法，不能在类的外部调用。在类的内部调用 self.__private_methods
    __privateAttr=10
    publicAttr=2
    def __privateMethod():
        print('我是一个私有方法')
    def printPrivateAttr(self):
        print(self.__privateAttr)

demo1=ClassNameSon(3,4)
print(demo1.publicAttr)
demo1.printPrivateAttr()
# demo1.__privateMethod()
# ClassNameSon.__privateMethod()
#Python不允许实例化的类访问私有数据，但你可以使用 object._className__attrName（ 对象名._类名__私有属性名 ）访问属性，
demo1._ClassNameSon__privateAttr

# 单下划线、双下划线、头尾双下划线说明：
# __foo__: 定义的是特殊方法，一般是系统定义名字 ，类似 __init__() 之类的。
# _foo: 以单下划线开头的表示的是 protected 类型的变量，即保护类型只能允许其本身与子类进行访问，不能用于 from module import *
# __foo: 双下划线的表示的是私有类型(private)的变量, 只能是允许这个类本身进行访问了。