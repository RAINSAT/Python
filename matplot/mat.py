# -*- coding:utf-8 -*-

# Numpy N维数组 矩阵 运行效率高
# Scipy 专为科学和工程设计： 线性代数 傅里叶变换 信号和图像处理
# Pandas 结构化数据分析利器： Time-Series DataFrame Panel 强大的数据索引和处理能力
# Matplotlib Python 2D 绘图 基本能取代Matlab的绘图功能 通过mplot3d 可以绘制精美的3D图
# Scikit-learn 机器学习的Python 模块 建立在 Scipy 之上 提供了常用的机器学习算法：聚类 回归 简单易学的API


import numpy as np
import matplotlib.pyplot as plt

def show():
    x = np.linspace(-3,3,10)
    y = np.sin(x)
    plt.figure(num='sin')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('x--y')
    plt.plot(x,y,color='red',linewidth=1.0,linestyle='--',label='y=sin(x)')
    plt.legend(loc='lower right')
    plt.figure(num='x=x')
    plt.plot(x,x)
    plt.show()

if __name__ == '__main__':
    show()
