
#91.函数参数定义_个数可变的位置形参_个数可变的关键字形参
'''
个数可变的位置参数：
-定义函数时，如果无法确认传递位置实参的个数时，可以使用可变的位置参数
-使用*定义个数可变的位置形参
-结果为一个元组
个数可变的关键字
-
'''


#92.函数的参数总结
'''
def fun(a,b,c):
	print('a=',a)
	print('b=',b)
	print('c=',c)
#函数的调用
fun(10,20,30) #函数调用时的参数传递，称为位置传参
lst=[11,22,33]
fun(*lst) #在函数调用是，将列表中的每个元素都转换为位置实参传入
fun(a=100,b=300,c=400)
dic={'a':111,'b':222,'c':333} #函数的调用，所以是关键字传参
fun(**dic) #函调用时，将字典中的键值对都转换为关键字传参

def fun(a,b=10): #b时在函数定义处，所以b时形参，而且进行了赋值，所以b称为默认值传参
	print('a=', a)
	print('b=', b)

def fun2(*args): #个数可变的位置形参
	print(args)
	
def fun3(**args2): #个数可变的关键字传参
	print(args2)
	
fun2(10,20,30,40)
fun3(a=11,b=22,c=33,d=44,e=55)

def fun4(a,b,c,d):
	print('a=',a)
	print('b=',b)
	print('c=',c)
	print('d=',d)
fun4(10,20,30,40)   #位置实参传递
fun4(a=10,b=20,c=30,d=40) #关键字实参传递
fun4(10,20,c=30,d=30)  #前零个参数，位置实参传递，而b,c时关键字传参

#需求：c,d只能采用关键字实参传递
'''

#93.变量的作用域
'''
1.程序代码能访问该变量的区域
2.根据变量的有效范围可分为
（1）局部变量：在函数定义并使用的变量，只在函数内部有效，可使用global声明，就会成为全局变量
（2）全局变量：函数体外定义的变量，可作用与函数内外

def fun(a,b):
	c=a+b #c就称为局部变量，因为C时函数体内部定义的变量，a,b为函数形参，作用范围也是函数内部
	print(c)
#print(c) #因为a,c超出了起作用的范围
#print(a)


name = 'jack' #name作用范围为函数内部和外部，称为全局变量
print(name)
def fun1():
	print(name)
fun1()

def fun2():
	global age #函数内部定义的变量，局部变量，可使用global声明，这个变量就变成了全局变量
	age =20
	print(age)
fun2()
#print(age)
'''

#94.递归函数
'''
什么是递归函数：如果在一个函数的函数体内部调用了该函数本身，就称之为递归函数
组成部分：递归调用与递 归终止条件
调用过程：每递归调用一次，都会在栈内分配一个栈帧
		 每执行一次，都会释放相应的空间
优点：思路和代码简单
缺点：占用内存多，效率地下

#利用递归计算阶乘

def fac(n):
	if n==1:
		return 1
	else:
		return n*fac(n-1)
print(fac(6))
'''

#96.斐波那契数列
'''
def fib(n):
	if n== 1:
		return 1
	elif n==2:
		return 2
	else:
		return fib(n-1)+fib(n-2)
#斐波那契数列第6位上的数字
print(fib(6))

#输出这个数列的前6位上的数字
for i in range(1,7):
	print(fib(i))
	
age = input('请输入你的年龄：')
print(type(age))
if int(age)>=18:
	print('成年人')
else:
	print('未成年人')

#BUG
# lst=[1,2,34,5] #列表的索引是从0开始的
# print(lst[3])

# ls=[]
# #ls.append('a','b','b')
# ls.append('a')
# ls.append('b')

# print(ls)
'''
#101.python异常处理机制
'''
#python提供了异常处理机制，可以在异常出现的时候，即时捕获，让程序继续执行
try:
	n=int(input('请输入第一个整数'))
	m=int(input('请输入第二个整数'))
	result = n/m
	print('结果位：',result)
except ZeroDivisionError:
	print('对不起，除数不允许为0')
print('程序结束')'''


#101.Pythn异常处理机制
'''
1.try...except...else结构
如果try块没有抛出异常，则执行else块，如果抛出异常，则执行except块
try:
	n=int(input('请输入第一个整数'))
	m=int(input('请输入第二个整数'))
	result=n/m
except BaseException as e:
	print('出错了',e)
else:
	print('结果为',result)
	
2.try...except...else...finally结构
finally不管是否发生异常都会执行，常用来释放try块中申请的资源
'''
'''
try:
	n=int(input('请输入第一个整数'))
	m=int(input('请输入第二个整数'))
	result=n/m
except BaseException as e:
	print('出错了',e)
else:
	print('结果为',result)
finally:
	print('thank very much！')
'''
#102.Pythn常见的异常类型
'''
#1.ZeroDivisionError:除零
print(10/0)
#2.IndexError：序列中没有次索引
li=[1,2,3]
print(li[9])
#3.KeyError：映射中没有这个键
dic={'name':'jack'}
print(dic['Home'])
#4.NameError：未声明
print(num)
#5.SyntaxErrorPytoh语法错误
int a=20
#6.ValueError传入无效的参数
a=int('hello')
print(a)'''

#103.traceback模块的使用，用来打印异常信息
'''
import traceback
try:
	print('---------')
	print(10/0)
except:
	traceback.print_exc()
'''
#104.pycharm的调试
'''
i=1
while i<10:
	print(i)
'''

#105.编程的两个思想——面向过程，面向对象
'''
面向过程：事物比较简单，可以用线性思维去解决
面向对象：事物比较复杂，无法用线性思维去解决
共同点：都是解决实际问题的一种思维方式

'''
#106.类与对象
'''
类时多个类似事物组成的群体总称，能够帮助与我们快速理解和判断事物的性质
'''

#107.python定义类，创建类
'''
class Student: #可以由一个或者多个单词组成，规范要求，第一个字母大写
	pass
#python中一切皆对象，student时对象吗？由内存空间吗？
print(id(Student))
print(type(Student))
print(Student)

类的组成：
类属性/实例方法/静态方法/类方法

class Student:
	def __init__(self,name,age):
		self.name=name
		self.age=age#selef.name为实体属性，进行一个赋值操作，将局部变量name值赋给实体属性
	native_pace='吉林' #直接写在类里的变量，称之为属性
	#实例方法
	def eat(self):
		print('学生正在吃饭：')
		
	#静态方法--不允许写self
	@staticmethod
	def method():
		print('我使用了staticmethod进行修饰，所以我是静态方法')
		
	#类方法
	@classmethod
	def cm(cls):
		print('我是类方法，因为使用了classmethod进行修饰')
		
	#
#在类之外定义的时函数，在类之内定义的时方法
def drick():
	print('喝水')'''
#108.对象的创建
'''
语法：实例名=类名()

class Student: #类对象
	def __init__(self,name,age):
		self.name=name
		self.age=age#selef.name
	
	def eat(self):
		print('学生在吃饭')
#创建Student类对象
stu1=Student('张三',20) #实例对象
print(id(stu1))
print(type(stu1))
print(stu1)

print('-----------')

print(id(Student))
print(type(Student))
print(Student)

#创建Student类对象
stu1.eat()
print(stu1.name)

print('------------')
Student.eat(stu1)
class Student 类对象
	def age 实例方法
stu = Student() 类的实例对象
'''
#109.类属性_类方法_静态方法的使用
'''
类属性：类中方法的变量，称为类属性
类方法：使用@classmethod修饰的方法，使用类名直接访问的方法
静态方法：使用@staticmethod修饰的方法，使用类名直接访问的方法
'''

'''
class Student:  # 类对象
	def __init__(self, name, age):
		self.name = name
		self.age = age  # selef.name
	pice = 'Aisa'
	
	def eat(self): #实例方法
		print('学生在吃饭')
	
	@staticmethod
	def method():
		print('我使用了staticmethod进行修饰，所以我是静态方法')
	
	# 类方法
	@classmethod
	def cm(cls):
		print('我是类方法，因为使用了classmethod进行修饰')


# 创建Student类对象
stu1 = Student('张三', 20)  # 实例对象
print(id(stu1))

#类属性的使用方式
print(Student.pice)
stu1 = Student('张三', 20)
stu2 = Student('李四', 10)
Student.pice='Erouch'
print(stu1.pice)
print(stu2.pice)
print('------类方法的使用方式-------')
Student.cm()
print('----------静态方法的使用方式--------------')
Student.method()
'''
#110.动态绑定属性和方法
'''
#一个类可以创建多个类的实例对象，每个实例对象的属性值不同
class Student:
	def __init__(self,name,age):
		self.name=name
		self.age=age
	def eat(self):
		print(self.name+'在吃饭')
		
stu1 = Student('张三',49)
stu2 = Student('李四',30)

print('----------stu2动态绑定性别属性---------')

stu2.sex='女'
stu1.sex='男'
print(stu1.name,stu1.age,stu1.sex)
print(stu2.name,stu2.age,stu2.sex)

print('----------stu1动态绑定方法-------------')

stu1.eat()
stu2.eat()

def show():
	print('定义在类之外的函数')
stu1.show=show
stu1.show()
#没有绑定类之外的函数，所以无法调用stu2.show()
'''

#111.面向对象的三大特征：封装/继承/多态
'''
封装：提高程序的安全性
继承：提高程序的复用性
多态：提高程序的扩展性
'''
'''
class Car:
	def __init__(self,brand):
		self.brand=brand
	def start(self):
		print('汽车已启动！')
car=Car('帕萨特')
car.start()
print(car.brand)'''
'''
class Student:
	def __init__(self,name,age):
		self.name = name
		self.__age = age #年龄不希望在类的外部使用，所以加了--
	def show(self):
		print(self.name,self.__age)
		
stu=Student('张三',20)
#在类的内部使用
stu.show()
#在类的外部使用
print(stu.name)
#print(stu.__age)
print(dir(stu))
print(stu._Student__age)#在类的外部可以使用_Student__age进行访问
'''
#112.继承及其实现方式

'''
1.语法格式：class 子类类名（父类1，父类2）：pass
2.如果一个类没有继承任何类，则默认继承object
3.python支持多继承
4.定义子类时，必须在其构造函数中调用父类的构造函数

class Person(object):
	def __init__(self,name,age):
		self.name = name
		self.age = age
	def info(self):
		print(self.name,self.age)
		
class Student(Person):
	def __init__(self,name,age,stuno):
		super().__init__(name,age)
		self.stu_no=stuno

		
class Teacher(Student):
	def __init__(self,name,age,teacherfyear):
		super().__init__(name,age)
		self.teacherfyear=teacherfyear

stu=Student('李四',20,100)
tea=Teacher('李四',20,10)

stu.info()
tea.info()

stude = Student('jack',22,1)
tea = Teacher('Tom',12,22)
stude.info()
tea.info()

class A(object):
	pass

class B(object):
	pass

class C(A,B):
	pass'''
#113.方法重写
'''
1.如果子类对继承自父类的某个属性或方法不满意，可以在子类中对其进行重新编写
2.子类重写后的方法中可以通过super().xxx()调用父类中被重写的方法
class Person(object):
	def __init__(self, name, age):
		self.name = name
		self.age = age
	
	def info(self):
		print(self.name, self.age)


class Student(Person):
	def __init__(self, name, age, stuno):
		super().__init__(name, age)
		self.stu_no = stuno
	def info(self):
		super().info()
		print(self.stuno)


class Teacher(Student):
	def __init__(self, name, age, teacherfyear):
		super().__init__(name,age)
		self.teacherfyear = teacherfyear


stu = Student('李四', 20, 100)
tea = Teacher('李四', 20, 10)

stu.info()
print('---------------')
tea.info()'''
#114.OBJECT类
'''
1.object类时所以类的父类，因此所以类都有object类的属性和方法
2.内置函数dir（）可以查看指定对象所有的属性
3.object有一个__str__()方法，用于返回一个对于对象的描述，对于内置函数str()经常用于print()方法
帮我们查看对象的信息，所以我们经常会对__str__()进行重写

class Student:
	def __init__(self,name,age):
		self.name=name
		self.age=age
		
	def __str__(self):
		return '我的名字是{0}，今年{1}岁'.format(self.name,self.age)

stu=Student('张三',20)
print(dir(stu))
print(stu)   #默认会调用__str__方法
print(type(stu))'''

#115.多态的实现
'''
简单来说，就是：具备多种形态，指的是：即便不知道一个变量所引用的对象到底是什么类型，
仍然可以通过这个变量调用方法吗，在运行过程中，根据变量引用对象的类型，动态决定调用哪个对象的方法

静态语言和动态语言
class Animal(object):
	def eat(self):
		print('动物会吃')
class Dog(object):
	def eat(self):
		print('狗吃骨头')
class Cat(Animal):
	def eat(self):
		print('猫吃鱼')
		
class Person:
	def eat(self):
		print('人吃五谷杂粮')
		
#定义一个函数
def fun(obj):
	obj.eat()
	
#开始调用
fun(Cat())
fun(Dog())
fun(Animal())
fun(Person())
'''

#116.特殊属性和特殊方法
'''
特殊属性：__dict__获得类对象或实例对象锁绑定所以属性和方法的字典
特殊方法：
__len__通过重写，让内置函数len()参数可以是自定义类型
__add__通过重写，可使用自定义对象具有+给你
__new__用于创建对象
__init__对创建对象进行初始化
class A:
	pass
class B:
	pass
class C(A,B):
	def __init__(self,name,age):
		self.name = name
		self.age = age
#创建C类对象
x=C('jack',20)
print(x.__dict__)  #实例对象的属性字典
print(C.__dict__)

print(x.__class__)  #输出对象所属的类
print(C.__bases__)  #C类的父类类型的元素
print(C.__base__)   #
print(C.__mro__)    #类的层次结构
print(C.__subclasses__())'''

#117.特殊方法
'''
a=20
b=30
c=a+b #两个整数类型相加操作
d=a.__add__(b)

print(c)
print(d)

class Student:
	def __init__(self,name):
		self.name = name
	def __add__(self, other):
		return self.name+other.name
	def __len__(self):
		return len(self.name)

stu1=Student('dddd')
stu2=Student('李四')

s=stu1+stu2 #实现两个对象加法运算__add__
print(s)
print('-----------------')
lst=[11,22,33]
print(len(lst))  #len是内置函数，输出对象长度，
print(lst.__len__())
print(len(stu1))
'''

#118.__new__与__init__演示创建对象的过程
'''
class Person(object):
	def __init__(self,name,age):
		self.name = name
		self.age = age
		
	def __new__(cls, *args, **kwargs):
		print('__new__被调用执行了，cls的id值为{0}'.format(id(cls)))
		super().__new__(cls)
		obj=super().__new__(cls)
		print('创建的对象id为：{0}'.format(id(obj)))
		return obj

	def __init__(self,name,age):
		print('__init__被调用了，self的id值为：{0}'.format(id(self)))
		self.name =name
		self.age = age

print('object这个类对象的id为:{0}'.format(id(object)))
print('Person这个类对象的id为:{0}'.format(id(Person)))

#创建Person类的实例对象
p1=Person('张三',20)
print('p1这个Person类的实例对象的id:{0}'.format(id(p1)))
'''

#119.类的赋值和拷贝
'''
变量赋值操作：只是形参两个变量，实际桑还是指向同一个对象
浅拷贝：Python一般是浅拷贝，拷贝是对象包含子对象内容不拷贝马，因此，源对象与拷贝对象会引用同一个子对象
深拷贝：使用copy模块的deepcopy函数，递归拷贝对象中包含子对象，源对象和拷贝对象所以的子对象也不相同

class CPU:
	pass
class Disk:
	pass
class Cpmputer:
	def __init__(self,CPU,Disk):
		self.CPU=CPU
		self.Disk=Disk
#1.变的赋值
cpu1=CPU()
cpu2=cpu1
print(cpu1,id(cpu1))
print(cpu2,id(cpu2))
#2.类有浅拷贝
dick=Disk()  #创建一个硬盘类的对象
computer=Cpmputer(cpu1,dick)  #创建一个计算机类的对象

#浅拷贝
import copy
computer2=copy.copy(computer)
print(computer,computer.CPU,computer.Disk)
print(computer2,computer2.CPU,computer.Disk)
'''

#120.深拷贝
'''
浅拷贝，只拷贝id
深拷贝，全部拷贝
class CPU:
	pass
class Disk:
	pass
class Cpmputer:
	def __init__(self,CPU,Disk):
		self.CPU=CPU
		self.Disk=Disk
#1.变的赋值
cpu1=CPU()
cpu2=cpu1
print(cpu1,id(cpu1))
print(cpu2,id(cpu2))
#2.类有浅拷贝
dick=Disk()  #创建一个硬盘类的对象
computer=Cpmputer(cpu1,dick)  #创建一个计算机类的对象

#浅拷贝
print('-----浅拷贝-----')
import copy
computer2=copy.copy(computer)
print(computer,computer.CPU,computer.Disk)
print(computer2,computer2.CPU,computer.Disk)

#深拷贝
print('-----深拷贝-----')
computer3=copy.deepcopy(computer)
print(computer,computer.CPU,computer.Disk)
print(computer3,computer3.CPU,computer3.Disk)'''
