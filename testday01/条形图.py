'''
模板介绍：
coding: utf-8
Team : 无
Author：张恒瑞
Date ：2021/5/28 16:08
Tool ：PyCharm
'''
from matplotlib import pyplot as mpl, font_manager
from pymongo import MongoClient
mc=MongoClient(host="1.15.17.194",port=27017)
var = mc["you"]
var.authenticate("1822","zhr")
vars = var["dianying"]
title=[]
grade=[]
# 设置字体
for i in vars.find():
        title.append(i["title"])
        grade.append(i["pf"])


# 获取字体
fonts=font_manager.FontProperties(fname="C:\Windows\Fonts\simkai.ttf")
# 设置面板大小
mpl.figure(figsize=(20,8),dpi=80)
print(title[1:11])
print(grade[1:11])
# 绘制x ， y 轴
x_1=[i+0.2 for  i in range(len(title[1:11]))]
x_2=[i+0.2*2 for  i in range(len(title[1:11]))]

mpl.bar(range(len(title[1:11])),[float(i)  for  i  in grade[1:11]],width=0.2,label="第一天")
mpl.bar(x_1,[float(i)+1 for  i  in grade[1:11]],width=0.2,label="第二天")
mpl.bar(x_2,[float(i)-0.5 for  i  in grade[1:11]],width=0.2,label="第三天")
mpl.legend(prop=fonts)
mpl.xticks(x_1,title[1:11],fontproperties=fonts)
mpl.yticks(range(0,10))
# 设置  x y  中文字体
mpl.ylabel("电影评分",fontproperties=fonts)
mpl.xlabel("电影名",fontproperties=fonts)
# 设置标签
mpl.title("电影评分排行榜",fontproperties=fonts)
mpl.show()