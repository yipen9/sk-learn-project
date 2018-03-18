# _*_ coding:utf-8 _*_

#scikit-learn提供了标准数据集,用于分类的iris和digits数据集
#波士顿房价回归数据集


from sklearn import datasets

iris = datasets.load_iris()

digits = datasets.load_digits()

#数据集是一个类似字典的对象,它保持有关数据的所有数据和一些原数据
# 保存在.data 成员中,它是n_samples , n_features 数组，一个或
# 多个标签变量存储在.target成员中


print(digits.data)

print(digits.target)


