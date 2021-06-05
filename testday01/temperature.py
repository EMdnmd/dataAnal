'''
模板介绍：
coding: utf-8
Team : 无
Author：张恒瑞
Date ：2021/5/25 11:08
Tool ：PyCharm
'''
# from  matplotlib import pyplot as  plt
# # 设置宽高   figsize:设置宽高   dpi:每英寸上点的个数
# plt.figure(figsize=(20,8),dpi=80)
# x=range(2,26,2)
#
# y=[15,13,14.4,17,13,14,14,16,13,14,15,13]
# #导入x y的数据
# plt.plot(x,y)
# # 绘制x轴的刻度
# plt.xticks(x)
# # 绘制y轴的刻度
# # plt.yticks(y)
# # 保存图片
# # plt.savefig("./temp.svg")
# plt.show()
from random import randint

from  matplotlib import  pyplot as plt

# plt.figure(figsize=(20,80),dpi=80)

# plt.xticks(range(20,35))
# plt.yticks(range(0,120))
x=range(0,120)
y=[randint(20,35)for i in range(120)]
plt.plot(x,y)
plt.show()