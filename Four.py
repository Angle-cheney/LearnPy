
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
'''
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
'''
stu=Student('李四',20,100)
tea=Teacher('李四',20,10)

stu.info()
tea.info()
'''
stude = Student('jack',22,1)
tea = Teacher('Tom',12,22)
stude.info()
tea.info()

class A(object):
	pass

class B(object):
	pass

class C(A,B):
	pass