'''
模板介绍：
coding: utf-8
Team : numpy学习
Author：张恒瑞
Date ：2021/5/31 16:15
Tool ：PyCharm
'''
import  numpy  as np
def     num():
    a=[1,2]
    b=[3,4]
    s=np.arange(24)
    print(s.ndim)
    e=s.reshape(4,3,2)
    print(e)
    print(e.ndim)
    print(e.flags)
    print(e.real)
    print(e.imag)


def chuangjian1num():
                n=np.empty([3,3],dtype=int,order="F")
                print(n)


# 创建使用数值范围创造数组数值
def num01():
        s=np.arange(10,100,10,dtype=float)
        print(s)

def num02():
        s=np.arange(12)
        a=s.reshape(4,1,3)
        print(a)

num02()