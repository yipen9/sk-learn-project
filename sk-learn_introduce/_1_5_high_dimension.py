# _*_ coding:utf-8 _*_


# 监督学习：从高维观察预测输出变量


#  sk-learn 中所有监督的估计量都有一个用来拟合模型的fit(X,y) 方法，和根据给定的
# 没有标签观察值 X 返回 预测标签的 y 的 predict(X) 方法


# 最近邻   NearestNeighbor
# 也许是最简单的分类器：
# 给定一个新的观察值 X_test，用最接近的特征向量在训练集
# (比如，用于训练估计器的数据)找到观察值

import numpy as np

from sklearn import datasets

iris = datasets.load_iris()

iris_X = iris.data

iris_y = iris.target

print np.unique(iris_y)
