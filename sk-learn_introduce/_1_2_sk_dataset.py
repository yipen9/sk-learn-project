# _*_ coding:utf-8 _*_


#iris 数据集(鸢尾花卉数据集)
# 每一行代表一个样本，每一列代表一种特征


from sklearn import datasets

iris = datasets.load_iris()

data = iris.data

print data.shape

# 样本包含4个特征：花萼长度，花萼宽度，花瓣长度，花瓣宽度
print data[:1]



# digits数据集包含1797个手写数字的图像，每个图像为8*8像素

digits = datasets.load_digits()

print digits.images.shape


import matplotlib.pyplot as plt

plt.imshow(digits.images[-1],cmap=plt.cm.gray_r)
# plt.show()
print digits.target[-1]

print digits.images.shape[0]

# 如果等于-1的话，那么Numpy会根据剩下的维度计算出数组的另外一个shape属性值

data = digits.images.reshape((digits.images.shape[0],-1))

print data[1]









# 拟合数据: scikit-learn实现最重要的一个API是`estimator`。
# estimators是基于数据进行学习的任何对象，
# 它可以是一个分类器，回归或者是一个聚类算法，或者是从原始数据中提取/过滤有用特征的变换器。










