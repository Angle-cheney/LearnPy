#121.什么是模块
'''
Python程序=模块+模块
模块=函数+类+语句。
类：类属性 类方法 静态方法 实例属性
好处：各司其职，便于分工，提高效率
'''
#122.自定义模块，模块导入
'''
新建一个.py文件，名称避免与自带的模块重复
导入模块 import 模块名称 ； from 模块名称 import 函数/变量/类
import math  #关于数学计算
print(id(math))
print(type(math))
print(math.pi)
print('---------')
print(dir(math))
print(math.pow(2,3),type(math.pow(2,3)))
print(math.ceil(9.001))
print(math.floor(9.999))

from math import pi
print(pi)
print(pow(2,3))
print(math.pow(2,3))'''
#123.以主程序方式运行
'''
在每个模块定义中都包括一个记录模块名称的变量__name__程序可以检查该变量，以确定在哪个模块执行
如果一个模块不是被导入其他程序中执行，那么她可能在解释器顶级模块中执行

def add(a,b):
	return a+b
if __name__ == '__main__': #设置主程序的时候，如果是被引入的，则不会执行
	print(add(10,20))'''
#124.python中的包
'''
作用：
1.代码规范
2.避免模块名称冲突
包与目录区别：
1.包含__init__.py文件的目录称为包
2.目录里通常不包含__init__py文件
包的导入：
import 包名.模块名
'''
#125.python常用的内置模块
'''

import sys #与python解释器及环境相关的标准库
print(sys.getsizeof(24))
print(sys.getsizeof(400))
print(sys.getsizeof(True))

import time #和时间相关的标准库
print(time.time())
#time.sleep(2)
print(time.localtime(time.time()))

import os #提供访问操作系统服务功能的标准库
print(os.name)
print(os.path)
print(os.times())

import calendar #提供与日期相关的各种函数标准库
print(calendar.day_name)

import urllib #用于读取来自网上的数据标准库
print((urllib))

import json #用于读取JSON序列化和反序列化对象
#print(((json))

import re  #用于在字符串执行正则表达式匹配和替换
print(re.ASCII)

import math #提供标准算术运算符
print(math.floor(1.1))

import decimal  #用于进行精确控制运算符，有效数位，四舍五入的十进制操作
print(decimal.Decimal)

import logging #提供了灵活的记录事件，错误，警告和调试信息等日志信息的功能
print(logging.getLogger())

'''

#126.第三代模块安装与使用
'''
安装：pip install 模块名
使用：import 模块名
'''

#127.编码格式的介绍
'''
常见编码格式
1.python解释器使用的是Unicode（内存）
2..py文件在磁盘上使用utf-8存储（外存）
ASCII---ISO8859-1---GB2312---GBK---GB18030---英文1个字节，汉字2个字节
ASCII---ISO8859-1---UTF-8---英文1个字节，汉字3个字节
ISO8859-1---不兼容---Unicode
'''
#128.文件读写原理_读写磁盘文件中的内容
'''

1.文件读写俗称IO（input Output）
2.文件读写操作流程，
3.操作原理
4.内置函数open()创建文件对象
5.语法规则：file
'''
#129.常用的文件打开模式
'''
#读取
file = open('a.txt','r')
print(file.readline())
file.close()
#创建
file = open('b.txt','w')
print(file.write('python'))
file.close()
#追加
file = open('b.txt','a')
print(file.write('python'))
file.close()
#复制
scr_file = open('b.png','rb')
targat_file = open('cop.png','wb')
targat_file.write(scr_file.readline())
scr_file.close()'''

#130.文件对象的常用方法
'''
read([size])从文件在读取size个字节，若省略，则读取全部内容
readline()读取一行内容
readlines()将每行读取的对象放入列表返回
write(str)将字符串str内容写入文件
writelines(s_list)将字符串列表s_list写入文本文件，不添加换行符
seek_offset[.whence]把文件指针移动新位置，offset表示相对于whence位置
					offset正往结束方向移动，为负往开始方向移动
tell()返回文件指针的当前位置
flush()

file = open('a.txt','r')
print(file.read(2))
print(file.readline())
'''

#131.with语句
'''
with语句可以自动管理上下文资源，不了社么愿意跳出with块，都能确保文件正确的关闭，达到释放资源的目的

with open('a.txt','r') as File:
	print(File.read())'''

#132.os函数的常用函数
'''
os函数调用

import os
os.system('notepad.exe')
os.system('calc.exe')
os.startfile('D:\\QQ\\Bin\\qq.exe')


import os
print(os.getcwd())
a=os.listdir('/third')
print(a)'''

#133.os.path模块常用方法
'''
#列出指定目录下所以python文件
import os
path = os.getcwd()
a=os.walk(path)
for dirpath,dirname,filename in a:
	print(dirname)
	print(dirpath)
	print(filename)
print('-------***-------')
lst = os.listdir(path)
for filename in lst:
	if filename.endswith('.py'):
		print(filename)
		'''
