'''
模板介绍：
coding: utf-8
Team : 无
Author：张恒瑞
Date ：2021/5/26 15:58
Tool ：PyCharm
'''
from random import randint
from matplotlib import pyplot as pit, font_manager

lista=[]
listb=[]
for i in range(30):
    a=randint(10,30)
    lista.append(a)
    b=randint(10,30)
    listb.append(b)
pit.figure(figsize=(20,8),dpi=80)
fonts=font_manager.FontProperties(fname="C:\Windows\Fonts\simkai.ttf")

x=range(1,31)
y=range(41,71)
s=list(x)+list(y)
_x=["三月{}号".format(i) for  i in x]
_x+=["十月{}号".format(i-40) for  i in y]

pit.scatter(x,lista)
pit.scatter(y,listb)

pit.xticks(s,_x,fontproperties=fonts,rotation=270)
pit.show()
