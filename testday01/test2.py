'''
模板介绍：
coding: utf-8
Team : 温度
Author：张恒瑞
Date ：2021/5/25 11:37
Tool ：PyCharm
'''
from random import randint
from  matplotlib import  font_manager

font = {'family': '宋体',
        'weight': 'bold',
        'size': '10'}
from  matplotlib import  pyplot as plt
# 设置字体
fonts=font_manager.FontProperties(fname="C:\Windows\Fonts\simkai.ttf")
plt.figure(figsize=(20,8),dpi=80)

y=[randint(20,35)for i in range(120)]

plt.yticks(range(20,35))

x=range(0,120)

lx=list(x)[::3]

_x_m=["10点{}分".format(i) for  i in  range(60)]
_x_m+=["11点{}分".format(i) for  i in  range(60)]
# 把数值对应到字符串上面
plt.xticks(lx,_x_m[::3] ,rotation=270,fontproperties=fonts) # rotation 旋转90渡
# 添加描述信息
plt.xlabel("时间",fontproperties=fonts)
plt.ylabel("温度",fontproperties=fonts)
plt.title("十点到十二点每分钟的气温的变化情况",fontproperties=fonts)

plt.plot(x,y)

plt.show()