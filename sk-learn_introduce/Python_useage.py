# _*_ coding: utf-8 _*_




import numpy as np

arr = np.array([[1,3,4],[2,4,5]])

# 如果等于-1的话，那么Numpy会根据剩下的维度计算出数组的另外一个shape属性值
data1 = arr.reshape(-1,2)
data2 = arr.reshape(-1)     #整行
data3 = arr.reshape(-1,1)   #整列

print data1.shape
print data2
print data3


X = np.sort(5 * np.random.rand(40, 1), axis=0)  # 产生40组数据，每组一个数据，axis=0决定按列排序(所有列都排序)，=1表示行排列(所有行)
X2 = np.sort(5 * np.random.rand(40, 2), axis=0)
print X
print X2


y = np.sin(X).ravel()  # np.sin()输出的是列，和X对应，ravel表示转换成行

print y

# a[1: ] 表示该列表中的第1个元素到最后一个元素，而，a[ : n]表示从第0歌元素到第n个元素(不包括n)


# 表示行数不变，列只取前两列
X3 = arr[:,:2]
print X3


#numpy 中 meshgrid函数用两个坐标轴上的点在平面上画网格

# [X,Y] = meshgrid(x,y)
# [X,Y] = meshgrid(x) 与 [X,Y] = meshgrid(x,x)是等同的
#[X,Y,Z] = meshgrid(x,y,z)生成三维数组，可以来计算三变量的函数和绘制三维立体图

# [X,Y] = meshgrid(x,y) 将向量x和y定义的区域转换成矩阵X和Y,
# 其中矩阵X的行向量是向量x的简单复制，而矩阵Y的列向量是向量y的简单复制


# 假设x是长度为m的向量，y是长度为n的向量，则最终生成的矩阵X和Y的维度都是 n,m

print '---------------------------------------------------------'
m,n = (5,3)
x = np.linspace(0,1,m)
y = np.linspace(0,1,n)
X,Y=np.meshgrid(x,y)

print x
print y
print X
print Y



print X.flat

import matplotlib.pyplot as plt

plt.plot(X, Y, marker='.', color='blue', linestyle='none')
plt.show()













