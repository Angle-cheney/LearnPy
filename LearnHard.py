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

'''依次打印每行多一个'''
for i in range(9):
	for j in range(1,i+1):
		print(i,'*',j,'=',i*j,end='\t')
	print()


#44.二重循环中的Break和continue
'''流程控制break与continue再二重循环中的使用'''
for i in range(5):  #代表外循环要执行5次
	for j in range(1,11):
		if j%2 ==0:
			#break
			continue
		print(j,end='/t')
	print()
	
	
#45.为什么需要列表