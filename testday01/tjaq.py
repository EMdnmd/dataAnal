'''
模板介绍：
coding: utf-8
Team : 无
Author：张恒瑞
Date ：2021/5/26 10:17
Tool ：PyCharm
'''

from matplotlib import pyplot  as pit, font_manager
fonts=font_manager.FontProperties(fname="C:\Windows\Fonts\simkai.ttf")
pit.title("小张20年交友数",fontproperties=fonts)
pit.ylabel("交友数",fontproperties=fonts)
pit.xlabel("年龄",fontproperties=fonts)
pit.figure(figsize=(20,10),dpi=80)
_y=[1,2,1,2,3,2,2,3,3,2,3,1,3,2,3,1,3,1,4,2]
_y2=[3,5,8,9,8,2,3,4,5,5,6,6,6,6,6,3,3,1,3,2]
# 绘制交友数
pit.yticks(range(0,9))
# 绘制年龄
mc=["{}岁".format(i) for  i in range(11,31,2)]
yz=[i for  i in range(1,21,2)]
pit.xticks(yz,mc,fontproperties=fonts)
_x=[i for  i in range(1,21)]
# 设置表格
pit.grid(alpha=0.4)
pit.plot(_x,_y,label="自己",)
pit.plot(_x,_y2,label="同桌")
pit.legend(prop=fonts)
pit.show()

