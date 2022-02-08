
#79.字符串的常见操作_字符串的劈分
'''

split()从左边分开，默认分隔符为空格，返回值是一个列表
--------通过参数sep指定劈分字符串
--------通过maxsplit指定匹配字符串的最大劈分次数
rsplit()从右边开始劈分，默认分隔符为空格，返回值时一个列表
--------通过参数sep指定劈分字符串
--------通过参数maxsplit指定最大劈分次数，

a = 'hello world python'
b = 'hello|world|python'
a1 = a.split()
a2 = a.rsplit()
print(a1)
print(b.split(sep='|',maxsplit=1))
'''

#80.字符串的常见操作_字符串的判断方法
'''
inidentifier()判断指定的字符串是不是合法的标识符
isspace()判断指定的字符串是都全部由空白字符串组成
isalpha()判断指定的字符串是否全部由字母组成
isdecimal()判断指定的字符串是否全部由十进制数字组成
isnumeric()判断指定的字符串是否全部由数字组成
isalnum()判断只当的字符串是否全部由字母和数字组成

print('abd'.isspace())
print('\n'.isspace())
print('Ni21!2'.isalnum())
'''

#81.字符串常见的操作_替换与合并
'''
1.字符串替换：replace()第一个参数指定被替换的子串，第2个参数指定替换子窜的字符串
2.字符串合并：jion()将列表或元组中的字符串合并成一个字符串

a = 'hello,python,PHP'
print(a.replace('python','JAVA'))

b = ['hello','word']
print('@'.join(b))

c = ('hello','python')
print('()'.join(c))

print('@'.join('python'))
'''

#82.字符串的比较操作
'''
运算符：>,<,==,<=,>=,!=
比较规则：比较两个字符串中的第一个字符，如果相等则继续比较下一个字符
比较原理：比较的时ordinal values原始值，

print('apple'>'app')  #true
print('apple'>'banana') #false  beacause97>98
print(ord('a'),ord('b'))
'''

#83.字符串的切片操作
'''
字符串时不可变类型，不具备增删改操作，切片操作将产生新的对象

a = 'hello,python'
a1 = a[:5] #由于没有起始位置，从0开始切
a2 = a[6:] #由于没有结束位置，所有回切到最后位置
a3 = '!'
a4 = a1+a3+a2
print(a4)

print(a[1:5:1]) #从1开始截至到5，不包括5，步长为1
print(a[::2])   #默认从0开始，默认到最后一个元素结束，步长为2，元素之间间隔为2
print(a[::-1])  #默认从字符串最后一个元素开始，到字符串第一个元素结束，因为步长为负数
print(a[6:])   #从索引-6开始，到字符串最后一个元素借宿'''

#84.格式化字符串
'''
为什么需要格式化字符串？
格式化字符串的两种方式
1.%作为占位符   %s:字符串  %i/%d:整数  %f:浮点数
2.{}作为占位符

name = '张三'
age = 20
#1.%作为占位符
print('我叫%s,今年%i' % (name,age))

#2.{}最为占位符
print('我叫{0},今年{1}岁'.format(name,age))
print('{0}{1}'.format(name,age))
print(f'我叫{name},今年{age}岁')

print('%d' % 100)
print('%10i' % 99)     #10表示宽度
print('%.3f' % 3.1415926)    #3表示的时小数点后3位

print('{}'.format(123))
print('{0:.3}'.format(3.1415926))  #.3表示一共三位数
print('{:.3f}'.format(3.1415926))  #3f表示三位小数
print('{:10.3f}'.format(3,1415926)) #同时设置宽度和精度，一共10位，3位时小数
'''

#85.字符串的编码和解码
'''
为什么需要编码转换，字符串再内存中以Unicode表示，编码后通过byte传输，服务器解码给客户端
1.编码：将字符串转换为二进制数据（bytes）
2.解码：将bytes类型的数据转换成字符串类型

s = '西风多少恨'
#编码
print(s.encode(encoding='GBK')) #在GBK编码格式中，一个中文占2个字节
print(s.encode(encoding='UTF-8'))#在UTF-8编码格式中，一个中文占3个字节

#解码,bytes代表一个二进制的数据
bytes=s.encode(encoding='GBK')
print(bytes.decode(encoding='GBK'))

bytes=s.encode(encoding='UTF-8')
print(bytes.decode(encoding='UTF-8'))'''

#86.函数的定义和调用
'''
什么是函数：函数是执行特定任务以完成特定功能的一段代码
为什么需要函数：
1.方便复用
2.隐藏实现细节
3.提高可维护性
4.提高可读性便于调试


#创建函数
def calc(a,b):
	c=a+b
	return c

result=calc(10,20)
print(result)'''


#87.函数调用的参数传递_位置实参_关键书实参
'''
位置实参：根据形参对应的位置进行实参传递
关键字实参：根据形参的名称进行实参传递

def calc(a,b):  #a,b称为形式参数，形参的位置是函数的定义处
	c=a+b
	return c

result=calc(10,20) #10，20称为实际参数值，简称实参，实参的位置是函数的调用处
print(result)

res=calc(b=10,a=20) #左侧的变量名称位关键字参数
print(res)
'''

#88.函数参数传递的内存分析
'''
def fun(arg1,arg2):
	print('arg1',arg1)
	print('arg2',arg2)
	arg1=100
	arg2.append(10)
	print('arg1',arg1)
	print('arg2',arg2)
	
n1=11
n2=[22,33,44]
print('n1',n1)
print('n2',n2)
fun(n1,n2)
#将位置传参，arg1.arg2是函数定义的形参，n1,n2是函数调用处的实参，总结，实参名称与形参名称可以不一致

print('n1',n1)
print('n2',n2)

#在函数调用过程中，进行参数的传递
#如果是不可变对象，在函数修改不会影响实参的值，arg1修改成100,不会影响n1的值
#如果是可变对象，函数修改会影响实参的值，arg2的修改，append(10),会影响到n2的值
'''

#89.函数的返回值
'''
函数返回多个值时，结果为元组

print(bool(0))
print(bool(1))

def fun(num):
	odd=[]  #存奇数
	even=[] #存偶数
	for i in num:
		if i%2:
			odd.append(i)
		else:
			even.append(i)
	return odd,even
lst=[10,29,34,23,44,53,55]
print(fun(lst))

#函数的返回值
	（1）如果函数没有返回值，函数执行完毕后，不需要给调用出提供数据，reture可省略
	（2）函数的返回值，如果时1个，直接返回类型
	（3）函数的返回值，如果时多个，返回的结果为元组

def fun1():
	print('hello')
fun1()

def fun2():
	return 'hello'
res=fun2()
print(res)

def fun3():
	return 'hello','world'
print(fun3())

#函数在定义时，是否需要返回值，视情况而定'''

#90.函数参数定义_默认值参数
'''
函数定义默认值参数：函数定义时，给形参设置默认值，只有与默认值不符的时候，才需要传递实参

def fun(a,b=10):
	print(a,b)
	
#函数的调用
fun(100)
fun(20,30)
'''

#91.函数参数定义_个数可变的位置形参_个数可变的关键字形参
'''
个数可变的位置参数：
-定义函数时，如果无法确认传递位置实参的个数时，可以使用可变的位置参数
-使用*定义个数可变的位置形参
-结果为一个元组
个数可变的关键字形参
-定义函数时呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃
'''