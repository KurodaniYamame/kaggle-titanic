# Kaggle泰坦尼克号项目

这是我参与的第一个 Kaggle 机器学习项目。也是第一个认真的github提交（迫真

## 任务

根据表格中的乘客信息，预测某位乘客是否在泰坦尼克号灾难中幸存下来。

## 数据集

数据集：Kaggle Titanic - Machine Learning from Disaster
主要文件：

- train.csv
- test.csv
- gender_submission.csv

## 方法

我使用了一个简单的基线模型：

- 选定的feature：Pclass, Sex, Age, SibSp, Parch, Fare
- 将Sex从字符串类型转换为数字类型：
  - Male = 0
  - Female = 1
  - 用中位数填充缺失的年龄和票价值
  - 使用 scikit-learn 中的随机森林分类器进行训练

## 结果

Kaggle 公开得分：
0.73923

## 代码

test.py

## 其他

该项目主要是为了实践完整的机器学习工作流程：
读取 CSV 数据
清理简单的表格数据
训练基础模型
生成提交文件
提交至 Kaggle
