#转义字符
print('hello \nworld') #换行
print('hello \tworld')
print('hello\rwoeld') #world将hello进行覆盖
print('hello\bworld') #\b是退一个格

#二进制和字符编码
print(chr(0b100111001011000))
print(ord('乘'))

#标识符和保留字
import keyword
print(keyword.kwlist)

#变量的定义和使用
name = '玛丽亚'
print(name)

#python中常用的数据类型
#整数型，浮点型，布尔型，字符串型
print(type(1))
print(type(1.1))
print(type('Ture'))
a = True
b = False
print(a,type(a))


#类型转换
name = '张三'
age = 20
print(type(name),type(age)) #说明两种该数据类型不一致
#print('我叫'+name+'今年,'+age+'岁') #两种类型连接是报错
print('我叫'+name+'今年'+str(age)+'岁') #将int类型转换成str类型
#str() int() float()


#python中的注释
#我日，这是一个注释
'''
这是一行注释
'''

'''
#iuput输入函数的使用
present = input('这是大圣的礼物吗')
print(present)

#input函数的高级使用
a=int(input('请输入一个加数：'))
b=int(input('请输入另一个加数：'))
print(a+b)
'''

#python中的运算符
#算术运算符
print(1+1)
print(1-1)
print(1*1)
print(1/1)
print(11//2) #最大整除数
print(11%4)  #取余
print(2**2)
print(9//4)
print(-9//-4)
print(9//-4)

#赋值运算符，运算顺序从右到左
i= 1+2
print(i)
#1,链式赋值
a=b=c=20
print(a,id(a))
print(b,id(b))
print(c,id(c))
#2,参数赋值
a=20
a+=30 #a=a+30
print(a)
a-=10 #a=a-10
a*=2 #a=a*2
print(a)

#3,解包赋值
a,b,c = 20,30,40
print(a,b,c)

#比23.较运算符
a,b = 10,20
print('a>b吗',a>b) #Flase
print('a<b吗',a<b) #Ture
print('a==b吗',a==b) #false
print('a<=b吗',a<=b) #Ture
#一个=是赋值运算符，两个=是比较运算符，一个变量由三部分组成：表示，类型，值
#==比较的是值还是标识呢，比较的是值，比较对象的表示使用is
a=10
b=10
print(a==b) #说明a与b的值相等
print(a is b)#说明a与b的标识相等
print(a is not b)

#24.布尔运算符
#Ture and Ture  = Ture
#Ture and false = false

a,b = 1,2
print('-----------and---------')
print(a==1 and b==2)
print(a==1 and b<2)
print(a!=1 and b==2)

print('-----------or---------')
print(a==1 or b==2)
print(a==1 or b<2)
print(a!=1 or b==2)

print('-----------not---------')
f = True
f2 = False
print(not f)
print(not f2)


print('-----------in与not in---------')
s='helloworld'
print('w' in s)
print('k' in s)
print('k' not in s)


#25.位运算符
print(4&8)
print(4|8)
print(4<<8)

#26.运算符的优先级
'''
算术>位运算>比较运算符>布尔运算
'''

#27.程序的组织结构_顺序结构
#把大象装冰箱一共分几步
print('-----程序开始-----')
print('1,把冰箱门打开')
print('2,把大象放冰箱里')
print('3,把冰箱门国关上')
print('------程序结束-----')

#28.测试对象的布尔值
#Python一切皆对象，所由对象都有一个布尔值
print(bool(False))
print(bool(0.0))
print(bool(None))
print(bool(''))
print(bool(""))
print(bool([]))
print(bool(list()))

#29.分支结构_单分支结构if
'''
money = 1000  #余额
s = int(input('请输入取款金额：'))  #取款金额
#判断余额是否充足
if money>=s:
	money=money-s
	print('取款成功，余额为：',money)
'''
	
# 30.分支结构_双分支结构if-else
'''
#键盘输入一个整数，编写程序让计算机判断是奇数还是偶数
num = int(input('请输入一个整数：'))
#条件判断
if num%2==0:
	print(num,'是偶数')
else:
	print(num,'是偶数')
	
'''
	
# 31.分支结构_多分支结构if-elif-else
'''
从键盘输入一个整数成绩
90-100 A  80-89 B  70-79 C  60-69 D  0-59 E
score=int(input('请输入一个成绩：'))
if score>=90 and score<=100:
	print('A级')
elif score>=80 and score<=89:
	print('B级')
elif score >= 70 and score <= 79:
	print('C级')
elif score >= 60 and score <= 69:
	print('D级')
elif score >= 0 and score <= 59:
	print('E级')
'''

#32.分支结构_嵌套if的使用
'''
会员   >=200  8折
      >=100  9折
      不打折
非会员 >=200  9.5折
	  不打折
answer = input('您是会员吗？y/n')
money=float(input('请输入您的购物金额'))
#外层判断是否为会员
if answer=='y':
	if money>=200:
		print('打8折，付款金额为：',money*0.8)
	elif money >=100:
		print('打9折。付款金额为：',money*0.9)
	elif money <100:
		print('不打折，付款金额为：',money)
else:
	if money>=200:
		print('打9.5折，付款金额为：',money*0.95)
	else:
		print('不打折，付款金额为：',money)
'''


#34.条件表达式
'''
从键盘录入两个整数，比较两个整数的大小

a = int(input('请输入第一个整数：'))
b = int(input('请输入第二个整数：'))
if a>b:
	print(a,'大于等于',b)
else:
	print(a,'小于',b)

print('使用条件表达式进行比较')
print((str(a)+'大于等于',+str(b)) if a>=b else str(a)+'小于'+str(b`))
'''


#35.PASS语句
#pass语句什么都不做，只是一个占位符，用到需要写语句的地方
'''
answer = input('您是会员吗？Y/N')

if answer=='y':
	pass
else:
	pass
'''


#36.range()函数的使用
#range()三种创建方式
'''第一种，只有一个参数，括号中只给了一个数'''
r = range(10)
print(r)
print(list(r))
'''第二种，给了两个参数，括号中给了两个数'''
r =range(1,10) #指定了起始值，从1开始，到10结束，不包括10
print(list(r))

'''第三种，给了三个参数，括号中给了三个数'''
r = range(1,10,3)
print(list(r))

'''判断指定的整数，再序列中是否存在，in,not in'''
print(10 in r) #false，10不在这个序列中
print(9 in r)  #false，9不在这个序列中
print(10 not in r)
print(range(1,20,1))
print(range(1,101,1))

#36.while循环 （if判断1次，while判断n+1次）
a = 1
#判断条件表达式
while a<10:
	#执行条件执行体
	print(a)
	a=a+1

#例子:计算0-4之间的累加和
'''
1.初始话变量
2.条件判断
3.条件执行体
4.改变变量
总结：初始化变量和与条件判断的变量与改变的变量为同一个
'''
sum = 0
a = 0
#条件判断
while a<5:
	#条件执行体（循环体）
	sum=sum+a
	#改变变量
	a=a+1
print('和为',sum)


#37.while练习题---1-100之间偶数的和
#初始化变量
sum =0
a=1
#条件判断
while a<=100:
	#条件执行体（求和）
	#判断是否为偶数
	if a%2 == 0:
		sum=sum+a
	a=a+1
print('1-100之间的偶数和',sum)


#38.for_in循环
for item in 'python': #第一次取出来的是p，将P复制给item输出
	print(item)

#range()产生一个整数序列，也是一个可迭代对象
for i in range(10):
	print(i)

#如果再循环体中不需要使用到自定义变量，可将自定义变量写为”_"
for _ in range(10):
	print('人生苦短，我只学python')
	
	
print('使用for循环，使1-100之间的偶数和')
sum = 0
for i in range(1,101):
	if i %2 ==0:
		sum=sum+i
print('1到100之间偶数和为',sum)


#39.for _in求100-999之间的水仙花数
#举例：153=3*3*3+5*5*5+1*1*1

'''没搞懂！！！'''



#40.流程控制语句break
'''从键盘输入密码，最多输入3次，如果正确就结束循环


for i in range(3):
	pwd = input('请输入密码：')
	if pwd == '888':
		print('密码正确')
		break
	else:
		print('密码不正确')
'''
'''
a=0
while a<3:
	pwd=input('请输入密码：')
	if pwd=='888':
		print('输入正确')
		break
	else:
		print('密码不正确')
'''

#41.流程控制语句continue
'''要求1-50之间所以5的倍数的共同点，和5的余数为0都是5的倍数
什么样的数，不是5的倍数a%5==0'''
'''

for i in range(1,51):
	if i%5 ==0:
		print(i)
print('----continue----')

for i in range(1,51):
	if i%5!=0:
		continue
	print(i)
	
	
#42.else语句
print('---------one---------')

for i in range(3):
	pwd = input('请输入密码：')
	if pwd == '888':
		print('密码正确')
		break
	else:
		print('密码不正确')
else:
	print('对不起，三次密码均输入错误')
	
	
print('---------two---------')

a=0
while a<3:
	pwd = input('请输入密码：')
	if pwd == '888':
		print('密码正确')
		break
	else:
		print('密码不正确')
		a = a+1
else:
	print('对不起，三次密码均输入错误')
	
	'''

#43.嵌套循环：嵌套循环中右嵌套了另外完整的虚幻结构，内循环做为外循环的循环体执行

'''输出一个三行四列的矩形'''
for i in range(3): #行数，一次是一行
	for j in range(4):
		print('*',end='\t') #不换行输出
	print()

'''依次打印每行多一个
for i in range(9):
	for j in range(1,i+1):
		print(i,'*',j,'=',i*j,end='\t')
	print()
'''

#44.二重循环中的Break和continue
'''流程控制break与continue再二重循环中的使用
for i in range(5):  #代表外循环要执行5次
	for j in range(1,11):
		if j%2 ==0:
			#break
			continue
		print(j,end='/t')
	print()
	
'''
#45.为什么需要列表，有序序列
'''
a = 10 #变量存储的是一个对象的引用
lst = ['hello','world',99]
print(id(lst))
print(type(lst))
print(lst)
'''
#46.列表对象的创建
'''第一种，使用[]'''
li=['hello','eorld']
'''第二种，使用内置函数list()
li2=list(['hello','world',98])
print(li2)
'''

#47.列表特点
'''
列表中的元素按照顺序有序排列
索引映射唯一的数据
可以存储重复数据
任意数据类型混存
根据需要动态分配和回收内存
'''

#48.获取指定元素的索引
'''
lst=['hello','world']
print(lst.index('hello'))#如果列表中有相同的元素，只返回列表中相同元素的第一个元素的索引
print(lst.index('Python'))#ValueError: 'Python' is not in list
print(lst.index('hello',1,3))#ValueError: 'Python' is not in list
print(lst.index('hello',1,4))
'''

#49.获取列表中的单个元素

'''
lst1=['hello','world',98,234,'nihao']
#获取索引为2的元素
print(lst1[2])
print(lst1[-3])
'''

#50.获取列表中的多个元素_切片操作
lst=[10,20,30,40,50,60,70,80]
#start=1.stop=6,step1
print(lst[1:6:1])
print('源列表',id(lst))
lst2=lst[1:6:1]
print('切的片段：',id(lst2))
print(lst[1:6])
print(lst[1:6:])
print(lst[1:6:2])

#51.列表元素的判断和遍历
print('p' in 'python')
print('p' not in 'python')

lst = [10,20,'python','hello']
print(10 in lst)
print(100 not in lst)

for i in lst:
	print(True)
	
	
#52.列表元素的添加操作
'''向列表中添加一个元素
append()在列表末尾添加元素
extend()在列表末尾至少添加一个元素
insert()在列表任意位置添加一个元素
切片，在列表的任意添加至少一个元素'''
ls = [10,20,30]
ls.append(12)
ls1=['hello']
ls.extend(ls1)
ls.insert(10,999)
print(ls)

ls2=[True,False,'hello'] #切掉
ls[1:]=ls2
print(ls)

#53.列表元素的删除操作
'''
1.remove()从列表移除一个元素，如果右重复元素只移除第一个
2.pop()根据索引移除元素，如果指定索引位置不存在，将抛出异常
3.切片，删除至少一个元素，将产生一个新的列表对象
4.clear()清除列表中的所有元素
5.del()语句，将列表删除

a = [10,20,30,30,40]
#a.remove(30)从列表移除一个元素，如果右重复元素只移除第一个
#a.pop(1)根据索引移除元素
#a.pop()如果不指定参数，将删除列表中的最后一个元素
#aa = a[1:3]
#a[1:3]=[]
#a.clear()清除列表中的所有元素
print(a)
'''


#54.修改元素的修改操作
a = [10,20,30,30,40]
#一次修改一个值
a[2]=100
print(a)
#修改列表多个值
a[1:3]=[300,400,500]
print(a)


#55.列表的排序操作
#1.开始排序，调用列表对象的sort方法， 升序排序
b = [102,20,330,3,40]
print('排序前的列表',b)
b.sort()
print('排序后的列表',b)
#2.通过指定关键字参数，将列表中的元素进行降序排序
b.sort(reverse=True)#reverse=ture表示降序排序，=false表示升序排序
print(b)
#3.使用内置函数sorted()对列表进行排序，经产生一个新的列表对象
c = [102,20,330,3,40]
cc=sorted(c)
print(cc)

#56.列表生成式
d=[i*i for i in range(1,10)]
print(d)
#列表中元素值为2，4，6，8，10
e = [i*2 for i in range(1,6)]
print(e)


#57.什么是字典
#字典是python内置的数据结构之一，与列表一样是一个可变序列
#以键值对的方式存储数据，字典是一个无序的序列{'张三':'11'}

#58.字典的实现原理
#字典的实现原理与查字典类似，查字典是现根据部首或拼音查找对于的页码
#python中的字典根据key查找values所在的位置

#59.字典的创建
score={'city':'上海','name':'阿修罗'}
print(type(score))
dict1=dict(name='阿修罗',age=20)
print(dict1)

#60.字典的元素获取
#1.第一种，使用[]，查找的键不存在，会报错
sc={'city':'上海','name':'阿修罗'}
#print(sc['city'])
#print(sc['jjj'])
#2.第二种，使用get()，查找的键存在，不会报错
print(sc.get('name'))
print(sc.get('急急急'))
print(sc.get('急',222))

#61.字典元素的增删改操作
#1.key的判断
scr={'city':'上海','name':'阿修罗'}
print('张三' in scr)
print('张三' not in scr)
#2.del字典元素的删除,删除指定的键值对
del scr['city']
print(scr)
#3.clear清空字典所有的键值对
#scr.clear()
#print(scr)
#4.新增元素
scr['李四']=90
print(scr)
#5.修改元素
scr['李四']=100
print(scr)

#62.获取字典视图
#1.keys()获取字典所有的key
skr={'city':'上海','name':'阿修罗'}
keys = skr.keys()
print(keys)
print(type(keys))
print(list(keys))
#2.values()获取字典中所有values
values = skr.values()
print(values)
print(type(values))
print(list(values))
#3.items()获取字典中所有的key,values对
items = skr.items()
print(items)
print(list(items))#转换之后的列表元素是由元组组成的


#63.字典元素的遍历
for item in skr:
	print(item,skr[item],skr.get(item))
	

#64.字典的特点
#1.字典所有元素都是一个key-values对，key不允许重复，values允许重复
#2.字典中元素是无序的
#3.字典中的key必须是不可变的对象
#4.字典也可以根据需要动态的伸缩
#5.字典浪费较大的内存，是一种使用空间换时间的数据结构
l = {'name':'张三','name':'李四'} #key不允许重复
print(l)
l = {'name':'张三','namelick':'李四'} #values允许重复
print(l)

#65.字典的生成式
#内置函数Zip()：用于将可迭代的对象作为参数，将对象中对应的元素打包成一个元组，
#然后返回由这些元组组成的列表

ite=['names','lights','Book']
prices=[90,34,23]
k={ite.upper():prices  for ite,prices in zip(ite,prices)}
print(k)

#66.什么是元组
#Python内置的数据结构之一，是一个不可变的序列
'''
不可变与可变序列
不可变序列：字符串，元组：没有增删改操作
可变序列：列表，字典：可以对序列进行增删改，对象地址不发生更改
'''
#可变序列：列表，字典
lis=[10,20,30]
print(id(lis))
lis.append(300)
print(id(lis))
#不可变序列:字符串，元组
s = 'hello'
print(id(s))
s=s+'word'
print(id(s))

#67.元组的创建方式
#1.使用(),只有一个元素的时候，必须加上,逗号
t = ('python','world',98)
print(t)
print(type(t))
#2.使用内置函数tuple()
t1=tuple(('python','world',98))
print(t1)
print(type(t1))

#68.为什么要将元组设计成不可变序列
'''
1.在多任务环境下，同时操作对象是不需要加锁，因此，在程序中尽量使用不可变序列
注意：如果元组中对象本身是不可变对象，则不能再引用其他对象
注意：如果元组中对象是可变对象，则可变对象的引用不可以改变，单数据可以改变
'''

#69.元组的遍历
t=('python','world',98)
'''第一种获取元素的方式：索引'''
print(t[0])
print(t[1])
print(t[2])
'''遍历元组'''
for i in t:
	print(i)
	
#70.集合的概述与创建
'''
python语言提供内置数据结构
与列表，字典一样属于可变类型的序列
集合没有values的字段
'''
#集合的直接创建
#1.使用{}直接创建
a={1,2,3,5,66,66,5} #集合中的元素不允许重复
print(a)
#2.使用内置函数set()
a1=set(range(6))
print(a1,type(a1))
a2=set([1,2,3,5,66,66,5])
print(a2)
a3=set('python')
print(a3,type(a3))
a4=set({1,2,3,5,66,66,5})
print(a,type(a4))
a5=set({})
print(a5,type(a5))

#71.集合的相关操作
'''
集合元素的判断操作：in not in
集合元素的新增操作：add()一次添加一个    update()至少添加一个
集合元素的删除操作：remove()一次删除一个指定元素，若不存在，抛出keyError异常
				discard()一次删除一个指定元素，若不存在，不抛出异常
				pop()一次只删除一个任意元素
				clear()清空集合
'''
'''
b={1,2,3,5,66,66,5}
print(2 in b)
print(2 not in b)
b.add(100)
print(b)
b1={1,2,3,5,66,66,5}
b1.remove(111)
b1.discard(33)
b1.pop()
'''
b2={1,2,3,5,66,66,5}
b2.clear()
print(b2)

#72.集合之间的关系
#1.两个集合是否相等
v={1,23,4}
v1={2,13,4}
print(v==v1)
print(v!=v1)
#2.一个集合是否是另一个集合的子集
b={1,2,3}
b1={1,2,3,4,5,6}
print(b.issubset(b1))
print(b1.issubset(b))
#3.一个集合是否为另一个集合的超集
print(b.issuperset(b1))
#4.两个集合是否存在交集
print(b.isdisjoint(b1)) #有交集为false  无交集为true


#73.集合的数据操作
#集合的数学操作
'''
#1.交集
a={10,20,30}
a1={10,23,4}
print(a1.intersection(a))
#2.并集操作
print(a1.union(a)) #union和|等价
print(a1|a)
#3.差集操作
print(a1.difference(a))
print(a1-a)
#4.对称差集
print(a1.symmetric_difference(a))

#74.集合生成式
#列表生成式
w=[i*i for i in range(6)]
print(w)
#集合生成式
w1={i*i for i in range(6)}
print(w1)
'''
#75.字符串的创建和驻留机制
#python中字符串是基本数据类型，是不可变的字符序列
'''
驻留机制的几种交互模式
1.字符串长度为0或1的时候
2.符合标识符的字符串
3.字符串旨在编译时进行驻留，而非运行时
4.【-5,256】之间的整数数字
优点：当需要值相同的字符串时，可以直接从字符串池里拿来使用，避免频繁创建和销毁，提升效率节约内存池
x= 'python'
y = "python"
print(x,id(x))
print(y,id(y))
'''


#76.字符串的常用操作_字符串的查询
'''
1.index()查找子串substr第一次出现的位置，如果查不到，抛出异常valuesError
2.rindex()查找子传substr最后一次出现的位置，如果查不到，抛出异常valesError
3.find()查找子串substr第一次出现的位置，如果不存在，则返回-1
4.efind()查找子串substr最后一次出现的位置，如果不存在，则返回-1


s='hello,hello'
print(s.index('lo'))#3
print(s.find('lo'))#3
print(s.rindex('l0'))#9
print(s.rfind('lo'))#9
print(s.find('k'))
'''
#77.字符串的常用操作_字符串大小写转换
'''
upper()把字符串所有字符都转换成大写字母
lower()把字符串所有字符都转换成小写字母
swapcase()把大小转化成小写，小写转换成大写
capitalize()第一个字符转化为大写，其余字符为小写
tittle()把每个单词的第一个字符转化成大写，每个单词剩余字符转化为小写

k ='hello,python'
k1=k.upper()
k2=k.lower()
k3=k.swapcase()
k4=k.capitalize()
k5=k.title()
print(k1)
print(k2)
print(k3)
print(k4)
print(k5)
'''

#78.字符串的常用操作_字符串内容对齐操作的方法
'''
center()居中对齐，第一个参数指定宽度，第二个参数指定填充符
ljust()左对齐，第一个参数指定宽度，第二个参数指定填充符
rjust()右对齐，第一个参数指定宽度，第二个参数指定填充符
zfill()右对齐，左边用0填充
'''
m='hello,worldHard'
print(m.center(20,'*'))
print(m.ljust(20,'*'))
print(m.rjust(20,'*'))
print(m.zfill(20,'*'))