'''
模板介绍：
coding: utf-8
Team : 绘制直方图
Author：张恒瑞
Date ：2021/5/31 14:50
Tool ：PyCharm
'''
import random

from  pymongo  import  MongoClient as mc
from  matplotlib  import  pyplot  as  plt

datalist=[]
for i in range(250) :
     datalist.append(random.randint(60,250))
# 绘制面板大小
plt.figure(figsize=(20,8),dpi=80)
# 绘制直方图
# 计算组数
b=10
print(max(datalist),min(datalist))
maxmix=(250-60)//b
print(maxmix)
plt.hist(datalist,maxmix)
plt.grid(alpha=0.4)
# 获知 y 和  x 轴
plt.xticks(range(60,250+5,b))

# 显示图形
plt.show()