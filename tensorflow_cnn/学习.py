#-*-coding:utf-8-*- 
# @File    : 学习.py
"""
http://www.360doc.com/content/19/0402/10/63179542_825878200.shtml
Label图 识别是什么
欠拟合:不认识相似的
提取特征feature
对应相乘取均值填入新图
stride步长每次移动像素

feature map是每一个feature从原始图像中提取出来的“特征”。其中的值，越接近为1表示对应位置和feature的匹配越完整，越是接近-1，表示对应位置和feature的反面匹配越完整，而值接近0的表示对应位置没有任何匹配或者说没有什么关联
Pooling池化
池化分为两种，Max Pooling 最大池化、Average Pooling平均池化。顾名思义，最大池化就是取最大值，平均池化就是取平均值。
拿最大池化举例：选择池化尺寸为2x2，因为选定一个2x2的窗口，在其内选出最大值更新进新的feature map。
"""