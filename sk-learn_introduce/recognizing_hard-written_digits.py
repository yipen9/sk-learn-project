# _*_ coding:utf-8 _*_

import matplotlib.pyplot as plt

#导入数据集,svm分类器,
from sklearn import datasets,svm,metrics


digits = datasets.load_digits()


images_and_labels = list(zip(digits.images,digits.target))

for index , (image,label) in enumerate(images_and_labels[:4]):
    plt.subplot(2,4,index+1)
    plt.axis('off')
    plt.imshow(image,cmap=plt.cm.gray_r,interpolation='nearest')
    plt.title('Training:%i' %label)


n_samples = len(digits.images)
data = digits.images.reshape((n_samples,-1))

classifier = svm.SVC(gamma=0.001)

# a[1: ] 表示该列表中的第1个元素到最后一个元素，而，a[ : n]表示从第0歌元素到第n个元素(不包括n)

classifier.fit(data[:n_samples // 2],digits.target[:n_samples // 2])    #一半数据用于训练

expected = digits.target[n_samples // 2 : ]


predicted = classifier.predict(data[n_samples // 2 :])

print("Classification report for classifier %s:\n%s\n"
      % (classifier, metrics.classification_report(expected, predicted)))

print("Confusion matrix:\n%s" % metrics.confusion_matrix(expected, predicted))


# 用手写数字识别来作为说明。
# 准确率： 所有识别为”1”的数据中，正确的比率是多少。
# 如识别出来100个结果是“1”， 而只有90个结果正确，有10个实现是非“1”的数据。 所以准确率就为90%
#
# 召回率： 所有样本为1的数据中，最后真正识别出1的比率。
# 如100个样本”1”, 只识别出了93个是“1”， 其它7个是识别成了其它数据。 所以召回率是93%
#
# F1-score:  是准确率与召回率的综合。 可以认为是平均效果。
#
#
# 详细定义如下：
# 对于数据测试结果有下面4种情况：
# TP: 预测为正， 实现为正
# FP: 预测为正， 实现为负
# FN: 预测为负，实现为正
# TN: 预测为负， 实现为负
#
# 准确率： TP/ (TP+FP)
# 召回率： TP(TP + FN)
# F1-score: 2*TP/(2*TP + FP + FN)



images_and_predictions = list(zip(digits.images[n_samples // 2:], predicted))
for index, (image, prediction) in enumerate(images_and_predictions[:4]):
    plt.subplot(2, 4, index + 5)
    plt.axis('off')
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title('Prediction: %i' % prediction)

plt.show()