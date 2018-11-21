# !/usr/bin/env python
#  -*- coding: utf-8 -*-
#  @Time : 2018/11/21 14:25
#  @Author : lg
#  @File : evaluation.py
import numpy as np

cost = np.array([[0, 0], [0, 0]])
# 定义所有的评价指标
from sklearn.metrics import classification_report, precision_score, recall_score, f1_score, accuracy_score, \
    roc_auc_score, confusion_matrix

def evalua(y_test, y_pre):
    # print(classification_report(y_test, y_pre))
    print('p = ', precision_score(y_test, y_pre))
    print('r', recall_score(y_test, y_pre, average=None))
    print('f1', f1_score(y_test, y_pre))
    # 第一个指标是精确度
    print('acc = ', accuracy_score(y_test, y_pre))
    # 第二个指标是G-mean
    recall_list = recall_score(y_test, y_pre, average=None)
    print('G-mean = ', G_mean(recall_list))
    # 第三个指标是每个cost矩阵对应的cost
    my_matrix = confusion_matrix(y_test, y_pre)
    print("my cost = ", get_cost(my_matrix, cost))


# 获得评价指标G-mean
def G_mean(lists):
    le = len(lists)
    result = 1
    for i in range(le):
        result = lists[i] * result
    return pow(result, 1 / le)


# 获得评价指标Cost
def get_cost(conf_matrix, cost):
    # print(conf_matrix)
    conf_matrix[0, 0] = 0
    conf_matrix[1, 1] = 0
    print(conf_matrix)
    result = np.matmul(cost.T, conf_matrix)
    # result[0,0]是cost(FN)*pro(FN)
    # result[1,1]是cost(FP)*pro(FP)
    # print("the result is:", result)
    cost_sum = result.sum(axis=0).sum(axis=0)
    print("all cost : ", cost_sum)
    return cost_sum
